import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.collections import EllipseCollection
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import seaborn as sns
import streamlit as st
import calendar

# Titular la pagina
st.subheader('Visualizaciones y KPIs')

# Cargar archivos CSV

df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', index_col=0)
df_homicidiosHechos_Moto = pd.read_csv('data//homicidiosHechos_Moto.csv', index_col=0)
df_homicidiosHechos_Semestre = pd.read_csv('data//homicidiosHechos_Semestre.csv', index_col=0)
df_homicidios_lesionados = pd.read_csv('data//homicidios_lesionados.csv', index_col=0)
df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', index_col=0)
df_homicidiosVictimas = pd.read_csv('data//homicidios_victimas_etl.csv', index_col=0)
df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', index_col=0)
df_lesionesVictimas = pd.read_csv('data//lesiones_victimas_etl.csv', index_col=0)

# KPIs

tasa_homicidios = df_homicidiosHechos_Semestre.loc[11, 'REDUCCION']
accidentes_motorizados = df_homicidiosHechos_Moto.loc[5, 'EVOLUCION_ANUAL']
lesionados_homicidio = df_homicidios_lesionados.loc[2, 'PROPORCION']

# Redondear los valores a 4 decimales en los valores de los KPIs
tasa_homicidios = round(tasa_homicidios, 4)
accidentes_motorizados = round(accidentes_motorizados, 4)
lesionados_homicidio = round(lesionados_homicidio, 4)

# Definir criterios de aprobación para segmentar los valores de los KPIs
criterio_tasa_homicidios = 10  # Valor objetivo para tasa de homicidios
criterio_accidentes_motorizados = 7  # Valor objetivo para accidentes motorizados
criterio_lesionados_homicidio = 10  # Valor objetivo para lesionados por homicidio

# Función para aplicar formato condicional al color de los KPIs
def formato_condicional(valor, criterio):
    color = "green" if valor >= criterio else "red"
    return f'<p style="font-size: 26px; color:{color};"> {valor}</p>'

# _____________________________________________

column1, column2, column3, column4, column5= st.columns(5)

with column1:
    st.write("Reducción 10% - Tasa Semestral de Homicidios cada 100 000 hab en CABA:")
    st.markdown(formato_condicional(tasa_homicidios, criterio_tasa_homicidios), unsafe_allow_html=True)

with column2:
    st.write('Reducción 7% - Evolucion Anual de Accidentes Mortales en Motorizados:')
    st.markdown(formato_condicional(accidentes_motorizados, criterio_accidentes_motorizados), unsafe_allow_html=True)

with column3:
    st.write('Aumento 10% - Proporción Anual de Lesionados por cada Homicidio:')
    st.markdown(formato_condicional(lesionados_homicidio, criterio_lesionados_homicidio), unsafe_allow_html=True)  
    
with column4:    
    # Selección múltiple de años en la página principal
    año_seleccionado = st.multiselect(
    "Seleccione el Año:",
    options=df_homicidiosHechos['AÑO'].unique()
    )
    
    # Filtrar los DataFrames según los años seleccionados
    if año_seleccionado:
        df_homicidiosHechos_Seleccion = df_homicidiosHechos[df_homicidiosHechos['AÑO'].isin(año_seleccionado)]
        df_homicidiosVictimas_Seleccion = df_homicidiosVictimas[df_homicidiosVictimas['AÑO'].isin(año_seleccionado)]
    else:
        df_homicidiosHechos_Seleccion = df_homicidiosHechos
        df_homicidiosVictimas_Seleccion = df_homicidiosVictimas
    
with column5: 
    # Selección múltiple de años en la página principal
    direccion_seleccionada = st.multiselect(
    "Seleccione la Direccion:",
    options=df_homicidiosHechos['DIRECCION_NORMALIZADA'].unique()
    )
    
    # Filtrar los DataFrames según las direcciones de ocurrencia
    if direccion_seleccionada:
        df_homicidiosHechos_Seleccion_Direccion = df_homicidiosHechos_Seleccion[df_homicidiosHechos_Seleccion['DIRECCION_NORMALIZADA'].isin(direccion_seleccionada)]
    else:
        df_homicidiosHechos_Seleccion_Direccion = df_homicidiosHechos

# _____________________________________________    

# Graficar KPI 1, KPI 2 y KPI 3

columnA, columnB, columnC = st.columns(3)

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
    sns.barplot(data=df_homicidiosHechos_Moto, x='AÑO', y='MOTOS', color='#459E97', ax=ax)

    # Configuraciones adicionales
    ax.set_ylabel('Homicidios en Motos', fontsize=14)
    ax.set_xlabel('Año', fontsize=14)
    ax.set_title('Homicidios en Motos por Año', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=12)

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

with columnC:
    # Filtrar los datos para los años 2019 a 2021
    #df_filtered = df_homicidios_lesionados[df_homicidios_lesionados['AÑO'].isin([2019, 2020, 2021])]

    # Configuración de Streamlit
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Deshabilitar advertencia de Pyplot Global Use

    # Crear figura y ejes
    fig, axs = plt.subplots(3, 1, figsize=(8, 4.5), sharex=True)

    # Color personalizado
    colors = ['#E68193', '#459E97', '#E68193']

    # Gráfico de barras para Homicidios
    sns.barplot(data=df_homicidios_lesionados, x='AÑO', y='HOMICIDIOS', ax=axs[0], color=colors[0])
    axs[0].set_ylabel('Homicidios')

    # Gráfico de barras para Lesionados
    sns.barplot(data=df_homicidios_lesionados, x='AÑO', y='LESIONADOS', ax=axs[1], color=colors[1])
    axs[1].set_ylabel('Lesionados')

    # Gráfico de barras para Lesionados por Homicidio
    sns.barplot(data=df_homicidios_lesionados, x='AÑO', y='LESIONADOS_HOMICIDIO', ax=axs[2], color=colors[2])
    axs[2].set_ylabel('Lesionados por Homicidio')

    # Ajustes estéticos
    fig.suptitle('Comparación de Homicidios, Lesionados y Lesionados por Homicidio', fontsize=16)

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

# _____________________________

# Crear dos columnas en una sola fila
col1, col2 = st.columns(2)

with col1:
    # Filtrar los datos para omitir los valores 'Sd'
    df_filtrado = df_homicidiosVictimas_Seleccion[df_homicidiosVictimas_Seleccion['EDAD'] != 'Sd']

    # Convertir la columna EDAD a numérica (puede que necesites convertir los datos a enteros)
    df_filtrado['EDAD'] = pd.to_numeric(df_filtrado['EDAD'], errors='coerce')

    # Contar la frecuencia de cada edad
    frecuencia_edad = df_filtrado['EDAD'].value_counts().sort_index()

    # Crear listas para los ejes x, y, y los tamaños de las elipses
    x = frecuencia_edad.index.values
    y = frecuencia_edad.values
    sizes = y  # Podemos usar la frecuencia como tamaño para las elipses

    # Configurar el tamaño del plot
    fig, ax = plt.subplots(figsize=(14, 5), subplot_kw={'aspect': 'auto'})

    # Crear las elipses
    widths = sizes
    heights = sizes
    angles = np.zeros_like(sizes)  # Podemos usar ángulos de 0 grados para todas las elipses

    # Definir los colores deseados en formato HSV
    color_min_hsv = mcolors.rgb_to_hsv(mcolors.hex2color('#E68193'))  # Color mínimo
    color_max_hsv = mcolors.rgb_to_hsv(mcolors.hex2color('#459E97'))  # Color máximo

    # Normalizar los valores de frecuencia
    norm = mcolors.Normalize(vmin=min(y), vmax=max(y))

    # Mapear los valores de frecuencia normalizados al rango de colores
    colors = [mcolors.rgb2hex(mcolors.hsv_to_rgb([color_min_hsv[0] + (color_max_hsv[0] - color_min_hsv[0]) * norm(value), color_min_hsv[1], color_min_hsv[2]])) for value in y]

    # Crear el EllipseCollection con colores
    ellipses = EllipseCollection(widths, heights, angles, units='x', offsets=np.c_[x, y], transOffset=ax.transData, facecolors=colors, edgecolors='black')

    # Añadir las elipses al eje
    ax.add_collection(ellipses)

    # Configurar los ejes
    ax.set_xlim(min(x) - 1, max(x) + 1)
    ax.set_ylim(0, max(y) + 5)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia de Sinistros con Homicidios')
    ax.set_title('Frecuencia de Homicidios por Edad')

    # Añadir una barra de color para indicar la escala de colores
    sm = plt.cm.ScalarMappable(cmap=None, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Frecuencia')

    # Mostrar el gráfico
    st.pyplot(fig)

with col2:
    # Filtrar filas donde el sexo no sea 'Sd'
    df_homicidiosVictimas_Seleccion_filtrado = df_homicidiosVictimas_Seleccion[df_homicidiosVictimas_Seleccion['SEXO'] != 'Sd']

    # Calcular el conteo de eventos por sexo
    conteo_masculino = df_homicidiosVictimas_Seleccion_filtrado[df_homicidiosVictimas_Seleccion_filtrado['SEXO'] == 'Masculino'].shape[0]
    conteo_femenino = df_homicidiosVictimas_Seleccion_filtrado[df_homicidiosVictimas_Seleccion_filtrado['SEXO'] == 'Femenino'].shape[0]
    conteo_total = conteo_masculino + conteo_femenino

    # Calcular los porcentajes
    porcentaje_sexo_masculino = (conteo_masculino / conteo_total) * 100
    porcentaje_sexo_femenino = (conteo_femenino / conteo_total) * 100

    # Crear un DataFrame para graficar
    data = {
        'SEXO': ['Masculino', 'Femenino'],
        'Porcentaje': [porcentaje_sexo_masculino, porcentaje_sexo_femenino]
    }
    df_porcentaje_sexo = pd.DataFrame(data)

    # Definir colores
    colores = {'Masculino': '#459E97', 'Femenino': '#E68193'}

    # Crear la gráfica
    plt.figure(figsize=(15, 6))
    barplot = sns.barplot(x='SEXO', y='Porcentaje', data=df_porcentaje_sexo, palette=colores)

    # Añadir etiquetas con los porcentajes
    for index, row in df_porcentaje_sexo.iterrows():
        barplot.text(index, row['Porcentaje'] + 1, f"{row['Porcentaje']:.2f}%", color='black', ha="center")

    # Configurar el título y etiquetas
    plt.title('Porcentaje de Homicidios por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Porcentaje')
    plt.ylim(0, 100)  # Asegurar que el eje y va de 0 a 100

    # Mostrar la gráfica
    st.pyplot(plt)

# ____________________________________________

# Crear dos columnas en una sola fila
col_1, col_2 = st.columns(2)

with col_1:
    # Filtrar ubicaciones y víctimas que no sean "Sd"
    df_homicidios_filtrado_Direccion = df_homicidiosHechos_Seleccion_Direccion[
        (df_homicidiosHechos_Seleccion_Direccion['DIRECCION_NORMALIZADA'] != 'Sd') &
        (df_homicidiosHechos_Seleccion_Direccion['VICTIMA'] != 'Sd') &
        (df_homicidiosHechos_Seleccion_Direccion['DIRECCION_NORMALIZADA'].notna())
    ]

    # Crear una paleta de colores personalizada
    custom_palette = sns.color_palette(['#459E97', '#E68193'])

    # Crear el gráfico de dispersión
    plt.figure(figsize=(14, 6.3))
    ax = sns.scatterplot(
        data=df_homicidios_filtrado_Direccion, 
        x='DIRECCION', 
        y='VICTIMA',
        hue='DIRECCION_NORMALIZADA', 
        palette=custom_palette,
        legend=False
    )

    # Ajustar el layout para una mejor visualización
    plt.title('Homicidios por Dirección y Víctimas', y=1.02)
    ax.set_xlabel("Direcciones")
    ax.set_ylabel("Víctimas")
    ax.set_xticks([])  # Eliminar la etiqueta del eje X

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

with col_2:
    # Obtener nombres de los meses en español
    nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    # Agrupar por mes y calcular la suma de homicidios
    df_mensual = df_homicidiosHechos_Seleccion.groupby('MES').size()

    # Crear el gráfico
    fig, ax1 = plt.subplots(figsize=(12, 4.7))

    # Crear un gráfico de barras para homicidios
    ax1.bar(df_mensual.index, df_mensual.values, color='#E68193')

    # Configurar el gráfico
    ax1.set_title('Frecuencia de Homicidios por Mes')
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Frecuencia')
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(nombres_meses)

    # Mostrar el gráfico con Streamlit
    st.pyplot(fig)
    
# ____________________________________________

# Define los anchos de las columnas en proporciones
col_A, col_B = st.columns([1, 3])

# Contenido de la primera columna (25% de ancho)
with col_A:
    # Selección múltiple de años en la página principal
    hora_seleccionada = st.multiselect(
    "Seleccione la Hora:",
    options=df_homicidiosHechos_Seleccion['HORA_NORMALIZADA'].unique()
    )
    
    # Filtrar los DataFrames según las direcciones de ocurrencia
    if hora_seleccionada:
        df_homicidiosHechos_Seleccion_Hora = df_homicidiosHechos_Seleccion[df_homicidiosHechos_Seleccion['HORA'].isin(hora_seleccionada)]
    else:
        df_homicidiosHechos_Seleccion_Hora = df_homicidiosHechos

# Contenido de la segunda columna (75% de ancho)
with col_B: 
    # Crear la columna de frecuencia
    df_frecuencia = df_homicidiosHechos_Seleccion_Hora['HORA_NORMALIZADA'].value_counts().reset_index()
    df_frecuencia.columns = ['HORA', 'FRECUENCIA']
    df_frecuencia = df_frecuencia.sort_values('HORA')

    # Función para crear el gráfico de dispersión
    def create_scatterplot(data):
        plt.figure(figsize=(10, 4))
        
        # Crear la paleta de colores personalizada
        colors = sns.color_palette(['#459E97', '#E68193'], as_cmap=True)
        
        scatter_plot = sns.scatterplot(
            data=data,
            x='HORA',       # Eje X
            y='FRECUENCIA', # Eje Y
            size='FRECUENCIA',# Tamaño de los puntos
            hue='FRECUENCIA', # Color de los puntos
            palette=colors,  # Aplicar la paleta de colores
            sizes=(20, 200),  # Tamaño mínimo y máximo de los puntos
            legend='brief'  # Mostrar la leyenda
        )
        # Ajustar la leyenda
        scatter_plot.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

        # Ajustar las etiquetas del eje X para que aparezca solo la primera
        scatter_plot.set_xticks([0])
        scatter_plot.set_xticklabels(['00:00'])

        # Añadir títulos y etiquetas
        plt.title('Frecuencia de Homicidios por hora de Ocurrencia')
        plt.xlabel('Hora del Día')
        plt.ylabel('Frecuencia de Ocurrencia')

        return plt
    
    # Generar y mostrar el gráfico en la primera columna
    fig1 = create_scatterplot(df_frecuencia)
    st.pyplot(fig1)