import pandas as pd
import streamlit as st

st.subheader("Dataframes de Homicidios y Lesionados")

# Definir las columnas a seleccionar
columnas_1 = ['ID_SINIESTRO', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']
columnas_2 = ['ID_SINIESTRO', 'AÑO', 'ROL', 'VICTIMA', 'SEXO', 'EDAD', 'FECHA_FALLECIMIENTO']
columnas_3 = ['ID_LESIONES', 'VICTIMAS', 'AÑO', 'MES', 'DIA', 'DIRECCION', 'VICTIMA']
columnas_4 = ['ID_LESIONES', 'AÑO', 'VEHICULO_VICTIMA', 'SEXO', 'EDAD_VICTIMA']

# Crear una lista de opciones
opciones = ["Datos de Eventos de Homicidios",
            "Datos de Victimas de Homicidios",
            "Datos de Eventos de Lesionados",
            "Datos de Victimas de Lesionados"]

# Crear un selectbox para elegir entre los DataFrames
opcion_seleccionada = st.selectbox("Selecciona el Dataframe que deseas visualizar", opciones)

# Cargar y mostrar el DataFrame según la opción seleccionada
if opcion_seleccionada == "Datos de Eventos de Homicidios":
    df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', usecols=columnas_1)
    df_homicidiosHechos.dropna(inplace=True)
    st.write("Datos de Eventos de Homicidios")
    st.dataframe(df_homicidiosHechos)

elif opcion_seleccionada == "Datos de Victimas de Homicidios":
    df_homicidiosVictimas = pd.read_csv('data//homicidios_victimas_etl.csv', usecols=columnas_2)
    df_homicidiosVictimas.dropna(inplace=True)
    st.write("Datos de Victimas de Homicidios")
    st.dataframe(df_homicidiosVictimas)

elif opcion_seleccionada == "Datos de Eventos de Lesionados":
    df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', usecols=columnas_3)
    df_lesionesHechos.dropna(inplace=True)
    st.write("Datos de Eventos de Lesionados")
    st.dataframe(df_lesionesHechos)

elif opcion_seleccionada == "Datos de Victimas de Lesionados":
    df_lesionesVictimas = pd.read_csv('data//lesiones_victimas_etl.csv', usecols=columnas_4)
    df_lesionesVictimas.dropna(inplace=True)
    st.write("Datos de Victimas de Lesionados")
    st.dataframe(df_lesionesVictimas)