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
schema_vendor_v1 = {
   'COL1': np.float64,
   'COL2': np.int64,
   'COL3': np.object,
}

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
