# Predicting named entities in context
# Models are statistical and not always right. Whether their predictions are correct depends on the training data and
# the text you're processing. Let's take a look at an example. The small English model is available as the variable nlp.

import spacy

nlp = spacy.load('en_core_web_sm')

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# Process the text
doc = nlp(text)

# Iterate over the entities
for ent in doc.ents:
    # print the entity text and label
    print(ent.text, ent.label_)

# Get the span for "iPhone X"
iphone_x = doc[1:3]

# Print the span text
print('Missing entity:', iphone_x.text)
