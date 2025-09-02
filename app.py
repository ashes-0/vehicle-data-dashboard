import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Lee los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de anuncios de venta de coches')

# Crear un botón que construirá un histograma
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se haga clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón que construirá un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, use_container_width=True)