########################################################
# Hierarchies of stocks
# See exercise02.md
#
# Preload
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

from preload import stock_movements as movements, stock_companies as companies
########################################################


# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method='complete')

# Plot the dendrogram
dendrogram(mergings, labels=companies, leaf_rotation=90, leaf_font_size=6)
plt.show()
