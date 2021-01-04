import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 'gapminder.csv' is a shortened file
df = pd.read_csv('gapminder.csv')
y = df['life'].values.reshape(-1, 1)
X_fertility = df['fertility'].values.reshape(-1, 1)
X = df.drop('life', axis=1).values
df_columns = df.drop('life', axis=1).columns

alpha_space = np.logspace(-4, 0, 50)


# Copied from `exercise8.md`
def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()
