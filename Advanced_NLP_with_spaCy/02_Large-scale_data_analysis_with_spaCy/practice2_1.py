# Creating a Doc
# Let's create some Doc objects from scratch! The nlp object has already been created for you.
#
# By the way, if you haven't downloaded it already, check out the spaCy Cheat Sheet. It includes an overview of the
# most important concepts and methods and might come in handy if you ever need a quick refresher!

import spacy

nlp = spacy.load('en_core_web_sm')

# Import the Doc class
from spacy.tokens import Doc

# Desired text: "spaCy is cool!"
words = ['spaCy', 'is', 'cool', '!']
spaces = [True, True, False, False]

# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
