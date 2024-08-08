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
    sheets =["QT_intake","QT_PERMEAT FILTRATION","QT_APRES FILTRES A CARTOUCHE","QT_PERMEAT RO","QT_sortie_global",
            "ESLI_intake","ESLI_PERMEAT FILTRATION", "ESLI_APRES FILTRES A CARTOUCHE","ESLI_PERMEAT RO",
            "ION_intake","ION_PERMEAT FILTRATION","ION_Bac_stockage","ION_APRES FILTRES A CARTOUCHE","ION_PERMEAT RO",
            "MCT_intake","MCT_APRES FILTRES A CARTOUCHE","MCT_PERMEAT RO"]
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
            unity = st.sidebar.selectbox('Unité:',
                                        ["Options",
                                            "QT",
                                            "ESLI",
                                            "ION EXCHANGE",
                                            "MCT"])

            if (unity == "MCT"):
                phase = st.sidebar.selectbox('Phase de traitement:',
                                        ['Options',
                                        'intake',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO'])
            elif  (unity == "QT"):
                phase = st.sidebar.selectbox('Phase de traitement:',
                                        ['Options',
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        'QT_sortie_global'])
            elif (unity == "ION EXCHANGE"):
                phase = st.sidebar.selectbox('Phase de traitement:',
                                        ['Options',
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'ION_Bac_stockage',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        ])
            elif(unity == "ESLI"):
                phase = st.sidebar.selectbox('Phase de traitement:',
                                        ['Options',
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        ])
            filter(uploaded_file,unity,phase)
            
    except Exception as e:

        st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
    
    try:
        
        container_content1 = """
        <h3 style='text-align: center;'>Comparaison des phases de traitement: </h3>
        </div>
         """


        st.sidebar.markdown(container_style + container_content1, unsafe_allow_html=True)
        #st.sidebar.markdown("<h3 style='text-align: center;'>Comparaison des paramètres dans la même unité: </h3>", unsafe_allow_html=True)
    
        phase_to_compare = []

        unity_to_compare = st.sidebar.selectbox('Unité :',
                                ["options",
                                    "QT",
                                    "ESLI",
                                    "ION",
                                    "MCT"])
        if unity_to_compare == "MCT":
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                        [
                                        'intake',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO'])
        elif  ( unity_to_compare == "QT"):
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                        [
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        'sortie_global'])
        elif (unity_to_compare == "ION"):
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                        [
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'Bac_stockage',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        ])
        elif(unity_to_compare == "ESLI"):
            phase_to_compare = st.sidebar.multiselect('Phase de traitement:',
                                        [
                                        'intake',
                                        'PERMEAT FILTRATION',
                                        'APRES FILTRES A CARTOUCHE',
                                        'PERMEAT RO',
                                        ])
            
        param_to_compare = {}

        if phase_to_compare:
            for j in range(len(phase_to_compare)):  
                param_to_compare[f"{unity_to_compare}_{phase_to_compare[j]}"] = st.sidebar.multiselect(f'paramètres d\'{phase_to_compare[j]}',
                                    data[f"{unity_to_compare}_{phase_to_compare[j]}"].columns[1:]) 

        filtrage(uploaded_file,[unity_to_compare, phase_to_compare, param_to_compare]) 
       

    except Exception as e:

        st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
    try:
        container_content2 = """
        <h3 style='text-align: center;'>Comparaison des unitées:</h3>
        </div>
        """
        st.sidebar.markdown(container_style + container_content2, unsafe_allow_html=True)
        unity_to_compare1 = st.sidebar.multiselect('Unité:',
                                [
                                    "QT",
                                    "ESLI",
                                    "ION",
                                    "MCT"])
        phase_traitement = {}
        paramètre = {}
        for i in range(len(unity_to_compare1)):
            if unity_to_compare1[i]  == "MCT":
                phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.selectbox(f"phase de traitement de {unity_to_compare1[i]}",
                                    [
                                    "intake",
                                    'APRES FILTRES A CARTOUCHE',
                                    'PERMEAT RO'])
            elif unity_to_compare1[i]  == "ION":
                phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.selectbox(f"phase de traitement de {unity_to_compare1[i]}",
                                    [
                                    "intake",
                                    "PERMEAT FILTRATION",
                                    "Bac_stockage",
                                    'APRES FILTRES A CARTOUCHE',
                                    'PERMEAT RO'])
            elif unity_to_compare1[i]  == "QT":
                phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.selectbox(f"phase de traitement de {unity_to_compare1[i]}",
                                    [
                                    "intake",
                                    "PERMEAT FILTRATION",
                                    'APRES FILTRES A CARTOUCHE',
                                    'PERMEAT RO',
                                    "sortie_global"])
            elif unity_to_compare1[i]  == "ESLI":
                phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.selectbox(f"phase de traitement de {unity_to_compare1[i]}",
                                    [
                                    "intake",
                                    "PERMEAT FILTRATION",
                                    'APRES FILTRES A CARTOUCHE',
                                    'PERMEAT RO'])
            

            paramètre[f"{unity_to_compare1[i]}_{phase_traitement[unity_to_compare1[i]]}"] = st.sidebar.multiselect(f"paramètres de {unity_to_compare1[i]}_{phase_traitement[unity_to_compare1[i]]}",
                                                                                     data[f"{unity_to_compare1[i]}_{phase_traitement[unity_to_compare1[i]]}"].columns[1:]     )

        unity_compare(uploaded_file,unity_to_compare1,phase_traitement,paramètre)
   

    
    except Exception as e:

       st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
else:
    st.markdown('<div class="centered">Veuillez charger un fichier Excel bien adapter pour commencer.</div>', unsafe_allow_html=True)

