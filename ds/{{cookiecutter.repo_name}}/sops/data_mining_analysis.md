# Data Mining and Analysis

## Fast Charactderization

- records with null fields
- cardinality of fields
- candidate key identification

## Identify column by statistical type

- dates (with or without timezone)
- start/end times, reconstruct time index
- numeric types

```python
only_ints = df.select_dtypes(include=["int"])
print(only_ints)
```

- categorical types: categories/codes with frequency counts

## Entity Resolution:

- records that can be linked to cannoical sources
- records that cannot be linked to cannonical sources

## Dendrogram

NOTE: consider re-reunning after group assignment to better understand how
the clustering actually works by group membership visually.

```python
from scipy.cluster.hierarchy import dendrogram, linkage

vdf = df.isnull().replace([True, False], [0, 1])
Z = linkage(vdf, "centroid")
dendrogram(Z)
plt.title("Contract Header Dendrograms")
plt.xlabel("cluster size")
```

## KNN Clusters

```python
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
K=3
nbrs = NearestNeighbors(n_neighbors=K, algorithm="ball_tree").fit(vdf)
distances, indicies = nbrs.kneighbors(vdf)
pca = PCA(n_components=2)
pca.fit(indicies)
X_pca = [ x[0] for x in pca.transform(distances)]
Y_pca = [ x[1] for x in pca.transform(distances)]
plt.scatter(indicies[0], indicies[1])
plt.title(f"Cluster Distances\nPCA explained variance ratio: {round(pca.explained_variance_ratio_[0] + pca.explained_variance_ratio_[1], 3)}")


## KMeans Clustering

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=K, n_init="auto", algorithm="lloyd", random_state=42)
y_hat = km.fit_predict(vdf)
df["cluster"] = y_hat
```

## Get Common Columns

```python
def get_mandatory_columns(percent, my_df):
   cdf = my_df.describe().T.reset_index()
   columns = list(cdf[ cdf["count"] >= (my_df.shape[0] * percent) ]["index"])
   cdf = my_df[columns].head(1).T.reset_index()
   value_column = cdf.columns[-1]
   columns = list(cdf[ cdf[value_column] > 0]["index"])
   return columns

# old method
#for i in range(K):
#   print(i, sorted(get_mandatory_columns(0, df[ df["cluster"] == i].drop("cluster", axis=1))))
```

## Build a set of columns

```python
all_columns = set([])
for c in record_types:
   [all_columns.add(r) for r in c]
group_df = pd.DataFrame(vdf, columns=sorted(list(all_columns)))
group_df.T.style.apply(lambda x: ["background: gray" if v == 0 else "" for v in x], axis=1)
```

## Group Membership

```python
df["cluster"].value_counts()
```
