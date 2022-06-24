import streamlit as st
import pandas as pd
import plotly.express as mp

# Archivo a trabajar
df = pd.read_csv('listings.csv')

# Config de la pagina 
st.set_page_config(page_title="AirBnB (L.A)",
                   page_icon="🌎",
                   layout="wide")

# ---- Side-Bar ----
st.sidebar.header("Modifica los filtros:")

# Selectboc para barrios
barrio = st.sidebar.selectbox('Selecciona un barrio:', sorted((df["neighbourhood"]).unique().tolist()))

# multiselect para el tipo de hospedaje
default_room=["Entire home/apt"]
hospedaje = st.sidebar.multiselect(
    "Selecciona el tipo de hospedaje",
    df['room_type'].unique(),
    default_room)


# Slider para determinar el maximo y minimo de precios
valor_min = int(df["price"].min())
valor_max = int(df["price"].max())
step=200
precios = st.sidebar.slider('Elige un rango de precio', 
                            valor_min, 
                            valor_max, 
                            (valor_min, valor_max),
                            step)

# Slider para seleccionar un minimo de reviews
reviews_max = int(df["number_of_reviews"].max())
reviews = st.sidebar.slider('Seleccione un minimo de reviews', 0, reviews_max)

# df filtrado
df_filter=df.query("neighbourhood == @barrio & room_type == @hospedaje & price >= @precios[0] & price <= @precios[1] & number_of_reviews >= @reviews")

# --- Página ---
# Título
st.title("AirBnb datos sobre Los Angeles")
#st.subheader(barrio)
st.markdown(barrio)

st.map(df_filter)
muestra=df_filter.loc[:,["name","neighbourhood","room_type","price","number_of_reviews"]]
st.dataframe(muestra)

df_barrio=df.query("neighbourhood == @barrio")
df_barrio_lista= df_barrio["room_type"].tolist()
Entire_home_apt=["Entire home/apt", df_barrio_lista.count("Entire home/apt")]
Private_room= ["Private room", df_barrio_lista.count("erivate room")]
Shared_room=["Shared room",  df_barrio_lista.count("Shared room")]
Hotel_room=["Hotel room", df_barrio_lista.count("Hotel room")]

list_room=[Entire_home_apt, Private_room, Shared_room, Hotel_room]
d = {"Type_room": ["Entire home/apt", "Private room", "Shared room", "Hotel room"],
     "Total": [df_barrio_lista.count("Entire home/apt"), df_barrio_lista.count("erivate room"),
                df_barrio_lista.count("Shared room"), df_barrio_lista.count("Hotel room")]}

df_torta=pd.DataFrame(data=d)

torta = mp.pie(df_torta, 
               "Porcentaje por hospedaje",
               values="Total",
               names="Type_room")

st.pyplot_chart(torta)
