import streamlit as st
import pandas as pd
import plotly.express as px
from filters import filter
import os

st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")
import streamlit as st



st.sidebar.image("logo.png")
st.title(":bar_chart:  Desslement de l'eau de mer")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


st.sidebar.header("Chose your filter: ")
unity = st.sidebar.selectbox('Sélectionner l\'unité',
                              [" ",
                               "QT",
                                "ESLI",
                                "ION EXCHANGE"])

phase = st.sidebar.selectbox('Sélectionner la phase de traitement',
                            [' ',
                            'Avant filtraion fine',
                            'Perméat filtration',
                            'Après filtration à cartouche',
                            'Perméat RO'])
filter(unity,phase)
selected_unity = st.sidebar.multiselect('Sélectionner les unités à comparées',
                              ["QT",
                                "ESLI",
                                "ION"])
selected_pahse = st.sidebar.multiselect('Sélectionner les unités à comparées',
                              ['avant',
                            'PF',
                            'après',
                            'PRO'])
data ={}
for i in selected_unity:
    for j in selected_pahse:
      data[f"{i}_{j}"] = pd.read_excel('DATA/data préparé.xlsx',sheet_name=f"{i}_{j}")
averages = []
for unity in selected_unity:
   for phase in selected_pahse:
        averages.append(data[f"{unity}_{phase}"].mean())
        
        


