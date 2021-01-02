# Setting extension attributes (1)
# Let's practice setting some extension attributes. The nlp object has already been created for you and the Doc,
# Token and Span classes are already imported.
#
# Remember that if you run your code more than once, you might see an error message that the extension already exists.
# That's because DataCamp will re-run your code in the same session. To solve this, you can set force=True on
# set_extension, or reload to start a new Python session. None of this will affect the answer you submit.

import spacy
from spacy.tokens import Token

nlp = spacy.load('en_core_web_sm')


# Register the Token extension attribute 'is_country' with the default value False
Token.set_extension('is_country', default=False)

# Process the text and set the is_country attribute to True for the token "Spain"
doc = nlp("I live in Spain.")
doc[3]._.is_country = True

# Print the token text and the is_country attribute for all tokens
print([(token.text, token._.is_country) for token in doc])
