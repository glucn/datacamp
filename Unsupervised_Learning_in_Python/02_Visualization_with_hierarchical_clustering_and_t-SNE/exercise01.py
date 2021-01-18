########################################################
# Hierarchical clustering of the grain data
# See exercise01.md
#
# Preload
from preload import seeds_samples as samples, seeds_varieties as varieties
########################################################


# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Calculate the linkage: mergings
mergings = linkage(samples, method='complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
           )
plt.show()
