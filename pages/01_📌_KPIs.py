import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Titular la pagina
st.subheader('KPIs')

# Cargar archivos CSV

df_homicidiosHechos_Moto = pd.read_csv('data//homicidiosHechos_Moto.csv', index_col=0)
df_homicidiosHechos_Semestre = pd.read_csv('data//homicidiosHechos_Semestre.csv', index_col=0)
df_homicidios_lesionados = pd.read_csv('data//homicidios_lesionados.csv', index_col=0)

# st.dataframe(df) 

# Filtrar los tres DataFrames por el año seleccionado
año_seleccionado = st.sidebar.selectbox(
    "Seleccione el Año:",
    options=df_homicidiosHechos_Semestre['AÑO'].unique(),
    index=0  # Selecciona el primer año por defecto
)

df_homicidiosHechos_Moto_Seleccion = df_homicidiosHechos_Moto[df_homicidiosHechos_Moto['AÑO'] == año_seleccionado]
df_homicidiosHechos_Semestre_Seleccion = df_homicidiosHechos_Semestre[df_homicidiosHechos_Semestre['AÑO'] == año_seleccionado]
df_homicidios_lesionados_Seleccion = df_homicidios_lesionados[df_homicidios_lesionados['AÑO'] == año_seleccionado]

# Filtrar por Semestre
semestre_seleccionado = st.sidebar.selectbox(
    "Seleccione el Semestre:",
    options = df_homicidiosHechos_Semestre['SEMESTRE'].unique(),
    index=0  # Selecciona el primer semestre por defecto
)

df_homicidiosHechos_Semestre_Seleccion = df_homicidiosHechos_Semestre_Seleccion[df_homicidiosHechos_Semestre_Seleccion['SEMESTRE'] == semestre_seleccionado]


# KPIs

tasa_homicidios = df_homicidiosHechos_Semestre_Seleccion['TASA_HOMICIDIOS']
accidentes_motorizados = df_homicidiosHechos_Moto_Seleccion['EVOLUCION_ANUAL']
lesionados_homicidio = df_homicidios_lesionados_Seleccion['PROPORCION']

column1, column2, column3 = st.columns(3)

with column1:
    st.write("Tasa Semestral de Homicidios cada 100 000 hab en CABA:")
    st.write(df_homicidiosHechos_Semestre_Seleccion['TASA_HOMICIDIOS'].iloc[0])

with column2:
    st.write('Evolucion Anual de Accidentes Mortales en Motorizados:')
    st.write(df_homicidiosHechos_Moto_Seleccion['EVOLUCION_ANUAL'].iloc[0])

with column3:
    st.write('Proporción Anual de Lesionados por cada Homicidio:')
    st.write(df_homicidios_lesionados_Seleccion['PROPORCION'].iloc[0])    


# Graficar KPI 1 y KPI 2

columnA, columnB = st.columns(2)

with columnA:
    # Graficar con Seaborn y Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Deshabilitar advertencia de Pyplot Global Use

    # Obtener los valores únicos de la columna SEMESTRE
    unique_semesters = df_homicidiosHechos_Semestre['SEMESTRE'].unique()

    # Asignar colores personalizados a cada semestre
    custom_palette = dict(zip(unique_semesters, sns.color_palette('husl', len(unique_semesters))))

    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(8, 4))

    # Graficar las barras de TASA_HOMICIDIOS con los colores personalizados
    sns.barplot(data=df_homicidiosHechos_Semestre, x='AÑO', y='TASA_HOMICIDIOS', hue='SEMESTRE', ax=ax, palette=custom_palette)

    # Configuraciones adicionales
    ax.set_ylabel('Tasa de Homicidios', fontsize=14)
    ax.set_xlabel('Año - Semestre', fontsize=14)
    ax.set_title('Tasa de Homicidios por Año y Semestre', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.legend(title='Semestre', title_fontsize='13', fontsize='11')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

with columnB:
    # Configuración de Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Deshabilitar advertencia de Pyplot Global Use

    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(8, 4.65))

    # Graficar las barras de MOTOS con el color acuamarine
    sns.barplot(data=df_homicidiosHechos_Moto, x='AÑO', y='MOTOS', color='aquamarine', ax=ax)

    # Configuraciones adicionales
    ax.set_ylabel('Homicidios en Motos', fontsize=14)
    ax.set_xlabel('Año', fontsize=14)
    ax.set_title('Homicidios en Motos por Año', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=12)

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
    
# Graficar KPI 3

# Filtrar los datos para los años 2019 a 2021
df_filtered = df_homicidios_lesionados[df_homicidios_lesionados['AÑO'].isin([2019, 2020, 2021])]

# Configuración de Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)  # Deshabilitar advertencia de Pyplot Global Use

# Crear tres columnas
col_1, col_2, col_3 = st.columns(3)

# Gráfico 1: X AÑO, Y LESIONADOS 
with col_1:
    fig, ax1 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_filtered, y='AÑO', x='LESIONADOS', color='grey', ax=ax1, orient='h')
    ax1.set_xlabel('Lesionados', fontsize=14)
    ax1.set_ylabel('Año', fontsize=14)
    ax1.set_title('Lesionados por Año', fontsize=16)
    ax1.tick_params(axis='both', which='major', labelsize=12)
    st.pyplot(fig)

# Gráfico 2: X AÑO, Y HOMICIDIOS 
with col_2:
    fig, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_filtered, y='AÑO', x='HOMICIDIOS', color='purple', ax=ax2, orient='h')
    ax2.set_xlabel('Homicidios', fontsize=14)
    ax2.set_ylabel('Año', fontsize=14)
    ax2.set_title('Homicidios por Año', fontsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=12)
    st.pyplot(fig)

# Gráfico 3: X AÑO, Y LESIONADOS_HOMICIDIO barplot en rojo
with col_3:
    fig, ax3 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_filtered, y='AÑO', x='LESIONADOS_HOMICIDIO', color='red', ax=ax3, orient='h')
    ax3.set_xlabel('Lesionados por Homicidio', fontsize=14)
    ax3.set_ylabel('Año', fontsize=14)
    ax3.set_title('Lesionados por Homicidio por Año', fontsize=16)
    ax3.tick_params(axis='both', which='major', labelsize=12)
    st.pyplot(fig)