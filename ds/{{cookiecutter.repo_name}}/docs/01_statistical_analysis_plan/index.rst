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
attribute metadtata by fusing data dictionary insight with scale/distribution
and missing data patterns as well as (b) data clean up to create a derived
subset sample with the statistical power required for meaningful study.

Traditional exploratory data analysis is to be used with features classified
into NOIR (nominal, ordinal, interval and ratio) for further visualization and
study.  Regression is used to identify orthogonal features.  Groups are mined,
labeled and explored through pivot tables, group bys and analytics.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
