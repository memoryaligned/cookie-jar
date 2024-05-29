# Pyspark

## Show details

```python
df.show(n=5, truncate=False, vertical=True)
```

## Schema

```python
from pyspark.sql.types import StructType, StructField, StringType, LongType, BooleanType, ArrayType

schema = StructType(
   [
      StructField("col1", StringType(), True),
      StructField("col2", StructType(
         [
            StructField("nested1", BooleanType(), True)
         ]
      )
   ]
)
```

## Create a table

```python
df.createOrReplaceTempView("people")

sdf = spark.sql("SELECT * FROM people")
sdf.show()
```
