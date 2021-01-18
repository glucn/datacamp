import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler

seeds = pd.read_csv('../data/seeds_dataset.txt', delim_whitespace=True, header=None)
seeds_samples = seeds.iloc[:, :-1]
seeds_samples_size = seeds.iloc[:, 3:5].to_numpy()
seeds_varieties = seeds.iloc[:, -1].replace({1: 'Kama wheat', 2: 'Rosa wheat', 3: 'Canadian wheat'}).tolist()

fish_catch = pd.read_csv('../data/fishcatch.dat.txt', delim_whitespace=True, header=None).iloc[:, :-1].dropna()
fish_catch_samples = fish_catch.iloc[:, 2:]
scaler = StandardScaler()
fish_catch_samples_scaled = scaler.fit_transform(fish_catch_samples)

# TODO: get the data for this
wiki_articles = csr_matrix((60, 13125), dtype=np.float64)
wiki_titles = ['HTTP 404',
               'Alexa Internet',
               'Internet Explorer',
               'HTTP cookie',
               'Google Search',
               'Tumblr',
               'Hypertext Transfer Protocol',
               'Social search',
               'Firefox',
               'LinkedIn',
               'Global warming',
               'Nationally Appropriate Mitigation Action',
               'Nigel Lawson',
               'Connie Hedegaard',
               'Climate change',
               'Kyoto Protocol',
               '350.org',
               'Greenhouse gas emissions by the United States',
               '2010 United Nations Climate Change Conference',
               '2007 United Nations Climate Change Conference',
               'Angelina Jolie',
               'Michael Fassbender',
               'Denzel Washington',
               'Catherine Zeta-Jones',
               'Jessica Biel',
               'Russell Crowe',
               'Mila Kunis',
               'Dakota Fanning',
               'Anne Hathaway',
               'Jennifer Aniston',
               'France national football team',
               'Cristiano Ronaldo',
               'Arsenal F.C.',
               'Radamel Falcao',
               'Zlatan Ibrahimović',
               'Colombia national football team',
               '2014 FIFA World Cup qualification',
               'Football',
               'Neymar',
               'Franck Ribéry',
               'Tonsillitis',
               'Hepatitis B',
               'Doxycycline',
               'Leukemia',
               'Gout',
               'Hepatitis C',
               'Prednisone',
               'Fever',
               'Gabapentin',
               'Lymphoma',
               'Chad Kroeger',
               'Nate Ruess',
               'The Wanted',
               'Stevie Nicks',
               'Arctic Monkeys',
               'Black Sabbath',
               'Skrillex',
               'Red Hot Chili Peppers',
               'Sepsis',
               'Adam Levine']
