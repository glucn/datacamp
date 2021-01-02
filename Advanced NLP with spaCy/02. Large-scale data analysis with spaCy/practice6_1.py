# Comparing similarities
# In this exercise, you'll be using spaCy's similarity methods to compare Doc, Token and Span objects and get
# similarity scores. The medium English model is already available as the nlp object.

import spacy

nlp = spacy.load('en_core_web_md')
doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)
