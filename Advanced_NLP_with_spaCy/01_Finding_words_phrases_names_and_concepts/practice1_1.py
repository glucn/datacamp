# Getting Started
# Let's get started and try out spaCy! In this exercise, you'll be able to try out some of the 45+ available languages.
#
# This course introduces a lot of new concepts, so if you ever need a quick refresher, download the spaCy Cheat Sheet
# and keep it handy!

# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)
