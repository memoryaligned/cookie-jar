# XGBoost

```python
from xgboost import XGBClassifier

bst = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective="binary:logistic")
bst.fit(X_train, y_train)
preds = bst.predict(X_test)

# create features (to save to file)
#  TODO: create a skeleton implementation where I can use standard/customer
#  transformers.
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, RobustScaler

# NOTE update with split percentage
X_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)

# NOTE: if you have outliers use RobustScaler or PCA(whiten=True) to further
# remove linaer correlation across features
pipe = make_pipeline(StandardScaler())
pipe.fit(X_train, y_train)
```

NOTE: PCA will find a lower-dimensional subspace onto which to project our
data.  We can look at a 2d graph and understand u1 (principle direction of
the variation in the data) and u2 (secondary direction of variation in the
data).

TODO: SOP to draw arrows and text in matplotlib on a graph for the
principle variance eigenvector and secondary variance eigenvector.
