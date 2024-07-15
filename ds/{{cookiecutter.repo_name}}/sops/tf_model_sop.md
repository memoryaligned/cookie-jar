# Tensorflow Modeling SOP

Install w/CUDA support:

```bash
pip install -U tensorflow[and-cuda]
```

NOTE: for deployment we want to train on everything.  It would be helpful to
create the model in a function so it would be easy to re-create the model
for training purposes.  The function creates, compiles and returns the model.

## Saving/Loading the Model

The Keras model consists of the following components (v3 format):

- the architecture (or configuration) of layers and how they are connected
- the set of weights values ("state" of the model)
- an optimizer (defined by compiling the model)
- a set of losses and metrics (defined by compiling the model)

```python

# display the model's architecture
print(model.summmary())

model.save("final_model.keras")
```

Loading the model:

```python
model = keras.modes.load_model("path/final_mode.keras")
```

## Checkpoints

Load the weights from the checkpoint this way:

```python
model = create_model()
model.load_weights(checkpoint_path)
loss, accuracy = model.evaluate(test_images, test_labels, verbose=2)
print("Untrained model, accuracy; {:5.2f}%".format(100 * accuracy))
```

Save the weights as we train this way:

```python
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# callback to save the model's weights (works with models w/same architecture)
cp_callback = tf.keras.callbacks.ModelCheckpoint(
      filepath=checkpoint_path,
      save_weights_only=True,
      verbose=1,
   )

model.fit(
      train_images,
      train_labels,
      epochs=10,
      validation_data=(test_images, test_labels),
      callbacks=[cp_callback],
   )
```

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
print(classification_report(np.argmax(y_test, axis=1), predictions))
print(confusion_matrix(np.argmax(y_test, axis=1), predictions))
print(model.evaluate(x_test, y_test, verbose=0))
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

# get metrics on loss and accuracy
metrics = pd.DataFrame(model.history.history)
metrics[["loss", "val_loss"]].plot()
metrics[["accuracy", "val_accuracy"]].plot()

# get final loss and accuracy
loss, accuracy = model.evaluate(scaled_X_test, y_test, verbose=0)
print("Untrained model, accuracy: {:5.2f}%".format(100 * accuracy))

print(mean_squared_error(y_test, predictions))
print(mean_absolute_error(y_test, predictions))

# like R squared
print(explained_variance_score(y_test, predictions))
```
