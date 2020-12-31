# NER with NLTK
# You're now going to have some fun with named-entity recognition! A scraped news article has been pre-loaded into
# your workspace. Your task is to use nltk to find the named entities in this article.
#
# What might the article be about, given the names you found?
#
# Along with nltk, sent_tokenize and word_tokenize from nltk.tokenize have been pre-imported.

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

from preload import article

# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')


# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]

# Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)
