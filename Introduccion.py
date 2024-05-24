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
st.markdown('***')