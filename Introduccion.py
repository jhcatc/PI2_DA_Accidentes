import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
import calendar
import streamlit as st

#Streamlit run Introduccion.py
st.set_page_config(page_title = 'PI_2', #Nombre de la pagina, sale arriba cuando se carga streamlit
                   page_icon = 'clipboard:', # https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")
st.title(':ambulance: Reporte Proyecto Integrador 2 - Siniestros Viales') #Titulo del Dash
st.subheader('HENRY')
st.markdown('##') #Para separar el titulo de los KPIs, se inserta un paragrafo usando un campo de markdown
st.markdown('***')


# Cargar archivos CSV
df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', index_col=0)
df_homicidiosVictimas = pd.read_csv('data//homicidios_victimas_etl.csv', index_col=0)
df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', index_col=0)
df_lesionesVictimas = pd.read_csv('data//lesiones_victimas_etl.csv', index_col=0)
df_homicidiosHechos_Moto = pd.read_csv('data//homicidiosHechos_Moto.csv', index_col=0)
df_homicidiosHechos_Semestre = pd.read_csv('data//homicidiosHechos_Semestre.csv', index_col=0)
df_homicidios_lesionados = pd.read_csv('data//homicidios_lesionados.csv', index_col=0)
df_poblacion_CABA = pd.read_csv('data//poblacion_CABA.csv', index_col=0)

#st.dataframe(df) 

st.sidebar.header("Aplicar Filtros:") #sidebar lo que nos va a hacer es crear en la parte izquierda un cuadro para agregar los filtros que queremos tener

