import streamlit as st
import numpy as np
import pandas as pd

# Config de la pagina 
st.set_page_config(
     page_title = "AirBnB (L.A)",
     page_icon = "🌎",
     layout = "wide",
     initial_sidebar_state = "auto",) 

# Título
st.title("Los Angeles")
df = pd.read_csv('listings.csv')

# Slider segun la cantidad de reviews de cada tipo de hospedaje
valor_min = float(df["price"].min())
valor_max = float(df["price"].max())

values = st.slider('Select a range of values', valor_min, valor_max, ((valor_max / 4) , (valor_max * 0.75))) 
# modificar parametros con una lista
st.write('Values:', values)

# Mapa
st.map(df[(df["price"] < values[1]) & (df["price"] >= values[0])])
