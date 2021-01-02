# Complex components
# In this exercise, you'll be writing a custom component that uses the PhraseMatcher to find animal names in the
# document and adds the matched spans to the doc.ents.
#
# A PhraseMatcher with the animal patterns has already been created as the variable matcher. The small English model
# is available as the variable nlp. The Span object has already been imported for you.

import spacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(['cat', 'Golden Retriever']))  # This is a shortened list
matcher.add('ANIMAL', None, *patterns)


# Define the custom component
def animal_component(doc):
    # Apply the matcher to the doc
    matches = matcher(doc)
    # Create a Span for each match and assign the label 'ANIMAL'
    spans = [Span(doc, start, end, label='ANIMAL')
             for match_id, start, end in matches]
    # Overwrite the doc.ents with the matched spans
    doc.ents = spans
    return doc


# Add the component to the pipeline after the 'ner' component
nlp.add_pipe(animal_component, after='ner')
print(nlp.pipe_names)

# Process the text and print the text and label for the doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
