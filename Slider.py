import pandas as pd
import matplotlib as mp

filename = 'listings.csv'
df = pd.read_csv(filename, header=0)
df_precios = df[['price']]

print(df_precios.describe())

