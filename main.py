import numpy as np
import pandas as pd


# load data as Pandas dataframe
df = pd.read_csv('train.csv', index_col=0)

# drop irrelevant columns
df = df.drop(['Name', 'Ticket'], axis=1)

print(df.head())
