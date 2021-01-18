########################################################
# Clustering Wikipedia part II
# See exercise08.md
#
# Preload
from exercise07 import pipeline
from preload import wiki_articles as articles, wiki_titles as titles
########################################################


# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))
