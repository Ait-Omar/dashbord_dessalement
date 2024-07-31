import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from fonctions import filter,filtrage
from PIL import Image
import base64
from io import BytesIO




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
hide_file_upload_style = """
    <style>
    .stFileUploader div[role='button'] {
        display: none;
    }
    .centered {
        display: flex;
        color: red;
        justify-content: center;
        align-items: center;
        height: 50vh;
        font-size: 1.5rem;
    }
    </style>
"""
st.markdown(hide_file_upload_style, unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx", "xls"])


if uploaded_file is not None:
    try:
        st.sidebar.markdown("<h3 style='text-align: center;'>Visualisation des paramètres: </h3>", unsafe_allow_html=True)


        unity = st.sidebar.selectbox('Unité:',
                                    ["Options",
                                    "QT",
                                        "ESLI",
                                        "ION EXCHANGE",
                                        "MCT"])

        if (unity == "MCT"):
            phase = st.sidebar.selectbox('Phase de traitement:',
                                    ['Options',
                                    'Après filtration à cartouche',
                                    'Perméat RO'])
        else:
            phase = st.sidebar.selectbox('Phase de traitement:',
                                    ['Options',
                                    'intake',
                                    'Perméat filtration',
                                    'Après filtration à cartouche',
                                    'Perméat RO'])

        sheets =["QT_PF","QT_après","QT_PRO",
            "ESLI_PF", "ESLI_après","ESLI_PRO",
            "ION_PF","ION_après","ION_PRO",
            "MCT_après","MCT_PRO"]
        st.sidebar.markdown("<h3 style='text-align: center;'>Comparaison des paramètres: </h3>", unsafe_allow_html=True)
        data = {}
        for sheet in sheets:
            data[sheet] = pd.read_excel(uploaded_file,sheet_name=sheet)

        unity_to_compare = st.sidebar.multiselect('Unité:',
                                ["QT",
                                    "ESLI",
                                    "ION",
                                    "MCT"])
        if unity_to_compare == ["MCT"]:
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                    [
                                    'après',
                                    'PRO'])  
        else:
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                    [
                                    'PF',
                                    'après',
                                    'PRO'])  

        if phase_to_compare:
            param_to_compare = st.sidebar.multiselect('paramètres:',
                                    data[f"{unity_to_compare[0]}_{phase_to_compare[0]}"].columns[1:])  
        filter(uploaded_file,unity,phase)
        if unity_to_compare and phase_to_compare and param_to_compare:
         filtrage(uploaded_file,[unity_to_compare, phase_to_compare, param_to_compare])        
    except Exception as e:

        st.markdown(f"<h3 style='text-align: center;color:red;'> le fichier n'est pas dans le format adapté: {e}</h3>", unsafe_allow_html=True)

else:
    st.markdown('<div class="centered">Veuillez charger un fichier Excel bien adapter pour commencer.</div>', unsafe_allow_html=True)

    