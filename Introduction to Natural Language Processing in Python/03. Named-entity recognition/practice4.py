# French NER with polyglot I
# In this exercise and the next, you'll use the polyglot library to identify French entities. The library functions
# slightly differently than spacy, so you'll use a few of the new things you learned in the last video to display the
# named entity text and category.
#
# You have access to the full article string in article. Additionally, the Text class of polyglot has been imported
# from polyglot.text.

from polyglot.text import Text

from preload import article_fr

# polyglot require some dependencies, please see:
# https://polyglot.readthedocs.io/en/latest/Installation.html

# Create a new text object using Polyglot's Text class: txt
txt = Text(article_fr)

# Print each of the entities found
for ent in txt.entities:
    print(ent)

# Print the type of ent
print(type(txt.entities[0]))
