Initial Data Analysis Report
============================

Should contain sufficient information that enables the research team to
continue with the statistical analysis plan (SAP) in a responsible manner.

1) Summary of the metadata including the:

- study design
- data sources
- data content

2)  Study flow diagram illustrating

- sample size
- inclusion criteria
- exclusion criteria
- subsequent selections made to arrive at the sample size for the analysis

3) Summary of the data cleaning process

Overview of the data quality issues and an overview of the rules used to 
identify and correct errors.

4) Description of the frequency and patterns of missing values

5) Overview of Univariate and multivariate distributions

6) Summary of the findings which may result in an update or refinement of the
   Statistical analysis plan (SAP)

## Intro

50% - 80% of the total time spent performance analysis and a model.

TODO: SOP for standard visualization techinques required for:

- scatter plots
- line plots
- horizontal bar plots
- histograms/kernel density plots (skew, kurtosis)

Data Analysis of Observational Studies to check if the observed data
corresponds to the expectations for the data.  IDA also provides data
ready for analysis including reliable information on the data properties.
IDA ensures transparency and integretiy of the pre-conditions to conduct
statistical analysis to answer pre-defined questions.
Typically IDA is not performed in a systematic manner.  Typically IDA 
is not mixed with:

- hypothesis generation (EDA)
- hypothesis exploration (EDA)
- formal analysis (EDA)
- interpretation of conclusions (EDA)

Target audience for intepretation of conclusions are domain experts.

NOTE: transparency means being faithful to the original research questions
and not pursuing other opportunities in the data instead.

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
