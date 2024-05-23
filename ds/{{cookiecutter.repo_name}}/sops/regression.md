# Regression SOP

## (OLS) Multi-linear Regression

```python
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("../my.csv")

y = df["TARGET"]
x1 = df[["col1", "col2"]]

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
results.summary()
```

NOTE: the R-Squared vs Adj. R-Squared and watch for p-values less than 0.05
(significant for the model).

Adding independent variables "increases explanatory power of the model"
