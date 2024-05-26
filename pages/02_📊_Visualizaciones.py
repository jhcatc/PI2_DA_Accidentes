import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.collections import EllipseCollection
import matplotlib.cm as cm
import seaborn as sns
import streamlit as st

# Titular la pagina
st.title('Visualizaciones')

# Cargar archivos CSV

#df_homicidiosHechos_Moto = pd.read_csv('data//homicidiosHechos_Moto.csv', index_col=0)
#df_homicidiosHechos_Semestre = pd.read_csv('data//homicidiosHechos_Semestre.csv', index_col=0)
df_homicidios_lesionados = pd.read_csv('data//homicidios_lesionados.csv', index_col=0)
df_homicidiosHechos = pd.read_csv('data//homicidios_hechos_etl.csv', index_col=0)
df_homicidiosVictimas = pd.read_csv('data//homicidios_victimas_etl.csv', index_col=0)
df_lesionesHechos = pd.read_csv('data//lesiones_hechos_etl.csv', index_col=0)
df_lesionesVictimas = pd.read_csv('data//lesiones_victimas_etl.csv', index_col=0)

st.markdown('***')


# Selección múltiple de años en la barra lateral
año_seleccionado = st.sidebar.multiselect(
    "Seleccione el Año:",
    options=df_homicidiosHechos['AÑO'].unique()
)

# Filtrar los DataFrames según los años seleccionados
if año_seleccionado:
    df_homicidiosHechos_Seleccion = df_homicidiosHechos[df_homicidiosHechos['AÑO'].isin(año_seleccionado)]
    df_homicidiosVictimas_Seleccion = df_homicidiosVictimas[df_homicidiosVictimas['AÑO'].isin(año_seleccionado)]
    df_lesionesHechos_Seleccion = df_lesionesHechos[df_lesionesHechos['AÑO'].isin(año_seleccionado)]
    df_lesionesVictimas_Seleccion = df_lesionesVictimas[df_lesionesVictimas['AÑO'].isin(año_seleccionado)]
    df_homicidios_lesionados_Seleccion = df_homicidios_lesionados[df_homicidios_lesionados['AÑO'].isin(año_seleccionado)]
else:
    df_homicidiosHechos_Seleccion = df_homicidiosHechos
    df_homicidiosVictimas_Seleccion = df_homicidiosVictimas
    df_lesionesHechos_Seleccion = df_lesionesHechos
    df_lesionesVictimas_Seleccion = df_lesionesVictimas
    df_homicidios_lesionados_Seleccion = df_homicidios_lesionados



# Graficar Dispercion respecto a Victimas de Homicidios o de solo Lesiones

columnA, columnB = st.columns(2)

with columnA:
    # Filtrar ubicaciones que no sean "SD"
    df_homicidios_filtrado = df_homicidiosHechos_Seleccion[(df_homicidiosHechos_Seleccion['DIRECCION_NORMALIZADA'] != 'Sd') & (df_homicidiosHechos_Seleccion['DIRECCION_NORMALIZADA'].notna())]

    # Crear el gráfico de dispersión
    plt.figure(figsize=(8, 5))
    ax = sns.scatterplot(data=df_homicidios_filtrado, x='DIRECCION', y='VICTIMA', hue='DIRECCION_NORMALIZADA', legend=False)

    # Ajustar el layout para una mejor visualización
    plt.title('Gráfico de Dispersión de Homicidios por Dirección respecto a Víctimas', y=1.02)
    ax.set_xlabel("Direcciones")
    ax.set_ylabel("Víctimas")
    ax.set_xticks([])  # Eliminar la etiqueta del eje X

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

with columnB:
    # Filtrar ubicaciones que no sean "SD"
    df_lesionados_filtrado = df_lesionesHechos_Seleccion[(df_lesionesHechos_Seleccion['DIRECCION_NORMALIZADA'] != 'Sd') & (df_lesionesHechos_Seleccion['DIRECCION_NORMALIZADA'].notna())]

    # Crear el gráfico de dispersión
    plt.figure(figsize=(8, 5))
    ax = sns.scatterplot(data=df_lesionados_filtrado, x='DIRECCION', y='VICTIMA', hue='DIRECCION_NORMALIZADA', legend=False)

    # Ajustar el layout para una mejor visualización
    plt.title('Gráfico de Dispersión de Lesionados por Dirección respecto a Víctimas', y=1.02)
    ax.set_xlabel("Direcciones")
    ax.set_ylabel("Víctimas")
    ax.set_xticks([])  # Eliminar la etiqueta del eje X

    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)
    

# Graficar Proporcion Homicidios y/o Lesiones por Sexo

column1, column2 = st.columns(2)
# column1 = st.container()

# Graficar proporcion de Hombre - Mujer en Homicidios
with column1:
    # Calcular el conteo de eventos por sexo
    conteo_masculino = df_homicidiosVictimas_Seleccion[df_homicidiosVictimas_Seleccion['SEXO'] == 'Masculino'].shape[0]
    conteo_femenino = df_homicidiosVictimas_Seleccion[df_homicidiosVictimas_Seleccion['SEXO'] == 'Femenino'].shape[0]
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
    colores = {'Masculino': 'lightblue', 'Femenino': 'pink'}

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
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
    
# Graficar proporcion de Hombre - Mujer en Lesionados
with column2:
    # Calcular el conteo de eventos por sexo
    conteo_masculino_lesionados = df_lesionesVictimas_Seleccion[df_lesionesVictimas_Seleccion['SEXO'] == 'Varon'].shape[0]
    conteo_femenino_lesionados = df_lesionesVictimas_Seleccion[df_lesionesVictimas_Seleccion['SEXO'] == 'Mujer'].shape[0]
    conteo_total_lesionados = conteo_masculino_lesionados + conteo_femenino_lesionados

    if conteo_total_lesionados > 0:
        # Calcular los porcentajes
        porcentaje_sexo_masculino_lesionados = (conteo_masculino_lesionados / conteo_total_lesionados) * 100
        porcentaje_sexo_femenino_lersionados = (conteo_femenino_lesionados / conteo_total_lesionados) * 100

        # Crear un DataFrame para graficar
        data = {
            'SEXO': ['Varon', 'Mujer'],
            'Porcentaje': [porcentaje_sexo_masculino_lesionados, porcentaje_sexo_femenino_lersionados]
        }
        df_porcentaje_sexo_lesionados = pd.DataFrame(data)

        # Definir colores
        colores = {'Varon': 'lightblue', 'Mujer': 'pink'}

        # Crear la gráfica
        plt.figure(figsize=(8, 6))
        barplot = sns.barplot(x='SEXO', y='Porcentaje', data=df_porcentaje_sexo_lesionados, palette=colores)

        # Añadir etiquetas con los porcentajes
        for index, row in df_porcentaje_sexo_lesionados.iterrows():
            barplot.text(index, row['Porcentaje'] + 1, f"{row['Porcentaje']:.2f}%", color='black', ha="center")

        # Configurar el título y etiquetas
        plt.title('Porcentaje de Lesionados por Sexo')
        plt.xlabel('Sexo')
        plt.ylabel('Porcentaje')
        plt.ylim(0, 100)  # Asegurar que el eje y va de 0 a 100

        # Mostrar la gráfica
        st.pyplot(plt)
    else:
        st.write("No hay datos disponibles para mostrar.")
        

# Graficar Frecuencia de Homicidios segun edades de las victimas
column_1 = st.container()

# Graficar proporcion de Hombre - Mujer en Homicidios
with column_1:
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

    # Usar un colormap para los colores
    cmap = plt.get_cmap('viridis')
    colors = cmap(np.linspace(0, 1, len(sizes)))

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
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(y), vmax=max(y)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Frecuencia')

    # Mostrar el gráfico
    #plt.show()
    st.pyplot(plt)    
    
    
# Graficar Frecuencia de Homicidios vs frecuencia de Lesionados
column_A = st.container()

# Verificar si el DataFrame filtrado está vacío
if df_homicidios_lesionados_Seleccion.empty:
    st.write("No hay datos disponibles para mostrar.")
else:
    # Eliminar o reemplazar valores NaN o Inf
    df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'].replace([np.inf, -np.inf], np.nan, inplace=True)
    df_homicidios_lesionados_Seleccion.dropna(subset=['LESIONADOS_HOMICIDIO'], inplace=True)

    # Verificar si la columna LESIONADOS_HOMICIDIO está vacía después de eliminar NaNs
    if df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'].empty:
        st.write("Data no disponible")
    else:
        # Asegurarse de que los valores sean numéricos y no haya strings o tipos incompatibles
        df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'] = pd.to_numeric(
            df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'], errors='coerce'
        )

        # Ajustar el tamaño del gráfico
        fig, ax1 = plt.subplots(figsize=(12, 5))  # Cambia el tamaño del gráfico aquí (ancho, alto)

        # Graficar Homicidios en el eje Y izquierdo
        ax1.bar(df_homicidios_lesionados_Seleccion['AÑO'], df_homicidios_lesionados_Seleccion['HOMICIDIOS'], color='purple', alpha=0.7)
        ax1.set_xlabel('Año', fontsize=12)  # Ajusta el tamaño de la fuente del eje X
        ax1.set_ylabel('Homicidios', color='purple', fontsize=12)  # Ajusta el tamaño de la fuente del eje Y izquierdo
        ax1.tick_params(axis='y', labelcolor='purple')

        # Crear un segundo eje Y para Lesionados_por_Homicidio
        ax2 = ax1.twinx()
        ax2.plot(df_homicidios_lesionados_Seleccion['AÑO'], df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'], color='k', marker='o', linestyle='-')
        ax2.set_ylabel('Lesionados por Homicidio', color='k', fontsize=12)  # Ajusta el tamaño de la fuente del eje Y derecho
        ax2.tick_params(axis='y', labelcolor='k')

        # Ajustar la escala del segundo eje Y, verificando si hay valores no NaN
        if not df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO'].isna().all():
            ax2.set_ylim(0, max(df_homicidios_lesionados_Seleccion['LESIONADOS_HOMICIDIO']))

        # Ajustar la fuente de la leyenda (si hay alguna leyenda)
        ax2.legend(['Lesionados por Homicidio'], loc='upper left', fontsize=10)  # Añade una leyenda y ajusta su tamaño de fuente

        # Mostrar el gráfico
        plt.title('Homicidios y Lesionados por Homicidio por Año', fontsize=14)  # Ajusta el tamaño de la fuente del título
        plt.show()

        # Mostrar el gráfico
        st.pyplot(fig)  # Muestra la figura en lugar de plt para streamlit