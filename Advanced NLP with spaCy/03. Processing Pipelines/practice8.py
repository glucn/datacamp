# Processing data with context
# In this exercise, you'll be using custom attributes to add author and book meta information to quotes.
#
# A list of (text, context) examples is available as the variable DATA. The texts are quotes from famous books, and
# the contexts dictionaries with the keys 'author' and 'book'. The nlp object has already been created for you.

import spacy

from preload import DATA

nlp = spacy.load('en_core_web_sm')


# Import the Doc class
from spacy.tokens import Doc

# Register the Doc extension 'author' (default None)
Doc.set_extension('author', default=None)

# Register the Doc extension 'book' (default None)
Doc.set_extension('book', default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = context['book']
    doc._.author = context['author']

    # Print the text and custom attribute data
    print(doc.text, '\n', "— '{}' by {}".format(doc._.book, doc._.author), '\n')
