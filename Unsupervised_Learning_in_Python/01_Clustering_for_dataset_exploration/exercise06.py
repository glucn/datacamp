########################################################
# Clustering the fish data
# See exercise06.md
#
# Preload
from exercise05 import pipeline
from preload import fish_catch_samples as samples, fish_catch_species as species
########################################################


# Import pandas
import pandas as pd

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels': labels, 'species': species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['species'])

# Display ct
print(ct)
