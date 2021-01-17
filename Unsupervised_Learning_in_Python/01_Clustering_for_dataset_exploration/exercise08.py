########################################################
# Which stocks move together?
# See exercise08.md
#
# Preload
from exercise07 import pipeline
from preload import stock_movements as movements, stock_companies as companies
########################################################


# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))
