import streamlit as st
import numpy as np
import pandas as pd

# Config de la pagina 
st.set_page_config(
     page_title = "AirBnB (L.A)",
     page_icon = "🌎",
     layout = "wide",
     initial_sidebar_state = "auto",
 ) 

# Título
st.title("Los Angeles")
df = pd.read_csv('listings.csv')

# Slider segun el precio de cada tipo de hospedaje
values = st.slider('Select a range of values', 0.0, 25000.0, (6250.0, 18750.0)) 
# modificar parametros con una lista
st.write('Values:', values)

# Mapa
st.map(df[(df["price"] < values[1]) & (df["price"] > values[0])])
