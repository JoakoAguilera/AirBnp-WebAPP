import pandas as pd
import matplotlib as mp
import streamlit as st 


filename = 'listings.csv'
df = pd.read_csv(filename, header=0)

print(df[["price"]])

