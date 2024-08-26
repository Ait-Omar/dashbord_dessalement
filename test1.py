

import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO
from fonctions import Visualisation_des_paramètres,Comparaison_des_phases_de_traitement,unity_compare,labo_oper,labo_oper1,labo_oper2,vis_op

#--------------------------------------------------heradr-------------------------------------------------------------
st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")

def image_to_base64(image_path):
    img = Image.open(image_path)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str


logo_path = "logo.png"  
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
#---------------------------------------------Chargement des données---------------------------------------------------
if uploaded_file is not None:
    st.write("Fichier téléchargé avec succès!")
    sheets =["QT_intake","QT_PERMEAT FILTRATION","QT_APRES FILTRES A CARTOUCHE","QT_PERMEAT RO","QT_sortie_global",
        "ESLI_intake","ESLI_PERMEAT FILTRATION", "ESLI_APRES FILTRES A CARTOUCHE","ESLI_PERMEAT RO",
        "ION_intake","ION_PERMEAT FILTRATION","ION_Bac_stockage","ION_APRES FILTRES A CARTOUCHE","ION_PERMEAT RO",
        "MCT_intake","MCT_APRES FILTRES A CARTOUCHE","MCT_PERMEAT RO"]
    data = {}
    for sheet in sheets:
            data[sheet] = pd.read_excel(uploaded_file,sheet_name=sheet)
#----------------------------------------------------body-------------------------------------------------------------


    #st.sidebar.markdown("<h3 style='text-align: center;'>Visualisation des paramètres: </h3>", unsafe_allow_html=True)
    # container_content88= """
    # <h3 style='text-align: center;'>Visualisation des paramètres: </h3>
    # </div>
    # """
    # st.sidebar.markdown(container_style + container_content88, unsafe_allow_html=True)
    # don = st.sidebar.selectbox('Type des Données:',
    #                                 [
    #                                     "Laboratoire",
    #                                     "Operationnelles",
    #                                     "Laboratoire & Operationnelles"
    #                                     ])
    don = st.sidebar.radio('Données:',
                                    [
                                        "Laboratoire",
                                        "Operationnelles",
                                        "Laboratoire & Operationnelles"
                                        ])
    if don == "Laboratoire":
        don1 = st.sidebar.radio('Visualisation:',
                                    [
                                        "Visualisation des paramètres",
                                        "Comparaison des phases de traitement",
                                        "Comparaison des unitées"
                                        ])       
        if don1 == "Visualisation des paramètres":
            # container_content0 = """
            # <h3 style='text-align: center;'>Visualisation des paramètres: </h3>
            # </div>
            # """
            # st.sidebar.markdown(container_style + container_content0, unsafe_allow_html=True)
            unity = st.sidebar.radio('Unité:',
                                            [
                                                "QT",
                                                "ESLI",
                                                "ION EXCHANGE",
                                                "MCT"])
            try:
                if (unity == "MCT"):
                    phase = st.sidebar.radio('Phase:',
                                            [
                                            'intake',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                elif  (unity == "QT"):
                    phase = st.sidebar.radio('Phase:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            'sortie_global'])
                elif (unity == "ION EXCHANGE"):
                    phase = st.sidebar.radio('Phase:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'Bac_stockage',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            ])
                elif(unity == "ESLI"):
                    phase = st.sidebar.radio('Phase:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            ])
                Visualisation_des_paramètres(uploaded_file,unity,phase)         
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif don1 == "Comparaison des phases de traitement":          
            # container_content1 = """
            # <h3 style='text-align: center;'>Comparaison des phases de traitement: </h3>
            # </div>
            # """
            # st.sidebar.markdown(container_style + container_content1, unsafe_allow_html=True)
            #st.sidebar.markdown("<h3 style='text-align: center;'>Comparaison des paramètres dans la même unité: </h3>", unsafe_allow_html=True)
        
            phase_to_compare = []

            unity_to_compare = st.sidebar.radio('Unité :',
                                    [
                                        "QT",
                                        "ESLI",
                                        "ION",
                                        "MCT"])
            try:
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

                Comparaison_des_phases_de_traitement(uploaded_file,[unity_to_compare, phase_to_compare, param_to_compare]) 
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
        else:
            # container_content2 = """
            # <h3 style='text-align: center;'>Comparaison des unitées:</h3>
            # </div>
            # """
            # st.sidebar.markdown(container_style + container_content2, unsafe_allow_html=True)
            unity_to_compare1 = st.sidebar.multiselect('Unité:',
                                    [
                                        "QT",
                                        "ESLI",
                                        "ION",
                                        "MCT"])
            try:
                phase_traitement = {}
                paramètre = {}
                for i in range(len(unity_to_compare1)):
                    if unity_to_compare1[i]  == "MCT":
                        phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.radio(f"phase de traitement de {unity_to_compare1[i]}",
                                            [
                                            "intake",
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                    elif unity_to_compare1[i]  == "ION":
                        phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.radio(f"phase de traitement de {unity_to_compare1[i]}",
                                            [
                                            "intake",
                                            "PERMEAT FILTRATION",
                                            "Bac_stockage",
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                    elif unity_to_compare1[i]  == "QT":
                        phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.radio(f"phase de traitement de {unity_to_compare1[i]}",
                                            [
                                            "intake",
                                            "PERMEAT FILTRATION",
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            "sortie_global"])
                    elif unity_to_compare1[i]  == "ESLI":
                        phase_traitement[f"{unity_to_compare1[i]}"] = st.sidebar.radio(f"phase de traitement de {unity_to_compare1[i]}",
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
    elif don == "Laboratoire & Operationnelles":
        unity = st.sidebar.radio('Unity:',
                                        [
                                        'QT',
                                        'ESLI',
                                        'MCT'
                                        ])
        if unity == "QT":
            try:
                sheets =["UF","FC","RO"]
                data_opertionel = {}
                for sheet in sheets:
                    data_opertionel[sheet] = pd.read_excel('Suivi contrôle qualité d\'eau de dessalement QT 13-08-2024.xlsx',sheet_name=sheet)
                phase_op = st.sidebar.radio("Phase operationnelle:",["UF","FC","RO"])
                phase_labo = st.sidebar.radio('Phase laboratoire:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            'sortie_global'])
                if phase_op != "options":
                    para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel[phase_op].columns[1:])
                if phase_labo != "options":
                    para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"QT_{phase_labo}"].columns[1:])
                labo_oper(data,data_opertionel,f"QT_{phase_labo}",phase_op,para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif unity =="ESLI":
            try:
                data_opertionel = {}
                data_opertionel["UF"] = pd.read_excel('Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name="UF")
                phase_labo = st.sidebar.selectbox('Phase laboratoire:',
                                            ['Options',
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                
                para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel["UF"].columns[1:])
                if phase_labo != "options":
                    para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"QT_{phase_labo}"].columns[1:])
                labo_oper1(data,data_opertionel,f"ESLI_{phase_labo}",para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif unity =="MCT":
            try:
                data_opertionel = {}
                data_opertionel["tr"] = pd.read_excel('SUIVI DP et Q et CIP des RO  MCT 13-08-2024.xlsx',sheet_name="tr")
                phase_labo = st.sidebar.selectbox('Phase laboratoire:',
                                            ['Options',
                                            'intake',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                
                para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel["tr"].columns[1:])
                if phase_labo != "options":
                    para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"MCT_{phase_labo}"].columns[1:])
                labo_oper2(data,data_opertionel,f"MCT_{phase_labo}",para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True) 
    elif don  == "Operationnelles":
        unity = st.sidebar.radio('Unité:',
                                        [
                                        'QT',
                                        'ESLI',
                                        'MCT'
                                        ])
        data_opertionel = {}
        if unity == 'QT':
            sheets =["UF","FC","RO"]
            for sheet in sheets:
                data_opertionel[sheet] = pd.read_excel('Suivi contrôle qualité d\'eau de dessalement QT 13-08-2024.xlsx',sheet_name=sheet)
            phase_op = st.sidebar.radio("Phase:",["UF","FC","RO"])
            vis_op(data_opertionel,phase_op)
        elif unity == 'ESLI':
            sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
            for sheet in sheets:
                data_opertionel[sheet] = pd.read_excel('Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
            phase_op = st.sidebar.radio("phases operationnelles:",["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
            vis_op(data_opertionel,phase_op)
        elif unity =="MCT":
            data_opertionel["tr"] = pd.read_excel('SUIVI DP et Q et CIP des RO  MCT 13-08-2024.xlsx',sheet_name="tr")
            phase_op = "tr"
            vis_op(data_opertionel,phase_op)

else:
    st.markdown('<div class="centered">Veuillez charger un fichier bien adapter pour commencer.</div>', unsafe_allow_html=True)