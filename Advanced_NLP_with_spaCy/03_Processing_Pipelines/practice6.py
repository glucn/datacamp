# Components with extensions
# Extension attributes are especially powerful if they're combined with custom pipeline components. In this exercise,
# you'll write a pipeline component that finds country names and a custom extension attribute that returns a country's
# capital, if available.
#
# The nlp object has already been created and the Span class is already imported. A phrase matcher with all countries
# is available as the variable matcher. A dictionary of countries mapped to their capital cities is available as the
# variable capitals.

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

from preload import COUNTRIES, CAPITALS

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add('GPE', None, *patterns)


def countries_component(doc):
    # Create an entity Span with the label 'GPE' for all matches
    doc.ents = [Span(doc, start, end, label='GPE')
                for match_id, start, end in matcher(doc)]
    return doc


# Add the component to the pipeline
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# Getter that looks up the span text in the dictionary of country capitals
get_capital = lambda span: CAPITALS.get(span.text)

# Register the Span extension attribute 'capital' with the getter get_capital
Span.set_extension('capital', getter=get_capital)

# Process the text and print the entity text, label and capital attributes
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
