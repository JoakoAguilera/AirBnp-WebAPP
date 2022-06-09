import streamlit as st
import numpy as np
import pandas as pd


# Config de la pagina 
st.set_page_config(
     page_title="AirBnB (L.A)",
     page_icon="🌎",
     layout="wide",
     initial_sidebar_state="auto",
 ) 

# Titulo
st.title("Las Vegas")
df = pd.read_csv('listings.csv')

values = st.slider('Select a range of values', 0.0, 25000.0, (6250.0, 18750.0))
st.write('Values:', values)

st.map(df[(df["price"] < values[1]) & (df["price"] > values[0])])
