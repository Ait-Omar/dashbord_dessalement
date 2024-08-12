import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from fonctions import filter,filtrage,unity_compare
from PIL import Image
import base64
from io import BytesIO




st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")


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
    <div style="text-align: center; padding-bottom: 40px;">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo" width="150">
    </div>
    """, 
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;color:#095DBA;'> Dessalement de l'eau de mer mobile à JORF LASFAR</h1>", unsafe_allow_html=True)
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
container_style = """
        <style>
        .container {
            background-color: #095DBA;  /* Couleur de l'arrière-plan */
            border: 2px solid #095DBA;  /* Bordure */
            padding: 10px;
            border-radius: 5px;
        }
        .container h3 {
        color: white;  /* Couleur du texte */
        font-family: 'Lobster', cursive;  /* Type de police */
        font-size: 20px;  /* Taille de la police */
        }
        </style>
        <div class="container">
        """

uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    sheets =["ULTRA FILTRATION","Filtre à cartouche","TRAIN RO"]
    data = {}
    for sheet in sheets:
            data[sheet] = pd.read_excel(uploaded_file,sheet_name=sheet)
    try:

            #st.sidebar.markdown("<h3 style='text-align: center;'>Visualisation des paramètres: </h3>", unsafe_allow_html=True)
            container_content0 = """
        <h3 style='text-align: center;'>Visualisation des paramètres: </h3>
        </div>
        """
            st.sidebar.markdown(container_style + container_content0, unsafe_allow_html=True)
            unity = st.sidebar.selectbox('phase:',
                                        ["Options",
                                            "ULTRA FILTRATION",
                                            "Filtre à cartouche",
                                            "TRAIN RO"])

            print(data[unity].columns)     
    except Exception as e:

        st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
