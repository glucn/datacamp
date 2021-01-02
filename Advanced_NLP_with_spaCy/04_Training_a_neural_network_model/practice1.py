# Creating training data (1)
# spaCy's rule-based Matcher is a great way to quickly create training data for named entity models. A list of
# sentences is available as the variable TEXTS. You can print it the IPython shell to inspect it. We want to find
# all mentions of different iPhone models, so we can create training data to teach a model to recognize them as
# 'GADGET'.
#
# The nlp object has already been created for you and the Matcher is available as the variable matcher.

import spacy
from spacy.matcher.matcher import Matcher

from preload import TEXTS

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)


# Two tokens whose lowercase forms match 'iphone' and 'x'
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT': True, 'OP': '?'}]

# Add patterns to the matcher
matcher.add('GADGET', None, pattern1, pattern2)


# Creating training data (2)
# Let's use the match patterns we've created in the previous exercise to bootstrap a set of training examples. The
# nlp object has already been created for you and the Matcher with the added patterns pattern1 and pattern2 is
# available as the variable matcher. A list of sentences is available as the variable TEXTS.

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Find the matches in the doc
    matches = matcher(doc)

    # Get a list of (start, end, label) tuples of matches in the text
    entities = [(start, end, 'GADGET') for match_id, start, end in matches]
    print(doc.text, entities)
