########################################################
# PCA doesn't learn parts
# See exercise06.md
#
# Preload
from preload import led as samples, show_as_image
########################################################

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
