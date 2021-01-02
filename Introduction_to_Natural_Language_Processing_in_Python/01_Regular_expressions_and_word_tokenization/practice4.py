# Regex with NLTK tokenization
# Twitter is a frequently used source for NLP text and tasks. In this exercise, you'll build a more complex tokenizer
# for tweets with hashtags and mentions using nltk and regex. The nltk.tokenize.TweetTokenizer class gives you some
# extra methods and attributes for parsing tweets.
#
# Here, you're given some example tweets to parse using both TweetTokenizer and regexp_tokenize from the nltk.tokenize
# module. These example tweets have been pre-loaded into the variable tweets. Feel free to explore it in the
# IPython Shell!
#
# Unlike the syntax for the regex library, with nltk_tokenize() you pass the pattern as the second argument.

from preload import tweets

# Import the necessary modules
from nltk.tokenize import regexp_tokenize, TweetTokenizer

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)

# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
