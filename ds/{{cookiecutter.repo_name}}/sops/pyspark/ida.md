# Pyspark Initial Data Analysis

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, regex_replace
from pyspark.sql.types import StructType, StructField, StringType, LongType, BooleanType, ArrayType

spark = (SparkSession
   .builder
   .appName("Initial Data Analysis")
   .getOrCreate()
)

schema = StructType(
   [
      StructField('col', StringType(), True),
      StructField('nested', StructType(
         [
            StructField('nested_col', StringType(), True)
         ]
      ))
   ]
)

df = (spark
   .read
   .format("csv")
   .options(
      header=True,
   )
   .load("../data/foo.csv")
)

df = df.withColumn("json_col", regexp_replace("json_col", "pattern", "sub"))
df = df.withColumn("json_col", from_json("json_col", schema=schema))
df.createOrReplaceTempView("myview")

qry = """
SELECT *
  FROM myview
"""

spark.sql(qry).show(truncate=False)
```
