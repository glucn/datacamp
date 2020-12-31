# Building a Counter with bag-of-words
# In this exercise, you'll build your first (in this course) bag-of-words counter using a Wikipedia article, which has
# been pre-loaded as article. Try doing the bag-of-words without looking at the full article text, and guessing what
# the topic is! If you'd like to peek at the title at the end, we've included it as article_title. Note that this
# article text has had very little preprocessing from the raw Wikipedia database entry.
#
# word_tokenize has been imported for you.

from nltk.tokenize import word_tokenize

from preload import article

# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))
