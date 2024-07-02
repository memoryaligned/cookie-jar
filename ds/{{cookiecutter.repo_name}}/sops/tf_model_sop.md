# Tensorflow Modeling SOP

## Feature engineering

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.plt as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data.csv")

# look for correlation/relationships
sns.pairplot(df)

# look at pearson correlation coefficient
df.corr()["target"].sort_values(ascending=False).plot(kind="barh")

# look a the data distribution for a feature
plt.figure(figsize(10,6))
sns.boxplot(data=df, x="independent", y="price")

X = df[["feature1", "feature2"]].values
y = df["price"].values

X_train, X_test, y_train, y_test = train_test_split(
   X,
   y,
   test_size=0.3,
   random_state=42
)

scaler = MinMaxScaler()
scaler.fit(X)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

## Binary Classification 

- sigmoid and binary_crossentropy

```python
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# wait 25 epochs after we detected the minimum value loss
early_stop = EarlyStopping(
   monitor="val_loss", 
   mode="min", 
   verbose=1, 
   patience=25
)

model.add(Dense(30, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(15, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(
   loss="binary_crossentropy", 
   optimizer="adam",
   metrics=["accuracy"],
)

model.fit(
   x=X_train,
   y=y_train,
   epochs=600,
   validation_data=(X_test, y_test),
   callbacks=[early_stop],
   verbose=0,
)

pd.DataFrame(model.history.history).plot()

# sigmoid: binary classification evaluation
predictions = (model.predict(X_test) > 0.5).astype("int32")
```

## Multiclass Classification 

- softmax and categorical_crossentropy

```python
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix

# wait 25 epochs after we detected the minimum value loss
early_stop = EarlyStopping(
   monitor="val_loss", 
   mode="min", 
   verbose=1, 
   patience=25
)

model.add(Dense(30, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(15, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(
   loss="categorical_crossentropy", 
   optimizer="adam",
   metrics=["accuracy"]
)

model.fit(
   x=X_train,
   y=y_train,
   epochs=600,
   validation_data=(X_test, y_test),
   callbacks=[early_stop],
   verbose=0,
)

pd.DataFrame(model.history.history).plot()

# softmax: binary classification evaluation
predictions = np.argmax(model.predict(X_test), axis=1)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
```

## Regression

- mean_absolute_error, explained_variance_score

```python
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score

# wait 25 epochs after we detected the minimum value loss
early_stop = EarlyStopping(
   monitor="val_loss", 
   mode="min", 
   verbose=1, 
   patience=25
)

model.add(Dense(30, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(15, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1))

model.compile(
   loss="mse", 
   optimizer="adam",
   metrics=["accuracy"]
)

model.fit(
   x=X_train,
   y=y_train,
   epochs=600,
   validation_data=(X_test, y_test),
   callbacks=[early_stop],
   verbose=0,
)

pd.DataFrame(model.history.history).plot()

# softmax: binary classification evaluation
predictions = model.predict(X_test)

print(mean_squared_error(y_test, predictions))
print(mean_absolute_error(y_test, predictions))

# like R squared
print(explained_variance_score(y_test, predictions))
```
