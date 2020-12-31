# Inspecting the vectors
# To get a better idea of how the vectors work, you'll investigate them by converting them into pandas DataFrames.
#
# Here, you'll use the same data structures you created in the previous two exercises (count_train, count_vectorizer,
# tfidf_train, tfidf_vectorizer) as well as pandas, which is imported as pd.

import pandas as pd

from practice1 import count_train, count_vectorizer
from practice2 import tfidf_train, tfidf_vectorizer

# Create the CountVectorizer DataFrame: count_df
count_df = pd.DataFrame(count_train.A, columns=count_vectorizer.get_feature_names())

# Create the TfidfVectorizer DataFrame: tfidf_df
tfidf_df = pd.DataFrame(tfidf_train.A, columns=tfidf_vectorizer.get_feature_names())

# Print the head of count_df
print(count_df.head())

# Print the head of tfidf_df
print(tfidf_df.head())

# Calculate the difference in columns: difference
difference = set(count_df.columns) - set(tfidf_df.columns)
print(difference)

# Check whether the DataFrames are equal
print(count_df.equals(tfidf_df))
