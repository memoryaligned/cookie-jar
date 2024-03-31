# Intial Data Analysis/Exploratory Data Analysis

General Rule of Thumb:
You need at least 10 times more instances than features in order to expect
some good results.

## Introduction

We are done when:

- we have expectations for the data and how it changes over time or category
- a "target" variable has been identified and the relationship with other
  variables is understood

Goals:

- identify the "target" variable (the one we want to predict)
- identify the relationships between the target variable and other variables
- identify features that can be extracted from related variables

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
print("schema_VENDOR_OBJECT_v1 = {")
for n, t in zip(df.dtypes.index, df.dtypes.values):
   if t == "bool" or t == "object":
      print(f"   '{n}': {t},")
   else:
      print(f"   '{n}': np.{t},")
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

### Null/NA

```python
df.isnull().any()
```

### Value Counts

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

nominal_col = []
oridnal_col = []
interval_col = []
ratio_col = []
```

## 3. Identify  features for Transformation

- categorical variables must be encoded (is there a natural order)?
- pearson correlation coefficient:

```python
df.corr()['Target'][:].sort_values(ascending=False)
```

- visualize:

```python
# visualize correlation between a column and the target
pd.plotting.scatter_matrix(df[feature_ratio], alpha=0.2, diagnal='hist', figsize(12,18))
```

## 4. Cleaning, investigation, matching and formatting

NOTE: Chapter 7: Wrangling with Python


