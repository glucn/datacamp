# Rewrite the example to use nlp.pipe. Don't forget to call list() around the result to turn it into a list.
#
# docs = [nlp(text) for text in TEXTS]
# entities = [doc.ents for doc in docs]
# print(*entities)

import spacy

from preload import TEXTS

nlp = spacy.load('en_core_web_sm')

# Process the texts and print the entities
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)
