# French NER with polyglot II
# Here, you'll complete the work you began in the previous exercise.
#
# Your task is to use a list comprehension to create a list of tuples, in which the first element is the entity tag,
# and the second element is the full string of the entity text.

from practice4 import txt

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print entities
print(entities)
