# Loading models
# Let's start by loading a model. spacy is already imported.

import spacy

# Execute this to download the model
# $ python -m spacy download en_core_web_sm

# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

# Print the document text
print(doc.text)
