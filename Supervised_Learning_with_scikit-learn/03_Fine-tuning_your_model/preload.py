import pandas as pd

diabetes = pd.read_csv('diabetes.csv')

diabetes_X = diabetes.drop('Outcome', axis=1)
diabetes_y = diabetes['Outcome'].values.reshape(-1, 1)
