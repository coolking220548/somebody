import pandas as pd

df = pd.read_csv('madang.csv')

print(df.iloc[0:9,0:4])