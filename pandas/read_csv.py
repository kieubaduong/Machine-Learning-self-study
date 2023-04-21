import pandas as pd

data = pd.read_csv('dataset/UNSW_NB15_training-set.csv', header=None)

data.loc[3].to_csv('test.csv')