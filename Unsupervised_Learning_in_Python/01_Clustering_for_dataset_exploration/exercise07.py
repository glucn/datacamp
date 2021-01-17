########################################################
# Clustering stocks using KMeans
# See exercise07.md
#
# Preload
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

from preload import stock_movements as movements
########################################################


# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)
