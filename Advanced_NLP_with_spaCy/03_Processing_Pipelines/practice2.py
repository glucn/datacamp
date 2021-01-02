# Simple components
# The example shows a custom component that prints the character length of a document. Can you complete it? spacy has
# already been imported for you.

import spacy


# Define the custom component
def length_component(doc):
    # Get the doc's length
    doc_length = len(doc)
    print("This document is {} tokens long.".format(doc_length))
    # Return the doc
    return doc


# Load the small English model
nlp = spacy.load('en_core_web_sm')

# Add the component first in the pipeline and print the pipe names
nlp.add_pipe(length_component, first=True)
print(nlp.pipe_names)

# Process a text
doc = nlp('This is a sentence.')
