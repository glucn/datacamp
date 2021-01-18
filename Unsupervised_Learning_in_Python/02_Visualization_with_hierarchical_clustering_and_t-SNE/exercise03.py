########################################################
# Different linkage, different hierarchical clustering!
# See exercise03.md
#
# Preload
from preload import eurovision_samples as samples, eurovision_country_names as country_names
########################################################


# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
plt.show()
