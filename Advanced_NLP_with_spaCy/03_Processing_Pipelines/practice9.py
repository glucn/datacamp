# Selective processing
# In this exercise, you'll use the nlp.make_doc and nlp.disable_pipes methods to only run selected components when
# processing a text. The small English model is already loaded in as the nlp object.

import spacy

nlp = spacy.load('en_core_web_sm')

text = "Chick-fil-A is an American fast food restaurant chain headquartered in the city of College Park, Georgia, specializing in chicken sandwiches."

# Only tokenize the text
doc = nlp.make_doc(text)

print([token.text for token in doc])

# Disable the tagger and parser
with nlp.disable_pipes('tagger', 'parser'):
    # Process the text
    doc = nlp(text)
    # Print the entities in the doc
    print(doc.ents)
