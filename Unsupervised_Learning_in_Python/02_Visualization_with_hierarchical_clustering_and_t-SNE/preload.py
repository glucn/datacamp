import pandas as pd
from scipy.cluster.hierarchy import linkage
from sklearn.preprocessing import normalize

seeds = pd.read_csv('../data/seeds_dataset.txt', delim_whitespace=True, header=None)
seeds_samples = seeds.iloc[:, :-1]
seeds_varieties = seeds.iloc[:, -1].replace({1: 'Kama wheat', 2: 'Rosa wheat', 3: 'Canadian wheat'}).tolist()
seeds_variety_numbers = seeds.iloc[:, -1].tolist()
seeds_mergings = linkage(seeds_samples, method='complete')


stock = pd.read_csv('../data/stock_movements.csv', header=None)
stock_movements = stock.iloc[:, 1:].to_numpy()
stock_normalized_movements = normalize(stock_movements)
stock_companies = stock.iloc[:, 0].to_list()

eurovision = pd.read_csv('../data/eurovision.csv', header=None)
eurovision_samples = eurovision.iloc[:, 1:].to_numpy()
eurovision_country_names = eurovision.iloc[:, 0].to_list()
