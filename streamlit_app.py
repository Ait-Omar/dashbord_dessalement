import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from filters import filter,rendement_mes,rendement_PO43,rendement_Turb,compare,filtrage


st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")
import streamlit as st




st.sidebar.image("logo.png")
st.title(":bar_chart:  Desslement de l'eau de mer")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


st.sidebar.header("Visualisation des paramètres: ")

unity = st.sidebar.selectbox('Unité:',
                              [" ",
                               "QT",
                                "ESLI",
                                "ION EXCHANGE"])

phase = st.sidebar.selectbox('Phase de traitement:',
                            [' ',
                            'Avant filtraion fine',
                            'Perméat filtration',
                            'Après filtration à cartouche',
                            'Perméat RO'])
filter(unity,phase)

st.sidebar.subheader('Comparaison des paramètres:')

selected_param = st.sidebar.selectbox('test:',
                              [" ",
                               "pH",
                               "SDI15",
                                "MES",
                                "Turb",
                                "Cond",
                                "PO43-"])

sheets =["QT_avant","QT_PF","QT_après","QT_PRO",
         "ESLI_avant","ESLI_PF", "ESLI_après","ESLI_PRO",
         "ION_avant","ION_PF","ION_après","ION_PRO"]

data = {}
for sheet in sheets:
    data[sheet] = df = pd.read_excel('DATA/data préparé.xlsx',sheet_name=sheet)

if selected_param == "MES":
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de MES:</h2>", unsafe_allow_html=True)
    rendement_mes(data)
elif selected_param == "PO43-":
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de PO43-:</h2>", unsafe_allow_html=True)
    rendement_PO43(data)
elif selected_param == "Turb":
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de Turb:</h2>", unsafe_allow_html=True)
    rendement_Turb(data) 

unity_to_compare = st.sidebar.multiselect('Unité:',
                              ["QT",
                                "ESLI",
                                "ION"])
phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                            ['avant',
                            'PF',
                            'après',
                            'PRO'])  
param_to_compare = st.sidebar.multiselect('paramètres:',
                              ["pH",
                               "SDI15",
                                "MES",
                                "Turb",
                                "Cond",
                                "PO43-",
                                "Fe3+",
                                "Fe2+"])  

compare( [unity_to_compare,phase_to_compare,param_to_compare])

filtrage([unity_to_compare,phase_to_compare,param_to_compare])