Introduction
************

Sample data from the <VENDOR> <DATA> containing <FILL IN>.
*(Source: XXXXXXXX)*

NOTE: location where the data was obtained
NOTE: when data was obtained

The <VENDOR> <DATA> data includs:
 - XX,XXX unqique records total
 - XX columns, XX containing data

.. list-table:: <VENDOR> <DATA> Dates
   :widths: 30 10 10 10
   :header-rows: 1

   * - Attribute
     - min
     - median
     - max
   * - col1
     - 2024-01-01
     - 0
     - 0

.. list-table:: <VENDOR> <DATA> Keys
   :widths: 30 10 10 15
   :header-rows: 1

    * - Primary Key, Foreign Key or Lookup Code
      - primary
      - foriegn
      - null count
      - unique count
      - definition?
    * - id
      - yes
      -
      - 0
      - 0
      - N/A
    * - fk
      -
      - yes
      - UNKNOWN
      - 0
      - 0

Include helpful figures to show the distribution of key data attributes and
note the nature of the subset of data including:


Data Cleaning
*************

 The data loading procedure is:

  - apply the schema (to prevent type autodetection anomalies)
  - column names are sanitized:
     - converted to lower case
     - replace space with "_"
     - replace "#" with "no"
     - replace "%" with "pct"
     - replace "." with "_"
     - remove "/"
  - drop duplicate records
