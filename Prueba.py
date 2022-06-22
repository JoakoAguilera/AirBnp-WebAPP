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

#Constante para determinar el max y min de los precios
valor_min = float(df["price"].min())
valor_max = float(df["price"].max())




# Barrio
barrio = st.selectbox(
     'Selecciona un barrio:',
     sorted(list(set(list(df['neighbourhood'])))))

# Tipo de hospedaje
hospedaje = st.multiselect(
     'Selecciona tipo de hospedaje',
     sorted(list(set(list(df['room_type'])))),
     ["Entire home/apt"])

#Slider para determinar el maximo y minimo de precios
values = st.slider('Elige un rango de precio', valor_min, valor_max, ((valor_max / 4) , (valor_max * 0.75))) 
# modificar parametros con una lista
st.write('Values:', values)

#Constante para determinar el maximo de reviews
reviews_max = int(df["number_of_reviews"].max())
#Slider para seleccionar un minimo de reviews
reviews = st.slider('Seleccione un minimo de reviews', 0, reviews_max, 0)

# Mapa
st.map(
     df[((df["neighbourhood"] == barrio) 
     & (df["room_type"] == hospedaje[0])
     & (df["price"] >= values[0]) 
     & (df["price"] <= values[1])
     & (df["number_of_reviews"] >= reviews))])


import matplotlib.pyplot as plt
 
arr = np.random.normal(1, 1, size=40)
fig, ax = plt.subplots()
ax.hist(arr, bins=3)
plt.axis ([0,6,0,20])
plt.rcParams["figure.figsize"]=(20,3)
labels= [list(df ["room_type"]).count("Hotel room"),list(df ["room_type"]).count("Private room"),list(df ["room_type"]).count("Shared room")]
ax.set_xticklabels(labels)

st.pyplot(fig)



https://matplotlib.org/stable/plot_types/stats/pie.html#sphx-glr-plot-types-stats-pie-py
