.. {{cookiecutter.repo_name}} documentation master file, created by
   sphinx-quickstart on Mon Apr  1 16:43:27 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Statistical Analysis Plan
=========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Title and Abstract
##################
Evaluate the data integration suitability for <DATASET NAME> from 
<METHOD WAS OBTAINED>.  To evaluate suitability the following will be peformed:

- Statistical initial data analysis (IDA)
- Statistical exploratory data analysis (EDA)
- Data mining for sub-groups with machine learning
- SQL Schema Design (PostgreSQL Integration)
- Opportunities to enrich data via joins will be identified.

Background
**********
This study of <DATASET NAME> is to assess the value of the data for
further investment in (a) analytics, (b) key process indicators and (c) general
business intelligence reporting.

Objectives
**********
- Pandas Schema for repeatable data loads
- Repeatable data cleaning method
- Produce a recommended SQL Schema
- Candidate primary key(s)
- Candidate foreign keys
- Univeriate analysis
- Bivariate analysis
- Business object lifecycle "begin" and "end"
- Data mining to discover potential sub-groups
- Row classification by potential sub-group
- Comparison of column membership by potential sub-group

Methods
*******
Traditional statistical initial data analysis is to be sued to (a) generate
attribute metadata by fusing data dictionary insight with scale/distribution
and missing data patterns as well as (b) data clean up to create a derived
subset sample with the statistical power required for meaningful study.

Traditional exploratory data analysis is to be used with features classified
into NOIR (nominal, ordinal, interval and ratio) for further visualization and
study.  Regression is used to identify orthogonal features.  Groups are mined,
labeled and explored through pivot tables, group bys and analytics.

Jupyter Lab Template
********************

.. code-block::

   # <VENDOR> <DATA> Initial Data Analysis
   import re
   import pandas as pd
   import matplotlib.pyplot as plt
   import numpy as np
   pd.set_option("display.max_rows", 200)
   plt.style.use("ggplot")

   ## Helper functions
   def date_summary(df: pd.DataFrame) -> pd.DataFrame:
      return pd.DataFrame({
         "min":    df.select_dtypes(include=np.datetime64).min(),
         "median": df.select_dtypes(include=np.datetime64).median(),
         "max":    df.select_dtypes(include=np.datetime64).max(),
      })

   re_underscores = re.compile("_+")
   def sanitize_columns(colname: str) -> str:
      s = (
         colname.lower()
         .replace(" ", "_")
         .replace("#", "no")
         .replace(".", "_")
         .replace("%", "pct")
         .replace("/", "")
      )
      return re_underscores.sub("_", s)

   def print_pandas_schema(df: pd.DataFrame, name: str) -> None:
      print("schema_" + name + "_v1 = {")
      for n, t in zip(df.dtypes.index, df.dtypes.values):
         if t == "bool" or t == "object":
            print(f"    '{n}': {t},")
         else:
            print(f"    '{n}': np.{t},")
      print("}")

   def print_sql_schema(df: pd.DataFrame, name: str) -> None:
      print(f"CREATE TABLE IF NOT EXISTS {name}_tbl (")
      for c in df.columns:
         sanitized_c = sanitize_columns(c)
         if df[c].dtype == np.float64:
            print(f"    {sanitized_c}   NUMERIC,")
         else:
            max_len = df[c].apply(lambda x: len(str(x)))
            print(f"    {sanitized_c}   VARCHAR({max_len}),")
      print(");")

   def attribute_cardinality(df: pd.DataFrame) -> None:
      for c in df.columns:
         if df[c].dtype == "object":
            print(df[c].fillna("").value_counts().sort_values(ascending=False)[:5])
         else:
            print(f"{c}: min: {df[c].min()} median: {df[c].median()} max: {df[c].max()}")
         print(f"null count: {df[c].isna().sum()} out of {df[c].shape[0]}")
         print()
         print()

   def hbar_category(df: pd.DataFrame, category: str, save_path:str) -> None:
      plt.clf()
      fig = plt.gcf()
      fig.set_size_inches(8,4)
      make_df = df[category].value_counts().sort_values().reset_index()[:20]
      plt.barh(make_df[category], make_df["count"])
      plt.title(f"attribute: {category}\nTop 20")
      plt.savefig(save_path)

   def visualize_hbar(df: pd.DataFrame, dirpath: str) -> None:
      for c in df.columns:
         sanitize_c = sanitize_columns(c)
         try:
            hbar_category(df, c, dirpath + f"/{sanitize_c}_hbar.png")
         except:
            pass

   import os
   DATADIR = "../data/raw"
   INFILE = DATADIR + "/" + "data.csv"


   ## 1. Load Data

   date_cols = []

   def load_vendor_data(csvfile_path: str, schema, date_cols) -> pd.DataFrame:
      df = pd.read_csv(
         csvfile_path,
         dtype = schema,
         parse_dates = date_cols,
         converters = { "col1": convert_currency }
      )
      df.columns = [sanitize_column(c) for c in df.columns]
      return df.drop_duplicates()

   df = load_vendor_data(INFILE)

   ### generate schema
   print_pandas_schema(df, "VENDOR_DATA")

   ## 2. Attribute Cardinality

   null_cols = []
   print(f"Columns: {df.shape[1]}, Columns with data {df.drop(null_cols, axis=1).shape[1]}")
   attribute_cardinality(df.drop(null_cols, axis=1))

   ### Visualize data
   visualize_hbar(df, "../reports/figures")

   ## 3. Classify columns into NOIR (For further analysis)

   key_col = []

   nominal_col = []
   ordinal_col = []
   interval_col = []
   ratio_col = []

   ## 4. Generate SQL DDL

   print_sql_schema(df, "VENDOR_DATA")


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
