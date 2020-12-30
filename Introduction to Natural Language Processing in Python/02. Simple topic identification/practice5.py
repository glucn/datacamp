# Tf-idf with Wikipedia
# Now it's your turn to determine new significant terms for your corpus by applying gensim's tf-idf. You will again
# have access to the same corpus and dictionary objects you created in the previous exercises - dictionary, corpus, and
# doc. Will tf-idf make for more interesting results on the document level?
#
# TfidfModel has been imported for you from gensim.models.tfidfmodel.

from gensim.models.tfidfmodel import TfidfModel
from practice3 import corpus, dictionary
from practice4 import doc

# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)