import streamlit as st
import pandas as pd
import plotly.express as px

# Archivo a trabajar
df = pd.read_csv('listings.csv')

# Config de la pagina 
st.set_page_config("AirBnB (L.A)",
                   "🌎",
                   "wide",
                   "collapsed")

# ---- Side-Bar ----
st.sidebar.header("Modifica los filtros:")

# Selectbox para barrios
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
step = 200
precios = st.sidebar.slider('Elige un rango de precio', 
                            valor_min, 
                            valor_max, 
                            (valor_min, valor_max),
                            step)

# Slider para seleccionar un minimo de reviews
step2 = 5
reviews = st.sidebar.slider('Seleccione un mínimo de reviews', 0, 200 , 0, step2)

# df filtrado
df_filter=df.query("neighbourhood == @barrio & room_type == @hospedaje & price >= @precios[0] & price <= @precios[1] & number_of_reviews >= @reviews")

# --- Página ---
# Título
st.title("AirBnb datos sobre Los Angeles")
#st.subheader(barrio)
st.markdown(f"Se muestran {len(df_filter)} resultados en el mapa")

st.map(df_filter)
muestra=df_filter.loc[:,["name","neighbourhood","room_type","price","number_of_reviews"]]
st.dataframe(muestra)
# --- Grafico de barras ---
df_barra = pd.DataFrame()
x = ["Hotel room", "Entire home/apt", "Private room", "Shared room"]
df_barra["Tipo de hospedaje"] = x

df_hotel_room = df.query("room_type == \"Hotel room\"")
valor1 = df_hotel_room["price"].mean()
df_entire_home = df.query("room_type == \"Entire home/apt\"")
valor2 = df_entire_home["price"].mean()
df_Private_room = df.query("room_type == \"Private room\"")
valor3 = df_Private_room["price"].mean()
df_Shared_room = df.query("room_type == \"Shared room\"")
valor4 = df_Shared_room["price"].mean()

y = [valor1, valor2, valor3, valor4]
df_barra["Precio promedio"] = y

grafico1 = px.bar(df_barra, "Tipo de hospedaje", "Precio promedio", "Tipo de hospedaje",)


# --- Gráfico de torta  ---

df_torta = pd.DataFrame()
df_torta["Tipo de hospedaje"] = x

hotel_room_count = list(df_filter["room_type"]).count("Hotel room")
Entire_home_count = list(df_filter["room_type"]).count("Entire home/apt")
Private_room_count = list(df_filter["room_type"]).count("Private room")
Shared_count = list(df_filter["room_type"]).count("Shared room")

valores = [hotel_room_count, Entire_home_count, Private_room_count, Shared_count]
df_torta["Total"] = valores

grafico2 = px.pie(df_torta, "Tipo de hospedaje", "Total", "Tipo de hospedaje")


# Diseño de la pagina

col1, col2 = st.columns(2)

with col1:
    st.write(grafico1)
with col2:
    st.write(grafico2)
