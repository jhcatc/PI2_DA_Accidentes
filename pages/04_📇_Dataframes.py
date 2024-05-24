import pandas as pd
import numpy as np
import streamlit as st

st.title("Dataframes de Homicidios y Lesionados")

# Definir las Columnas que interesan
columnas_1 = ['ID_SINIESTRO', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']
columnas_2 = ['ID_LESIONES', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']

# Cargar Dataframe
df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', usecols=columnas_1)
df_homicidiosHechos.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Homicidios")
st.dataframe(df_homicidiosHechos)

df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', usecols=columnas_2)
df_lesionesHechos.dropna(inplace=True)
# Mostrar el título del DataFrame y el Dataframe
st.subheader("Datos de Lesionados")
st.dataframe(df_lesionesHechos)