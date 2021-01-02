# Rewrite the example to use nlp.pipe. Don't forget to call list() around the result to turn it into a list.
#
# patterns = list(nlp.pipe(people))

import spacy

nlp = spacy.load('en_core_web_sm')

people = ['David Bowie', 'Angela Merkel', 'Lady Gaga']

# Create a list of patterns for the PhraseMatcher
patterns = list(nlp.pipe(people))
