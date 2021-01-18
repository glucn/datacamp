from collections import Counter

import nltk
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler

seeds = pd.read_csv('../data/seeds_dataset.txt', delim_whitespace=True, header=None)
seeds_samples = seeds.iloc[:, :-1]
seeds_samples_size = seeds.iloc[:, 3:5].to_numpy()
seeds_varieties = seeds.iloc[:, -1].replace({1: 'Kama wheat', 2: 'Rosa wheat', 3: 'Canadian wheat'}).tolist()

fish_catch = pd.read_csv('../data/fishcatch.dat.txt', delim_whitespace=True, header=None).iloc[:, :-1].dropna()
fish_catch_samples = fish_catch.iloc[:, 2:]
scaler = StandardScaler()
fish_catch_samples_scaled = scaler.fit_transform(fish_catch_samples)

wiki = pd.read_csv('../data/wiki.csv')
wiki_titles = wiki.iloc[:, 0].to_list()
# TODO: improve the sparse matrix, the one on datacamp is 60x13125
vectorizer = DictVectorizer()
wiki_articles = vectorizer.fit_transform([Counter(nltk.tokenize.word_tokenize(article)) for article in wiki['article']])
