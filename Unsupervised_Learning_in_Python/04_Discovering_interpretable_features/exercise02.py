########################################################
# NMF features of the Wikipedia articles
# See exercise02.md
#
# Preload
from exercise01 import nmf_features
from preload import wiki_titles as titles
########################################################


# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])
