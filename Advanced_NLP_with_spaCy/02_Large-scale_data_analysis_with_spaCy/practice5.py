# Inspecting word vectors
# In this exercise, you'll use a larger English model, which includes around 20.000 word vectors. Because vectors
# take a little longer to load, we're using a slightly compressed version of it than the one you can download with
# spaCy. The model is already pre-installed, and spacy has already been imported for you.

import spacy

# Execute this to install the model
# $ python -m spacy download en_core_web_md

# Load the en_core_web_md model
nlp = spacy.load('en_core_web_md')

# Process a text
doc = nlp("Two bananas in pyjamas")

# Get the vector for the token "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)
