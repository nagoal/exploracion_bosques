import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Datos mundiales recopilados por Naciones Unidas sobre la meta de desarrollo sostenible número 15: Proteger, restablecer y promover el uso sostenible de los ecosistemas terrestres, gestionar sosteniblemente los bosques, luchar contra la desertificación, detener e invertir la degradación de las tierras y detener la pérdida de biodiversidad')  # poner un encabezado

bosques_data = pd.read_csv('Data_SDG15.csv', sep=";")  # leer los datos

hist_button = st.button('Construir histograma de bosques')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de áreas certificadas de bosques')

# crear un histograma
    fig = px.histogram(bosques_data, x='Forest area certified under an independently verified certification scheme (thousands of hectares)',
                       title='Extension de bosques certificados por terceros a 2023 (miles de hectareas)')

# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button(
    'Construir diag. de dispersión de ecosistemas de montaña protegidos')  # crear un botón

if scatter_button:  # al hacer clic en el botón
 # escribir un mensaje
    st.write('Creación de un diag. de dispersión para la porción de recursos ambientales clave de montaña que están protegidos vs. la extensión de los bosques certificados por agentes independientes')

# crear un diagrama de dispersión
    fig = px.scatter(bosques_data, x="Average proportion of Mountain Key Biodiversity Areas (KBAs) covered by protected areas (%)",
                     y="Forest area certified under an independently verified certification scheme (thousands of hectares)")

# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
