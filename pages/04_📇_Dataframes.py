import pandas as pd
import streamlit as st

st.title("Dataframes de Homicidios y Lesionados")

# Definir las Columnas que interesan

columnas_1 = ['ID_SINIESTRO', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']
columnas_2 = ['ID_SINIESTRO', 'AÑO', 'ROL', 'VICTIMA', 'SEXO', 'EDAD', 'FECHA_FALLECIMIENTO']
columnas_3 = ['ID_LESIONES', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']
columnas_4 = ['ID_LESIONES', 'AÑO', 'VEHICULO_VICTIMA', 'SEXO', 'EDAD_VICTIMA']


# Cargar Dataframe

df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', usecols=columnas_1)
df_homicidiosHechos.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Eventos de Homicidios")
st.dataframe(df_homicidiosHechos)

df_homicidiosVictimas = pd.read_csv('data//homicidios_victimas_etl.csv', usecols=columnas_2)
df_homicidiosVictimas.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Victimas de Homicidios")
st.dataframe(df_homicidiosVictimas)

df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', usecols=columnas_3)
df_lesionesHechos.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Eventos de Lesionados")
st.dataframe(df_lesionesHechos)

df_lesionesVictimas = pd.read_csv('data//lesiones_victimas_etl.csv', usecols=columnas_4)
df_lesionesVictimas.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Victimas de Lesionados")
st.dataframe(df_lesionesVictimas)