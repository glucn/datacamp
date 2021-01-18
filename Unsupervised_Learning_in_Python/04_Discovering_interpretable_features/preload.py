from collections import Counter

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import scipy.sparse
from sklearn.feature_extraction import DictVectorizer

wiki = pd.read_csv('../data/wiki.csv')
wiki_titles = wiki.iloc[:, 0].to_list()
# TODO: improve the sparse matrix, the one on datacamp is 60x13125
vectorizer = DictVectorizer()
wiki_articles = vectorizer.fit_transform([Counter(nltk.tokenize.word_tokenize(article)) for article in wiki['article']])
wiki_words = list(vectorizer.vocabulary_.keys())

led = pd.read_csv('../data/led.csv', header=None).to_numpy()

artists = pd.read_csv('../data/artists.csv', header=None)
artists_data = scipy.sparse.csr_matrix(artists.iloc[:, 1:].values)
artist_names = artists.iloc[:, 0].to_list()


def show_as_image(sample):
    bitmap = sample.reshape((13, 8))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()
