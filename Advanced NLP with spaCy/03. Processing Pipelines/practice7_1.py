# Processing streams
# In this exercise, you'll be using nlp.pipe for more efficient text processing. The nlp object has already been
# created for you. A list of tweets about a popular American fast food chain are available as the variable TEXTS.
#
# Rewrite the example to use nlp.pipe. Instead of iterating over the texts and processing them, iterate over the doc
# objects yielded by nlp.pipe.
#
# for text in TEXTS:
#     doc = nlp(text)
#     print([token.text for token in doc if token.pos_ == 'ADJ'])

import spacy

from preload import TEXTS

nlp = spacy.load('en_core_web_sm')

# Process the texts and print the adjectives
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == 'ADJ'])
