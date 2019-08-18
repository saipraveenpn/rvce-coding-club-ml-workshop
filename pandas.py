import pandas as pd
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, 3]
