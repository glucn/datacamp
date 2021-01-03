import pandas as pd

df = pd.read_csv('house-votes-84.data',
                 names=['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite',
                        'aid', 'missile', 'immigration', 'synfuels', 'education', 'superfund', 'crime',
                        'duty_free_exports', 'eaa_rsa']
                 )
df = df.replace({'n': 0, 'y': 1, '?': 0})

X_new = pd.DataFrame(
    [[0.696469, 0.286139, 0.226851, 0.551315, 0.719469, 0.423106, 0.980764, 0.68483, 0.480932, 0.392118, 0.343178,
      0.72905, 0.438572, 0.059678, 0.398044, 0.737995]])
