import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from filters import rendement_mes,rendement_PO43,rendement_Turb,compare,filtrage
from fonctions import filter
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
                                "ION EXCHANGE",
                                "MCT"])

phase = st.sidebar.selectbox('Phase de traitement:',
                            [' ',
                            'intake',
                            'Perméat filtration',
                            'Après filtration à cartouche',
                            'Perméat RO'])
filter(unity,phase)



