# {{cookiecutter.project_name}}

==============================

TODO: provide guidance on using XGBoost with PySpark
[https://xgboost.readthedocs.io/en/stable/tutorials/spark_estimator.html](https://xgboost.readthedocs.io/en/stable/tutorials/spark_estimator.html)

{{cookiecutter.description}}

## Project Organization

------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── scripts            <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## PySpark Quickstart

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = (SparkSession
    .builder
    .appName("MyApp")
    .config("spark.executor.memory", "8g")
    .config("spark.executor.pyspark.memory", "8g")
    .config("spark.driver.memory", "16g")
    .getOrCreate()
)

schema = StructType([
    StructField(name="col1", datatype=StringType(), nullable=True, metadata=None),
    ...
])

data = "../data/raw/dataset.csv"
df = (spark
    .read
    .format("csv")
    .options(
        header=True,
        encoding="utf8",
        schema=schema,
    )
    .load(data)
)
df.withColumn("value", df["value"].cast("double"))

df.createOrReplaceTempView("data")
spark.sql("SELECT industry, value FROM data")

target_col = "value"

## Categorical Variables
cat_cols = ["col1", "col2"]
cat_cols_out = [col + "_idx" for col in cat_cols]

categorical = []
for i in range(len(cat_cols)):
    categorical.append(
        StringIndexer(inputCol=cat_cols[i], outputCol=cat_cols_out[i])
    )

## Encoding
one_hot_col_out = [col + "_enc" for col in cat_cols_out]
one_hot = OneHotEncoder(inputCols=cat_cols_out, outputCols=one_hot_col_out)

## Assembler
assembler = VectorAssembler(inputCols=one_hot_col_out, outputCol="features")

## Feature Engineering
feat_pipeline = Pipeline(stages=categorical + [one_hot, assembler])
feat_df = feat_pipeline.fit(df).transform(df).select("features", target_col)
feat_df.show(3)

## Train/Test split
train_df, test_df = feat_df.randomSplit([0.7, 0.3], seed=42).repartition(48)

## Cross-Fold Validation
ml = RandomForestRegressor(labelCol=target_col, featuresCol="features", seed=42)

param_grid = (ParamGridBuilder()
    .addGrid(ml.maxBins, [2,3,4,5,6])
    .addGrid(ml.maxDepth, [1,2,4,6,8,10,12,14,16,18.20,22,24,26,28,30])
    .addGrid(ml.minInstancesPerNode, [1,2,3])
    .addGrid(ml.numTrees, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
)

evaluator = RegressionEvaluator(
    predictionCol=target_col,
    labelCol="prediction",
    metricName="rmse",
)

crossval = CrossValidator(
    estimator=Pipeline(stages=[ml]),
    estimatorParamMaps=param_grid,
    evaluator=evaluator,
    numFolds=5,
)

cv_model = crossval.fit(train_df)
cv_model.bestModel.explainParams()
cv_model.bestModel.extractParamMap()
cv_model.bestModel.params
cv_model.bestModel.featureImportances
```
