########################################################
# NMF learns topics of documents
# See exercise03.md
#
# Preload
from exercise01 import model
from preload import wiki_words as words
########################################################


# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
