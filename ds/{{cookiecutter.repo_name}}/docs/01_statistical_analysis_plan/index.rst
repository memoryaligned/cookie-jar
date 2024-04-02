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
   import pandas as pd
   import matplotlib.pyplot as plt
   import numpy as np
   pd.set_option("display.max_rows", 200)
   plt.style.use("ggplot")

   import os
   DATADIR = "../data/raw"
   INFILE = DATADIR + "/" + "data.csv"

   ## 1. Load Data

   def load_vendor_data(csvfile_path: str) -> pd.DataFrame:
      df = pd.read_csv(
         csvfile_path,
         dtype = schema_<VENDOR>_<DATA>_v1,
         converters = { "col1": convert_currency }
      )
      return df

   df = load_vendor_data(INFILE)

   print("schema_VENDOR_OBJECT_v1 = {")
   for n, t in zip(df.dtypes.index, df.dtypes.values):
      if t == "bool" or t == "object":
         print(f"    '{n}': {t},")
      else:
         print(f"    '{n}': np.{t},")
   print("}")

   ## 2. Attribute Cardinality

   for c in df.columns:
      if df[c].dtype == "object":
         print(df[c].fillna("").value_counts().sort_values(ascending=False)[:5])
      else:
         print(f"{c}: min: {df[c].min()} median: {df[c].median()} max: {df[c].max()}")
      print()

   ## 3. Classify columns into NOIR (For further analysis)

   key_col = []
   null_col = []

   nominal_col = []

   ordinal_col = []
   interval_col = []
   ratio_col = []

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
