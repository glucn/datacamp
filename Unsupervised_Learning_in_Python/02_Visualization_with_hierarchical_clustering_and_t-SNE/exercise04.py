########################################################
# Extracting the cluster labels
# See exercise04.md
#
# Preload
from preload import seeds_mergings as mergings, seeds_varieties as varieties
########################################################


# Perform the necessary imports
import pandas as pd
from scipy.cluster.hierarchy import fcluster

# Use fcluster to extract labels: labels
labels = fcluster(mergings, t=8, criterion='distance')  # As the data is different, use distance 8 instead of 6

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)
