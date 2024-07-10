# Intial Data Analysis/Exploratory Data Analysis

General Rule of Thumb:
You need at least 10 times more instances than features in order to expect
some good results.

TODO: SOP for standard visualization techinques required for:

- scatter plots
- line plots
- horizontal bar plots
- histograms/kernel density plots (skew, kurtosis)
- box and whisker plots for data distribution

TODO: SOP for anomaly detection

## Introduction

We are done when:

- we have expectations for the data and how it changes over time or category
- a "target" variable has been identified and the relationship with other
  variables is understood

Goals:

- identify the "target" variable (the one we want to predict)
- identify the relationships between the target variable and other variables
- identify features that can be extracted from related variables
- examine the distribution of the feature variable to the target variable via
  box and whisker plot.

Tools to use:

- pandas
- matplotlib
- sklearn
- statsmodels
- jupyter
- yellowbrick
- plotly
- xgboost
- lightgbm
- fastcluster
- hdbscan
- tslearn

TODO:

- Frequentist Statistics method
- Bayesian data analysis (conditional probability conclusions based on priors)
- %lsmagic in cells for timing and performance measures

## 1. Data Load and Schema

We are done when:

- durations, dates and times are prased accordingly w/time zone analysis
- dtype and converers are written in our load_data() function
- data can be loaded with a schema (no more autodetection)
- time periods are regular/consistent (no missing data points IF doing i
  time series analysis)
- missing values are imputed without skewing the median

Set the schema via parse_dates=[4], "dtype" and "converters"

```python
pd.read_csv(
   "myfile.csv",
   dtype = {"col1": "int"},
   parse_dates = ["coldt", "coldt2"],
   converters={"col1", convert_currency, "col2": pd.to_numeric(x, errors="coerce")}
)
```

```python
print("schema_VENDOR_OBJECT_v1 = {")
for n, t in zip(df.dtypes.index, df.dtypes.values):
   if t == "bool" or t == "object":
      print(f"   '{n}': {t},")
   else:
      print(f"   '{n}': np.{t},")
print("}")
```

### Cardinality Counts

```python
for c in df.columns:
   print(df[c].fillna("").value_counts().sort_values(ascending=False)[:5]
   print()
```

### Date Handling

- impute missing values
- upscale/downscale data
- date/datetime timezone identification

```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df.apply(lambda r: r["date"].year, axis=1)
df["month"] = df.apply(lambda r: r["date"].month, axis=1)
df["day"] = df.apply(lambda r: r["date"].day, axis=1)
```

### Null/NA

```python
df.isnull().any()
```

### Value Counts

TODO: put in code you used for Series index/data

```python
df.apply( pd.value_counts )

# or

df.col1.value_counts()
```

## 2. Classify columns into NOIR for further analysis

We are done when we have classified data into statistical
types, nominal, ordinal, interval and ratio.

```python
null_col = []
features_col = []
target_col = []

nominal_col = []
ordinal_col = []
interval_col = []
ratio_col = []
```

## 3. Identify  features for Transformation

- categorical variables must be encoded (is there a natural order)?
- heatmap of numerical correlation

```python
numeric_columns = df.select_dtypes(include=["number"])
numeric_columns.corr()
numeric_columns.cov()
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_columns.corr(), annot=True)
plt.title("The correlation matrix of the numeric columns", y=1.2)
plt.show()
```

- feature correlation before jumping into regression

```python
from yellowbrick.target import FeatureCorrelation
feature_names = features.columns
visualizer = FeatureCorrelation(labels = feature_names)
visualizer.poof()
```

- pearson correlation coefficient:

```python
df.corr()['Target'][:].sort_values(ascending=False)
```

- visualize:

```python
# visualize correlation between a column and the target
pd.plotting.scatter_matrix(df[feature_ratio], alpha=0.2, diagnal='hist', figsize(12,18))
```

- examine the feature data distribution relative to the target

```python
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="feature", y="target")
```

- for geospatial visualize location given the target to figure out how to
  create a new feature to capture the location.

```python
plt.figure(figsize=(10,6))
upper_half_filter = df["price"] > df["price"].median()
sns.scatterplot(data=df[upper_half_filter], x="long", y="lat", hue="price")
```

## 4. Normalizing/standardizing  and cleaning data

NOTE: Chapter 7: Wrangling with Python

- TODO: reshaping and pivoting
- TODO: data transformation
- TODO: joining/merging datasets

NOTE: Chapter 8 Data Wrangling with Python

- TODO: scripting data cleanup
- TODO: testing data cleanup
- TODO: saving "normalized" and "standardized" data

## 5. Exploratory Data Analysis (John Tukey's Approach)

Summarize and visualize main characteristics.  We are done when we have set
expectations for "typical" values and understand the relationships between
different attributes (columns) in our data.  Outliers have been quantified
(e.g., > 3 standard deviations)

- Historgram (see data distribution)

```python
df[features].hist(bins=50, figsize=(12,12))
plt.show()
```

- Frequency counts (see above)
- Descriptive statistics (mean, std, median, normality histogram skewness/kurtosis, freq)

### 5a. Univariate exploratory data analysis

Is this data autoregressive?

Autocorrelation and autoregression over one hour and twelve hours

```python
df[["col1"]].autocorr(lag=60)
df[["col1"]].autocorr(lag=60 *12)

# plot to understand the range
fix, ax1 = plt.subplots(1, figsize=(12, 14))
ax1.acorr(global_intensity_column, maxlags=60*12, color="blue")
ax1.title.set_text("Global Intensity")
ax1.set_xlabel("Lags", fontsize=15)
plt.show()

TODO: Autoregression
```

Distribution of this feature:

- mean, median, mode
- max, min and std dev
- unique values and missing data
- visual exploration (see below)

Categorical Univariate data analysis:

- horizontal bar plot by category
- pie graph (proportion of categories)
- top 10

Continuous Univariate data analysis:

- histogram
- box plot
- violin plot [https://matplotlib.org/stable/gallery/statistics/violinplot.html](https://matplotlib.org/stable/gallery/statistics/violinplot.html])

```python
plt.scatter(x, y, c = np.random.rand(N), alpha=0.5)
df.assign(index=df.groupby('column').cumcount()).pivot('index', 'column').plot(kind='box')
```

### 5b. Bivariate exploratory data analysis

- scatter plot
- box and whisker plot showing the interquartile range (IQR)
- box plot

```pandas
import seaborn as sns
ax = sns.boxplot(x="relatedCol", y="univariateCol", data=df, palette="Set3")
plt.boxplot(df[features])
plt.show()
```

### 5c. Baysian Data Analysis

TODO: fill this in for conditional probability

### 5d. Analytics

TODO: Chapter 9: Python for Data Analysis: Data Aggregation and Group Operations

- Pivot tables and cross-tabulation
- group by

## 6. Modeling and autocorrelation

PCA
XGBoost
LinearRegression
