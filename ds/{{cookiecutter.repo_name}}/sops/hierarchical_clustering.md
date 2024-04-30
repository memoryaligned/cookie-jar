# Hierarchical Clustering

## Agglomerative Clustering

## HDBSCAN

Hierarchical Density-Based Spatial Clustering of Applications with Noise.
This is a hierarchical version of DBSCAN which allows for dense
micro-clusters to be found without having to explicitly specify the number of
clusters.

Because it is density-based it can detect outliers in the data.

```python
from hdbscan imnport HDBSCAN

# We instantiate the model
hdbscan_model = HDBSCAN(min_cluster_size=15, metric="euclidean", cluster_selection_method="eom")

# We fit our model and extract the cluster labels
hdbscan_model.fit(reduce_embeddings)
labels = hdbscam_model.labels_

# Visualize how it has clustered our data
import seaborn as sns

# Reduce 384-dimensional embeddings to 2 dimensions for visualization
reduced_embeddings = UMAP(
   n_neighbors=15,
   n_components=2,
   min_dist=0.0,
   metric="cosine",
).fit_transform(embeddings)

df = pd.DataFrame(
    np.hstack([reduced_embeddings, clusters.reshape(-1, 1)]),
    columns=["x", "y", "cluster"]).sort_values("cluster")

# Visualize clusters
df.cluster = df.cluster.astype(int).astype(str)

sns.scatterplot(data=df, x="x", y="y", hue="cluster", linewidth=0, legend=False, s=3, alpha=0.3)

## To inspect manually
for index in np.where(labels==1)[0][:3]:
   print(abstracts[index])
```
