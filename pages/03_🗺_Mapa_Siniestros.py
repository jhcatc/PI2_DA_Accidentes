import streamlit as st
import streamlit.components.v1 as components

# Titular la pagina
st.title('Mapa de los Siniestros en CABA')

st.markdown('***')

# Ruta al archivo HTML
html_file_path = 'code//mapa.html'

# Leer el contenido del archivo HTML
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Mostrar el contenido HTML en Streamlit
components.html(html_content, height=450, scrolling=True)