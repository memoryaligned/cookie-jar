# Unstack

Set the columns you don't want pivoted as the index then call unstack on the
numerical column

```python
df.set_index(["c1", "c2"]).unstack(-1)
```
