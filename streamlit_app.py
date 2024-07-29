import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from filters import filter,rendement_mes,rendement_PO43,rendement_Turb,filtrage
from PIL import Image
import base64
from io import BytesIO
import os

st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")
import streamlit as st


def image_to_base64(image_path):
    img = Image.open(image_path)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

# Charger et centrer l'image dans la barre latérale
logo_path = "logo.png"  # Assurez-vous que le fichier logo.png est dans le même répertoire que ce script
logo_base64 = image_to_base64(logo_path)

st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" width="150">
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;'> Dessalement mobile de l'eau de mer à JORF LASFAR</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


st.sidebar.markdown("<h3 style='text-align: center;'>Visualisation des paramètres: </h3>", unsafe_allow_html=True)


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

st.sidebar.markdown("<h3 style='text-align: center;'>Comparaison des paramètres: </h3>", unsafe_allow_html=True)


sheets =["QT_avant","QT_PF","QT_après","QT_PRO",
         "ESLI_avant","ESLI_PF", "ESLI_après","ESLI_PRO",
         "ION_avant","ION_PF","ION_après","ION_PRO"]

data = {}
for sheet in sheets:
    data[sheet] = pd.read_excel('DATA/data préparé.xlsx',sheet_name=sheet)

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

# Vérifier si des options ont été sélectionnées pour toutes les catégories
if unity_to_compare and phase_to_compare and param_to_compare:
    # Appeler les fonctions avec les options sélectionnées
    #compare([unity_to_compare, phase_to_compare, param_to_compare])
    filtrage([unity_to_compare, phase_to_compare, param_to_compare])

if param_to_compare == ["MES"]:
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de MES:</h2>", unsafe_allow_html=True)
    rendement_mes(data)
elif param_to_compare == ["PO43-"]:
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de PO43-:</h2>", unsafe_allow_html=True)
    rendement_PO43(data)
elif param_to_compare == ["Turb"]:
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements des moyennes de Turb:</h2>", unsafe_allow_html=True)
    rendement_Turb(data) 