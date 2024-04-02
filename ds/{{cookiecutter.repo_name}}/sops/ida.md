# Intial Data Analysis/Exploratory Data Analysis

## Notebook structure

1. Load Data
2. Attribute Cardinality
3. Classify columns into NOIR
4. SQL DDL
5. Visualize Nominal Data

```python
def hbar_category(category: str, save_path: str) -> None:
   plt.clf()
   fig = plg.gcf()
   fig.set_size_inches(8,4)
   cat_df = df[category].value_counts().sort_values().reset_index()[:20]
   plt.barh(cat_df[category], cat_df["count"])
   plt.title(f"attribute: {category}\nTop20")
   plt.savefig(save_path)

for c in nominal_col:
   sanitize_c = c.lower().replace(" ", "_").replace("#", "no")
   hbar_category(c, f"../reports/figures/{sanitize_c}_hbar.png")
```

NOTE: to include the image in your Sphinx report:

```
.. image:: ../../reports/figures/c_hbar.png
```

## 1. Metadata Setup

Know what your numbers represent comprising of the characteristics of the data
supplemented by background domain knowledge, how they were generated and its
intended use.  Metadata is comprised of data dictionary information:

- labels
- plausability limits
- codecs for missing data
- measurement units
- expectations about distributional properties and associations
- frequency and proportion of missing values for each variable

Develop an IDA plan that supports the research objective

- assesses the distribution and scale of variables
- check for unusual or implausible observations
- summarize missing data patterns
- investigate data facets that could influence formal analysis

NOTE: projects should include the setup, management and publishing of metadata
with a data management and stewardship plan.  This allows the unambiguous
meaning and interpretation of data which allows positive feedback loops and
building on top of existing data resources.

## 2. Data Cleanup

Make IDA reproduceable by keeping track of changes that you or your
collaborators make to project data (e.g., analysis scripts, libraries and
packages).  The golden rule is to NOT change or overwrite the source data.

All derivations from the source data including the lineage of new variables
and rationale for the derivation should be clearly documented with a clear
description of all the data cleaning rules.

Missing data could introduce important bias in the data and reduce the
statistical power of the data.

NOTE: Chapter 8 Data Wrangling with Python

- TODO: scripting data cleanup
- TODO: testing data cleanup
- Frequency counts (see above)
- Descriptive statistics (mean, std, median, normality histogram skewness/kurtosis, freq)
## 3. Data Screening

- sample size
- exclusion criteria
- inclusion criteria
- subsequent selections to arrive at the sample size used for the analysis

## 4. Initial Data Reporting

Communicate clearly:

- methods or decision rules for data pre-processing
- possible changes to the statistical analysis plan (SAP)
- flow chart of the study inclusion with a table of important variables with
  numbers of missing values should be placed in the results section.  
  NOTE: Google "Flow chart of the study inclusion for examples."

- TODO: saving "normalized" and "standardized" data
- Historgram (see data distribution)

```python
df[features].hist(bins=50, figsize=(12,12))
plt.show()
```

## 5. Refining/updating the research analysis plan

A good understanding of (a) the research question, (b) the intended analysis
and (c) the data are all required to execute the analysis adequately and
correctly interpreting the results.  Matching the relevance of the data to the
research question has been termed the "zeroth problem."

It is important to avoid hypothesizing after the results are known (HARKing).
It is desired to avoid data-driven selection of analyses and methods, chance
observations which might lead to incorrect or inflated claims.

All changes to the Statistical Analysis Plan (SAP) should be well-motivated and
well documented which is more likely by separating IDA from the analyses
peformed to answer the research question.

## 6. Documenting and reporting IDA

Visualization is key in IDA supporting (a) information seeking, (b) pattern
identification and (c) pattern recognition during the phases of IDA for ease
of interpretation.

The purpose is to provide an "overview first and details on demand" which
supports the identification of emerging signals, not in alignment with
assumptions about the data that could influence the interpretation of analysis
data.

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
keyh_col = []
null_col = []
#features_col = []  move to EDA
#target_col = []    move to EDA

nominal_col = []
ordinal_col = []
interval_col = []
ratio_col = []
```

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

## 6. SQL DDL

```python
print("CREATE TABLE IF NOT EXISTS vendor_topic_tble (")
for c in df.columns:
    sanitized_c = c.lower().replace(" ", "_").replace("#", "no")
    if df[c].dtype == np.float64:
       print(f"     {sanitized_c}   NUMERIC,")
    elif df[c].dtype == object:
        max_len = df[c].apply(lambda x: len(x)).max()
        print(f"    {sanitized_c}    VARCHAR({max_len}),")
print(");")
```
