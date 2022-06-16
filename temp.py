import streamlit as st
import pandas as pd
df = pd.read_csv('listings.csv')

st.selectbox(
     'Selecciona un barrio:',
     sorted(list(set(list(df['neighbourhood'])))))