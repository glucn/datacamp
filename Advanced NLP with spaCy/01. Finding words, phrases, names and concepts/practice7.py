# Using the Matcher
# Let's try spaCy's rule-based Matcher. You'll be using the example from the previous exercise and write a pattern
# that can match the phrase "iPhone X" in the text. The nlp object and a processed doc are already available.

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("New iPhone X release date leaked as Apple reveals pre-orders by mistake")

# Import the Matcher
from spacy.matcher import Matcher

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# Add the pattern to the matcher
matcher.add('IPHONE_X_PATTERN', None, pattern)

# Use the matcher on the doc
matches = matcher(doc)
print('Matches:', [doc[start:end].text for match_id, start, end in matches])
