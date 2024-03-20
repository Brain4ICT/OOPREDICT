import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from streamlit_option_menu import option_menu

def arima_forecasting():
    return np.random.rand(12)

def kernel_ridge_forecasting():
    return np.random.rand(12)

def lstm_forecasting():
    return np.random.rand(12)

st.title('Olive Oil Prices: Modèles Prévisionnels')

with st.sidebar:
    selected_tab = option_menu("", ['Accueil', 'Univariate Forecasting', 'Multivariate Forecasting'])

if selected_tab == 'Accueil':
    st.write("Bienvenue sur l'application de prévision des prix de l'huile d'olive.")
    st.write("Cette application vous permet de prévoir les prix de l'huile d'olive en utilisant différentes méthodes de prévision.")

elif selected_tab == 'Univariate Forecasting':
    st.write("## Univariate Forecasting")
    st.write("Veuillez télécharger un fichier CSV contenant les données.")
    uploaded_file = st.file_uploader("Uploader un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Données téléchargées:")
        st.write(data)

        st.write("Appuyez sur le bouton ci-dessous pour effectuer les prévisions univariées.")

        if st.button('Univariate Forecasting'):
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(range(1, 13)), y=arima_forecasting(), mode='lines', name='ARIMA'))
            fig.add_trace(go.Scatter(x=list(range(1, 13)), y=kernel_ridge_forecasting(), mode='lines', name='Kernel Ridge Regression'))
            fig.update_layout(xaxis_title='Semaine', yaxis_title='Prix', title='Univariate Forecasting')
            st.plotly_chart(fig)

elif selected_tab == 'Multivariate Forecasting':
    st.write("## Multivariate Forecasting")
    st.write("Remplissez les champs suivants avec les variables appropriées.")

    variables = []
    for i in range(16):
        variables.append(st.number_input(f'Variable {i+1}', min_value=0.0))

    if st.button('Multivariate Forecasting'):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(1, 13)), y=np.random.rand(12), mode='lines', name='Linear Regression'))
        fig.add_trace(go.Scatter(x=list(range(1, 13)), y=np.random.rand(12), mode='lines', name='LSTM'))
        fig.update_layout(xaxis_title='Semaine', yaxis_title='Prix', title='Multivariate Forecasting')
        st.plotly_chart(fig)
