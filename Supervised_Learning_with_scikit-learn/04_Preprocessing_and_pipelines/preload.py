import pandas as pd

gapminder = pd.read_csv('gapminder.csv')

gapminder_region = pd.get_dummies(gapminder, drop_first=True)

gapminder_X = gapminder_region.drop('life', axis=1).values
gapminder_y = gapminder_region['life'].values.reshape(-1, 1)


house_votes = pd.read_csv('house-votes-84.data',
                          names=['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious',
                                 'satellite', 'aid', 'missile', 'immigration', 'synfuels', 'education', 'superfund',
                                 'crime', 'duty_free_exports', 'eaa_rsa']
                          )
house_votes = house_votes.replace({'n': 0, 'y': 1, '?': 'NaN'})

house_votes_X = house_votes.drop('party', axis=1)
house_votes_y = house_votes['party'].values.reshape(-1, 1).ravel()


wine_quality = pd.read_csv('winequality-white.csv')

wine_quality_X = wine_quality.drop('quality', axis=1).values
wine_quality_y = wine_quality['quality'].values.reshape(-1, 1).ravel()
wine_quality_y_classify = wine_quality_y == 5
