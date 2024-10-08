import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO
import plotly.express as px
import json

from fonctions import Visualisation_des_paramètres,Comparaison_des_phases_de_traitement,unity_compare
from fonctions import labo_oper,labo_oper1,labo_oper2,vis_op,compare_op,compar_unity_op,visualisation_volume,visualisation_volume_op,send_notification
#--------------------------------------------------heradr-------------------------------------------------------------

st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")

def image_to_base64(image_path):
    img = Image.open(image_path)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

logo_path = "static/logo.png"  
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

uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx", "xls"])

#---------------------------------------------Chargement des données-----------------------------------------------------

if uploaded_file is not None:
    st.markdown("<p style='text-align: center;'>Fichier téléchargé avec succès!</p>",unsafe_allow_html=True)
    sheets =["QT_intake","QT_PERMEAT FILTRATION","QT_APRES FILTRES A CARTOUCHE","QT_PERMEAT RO","QT_sortie_global",
        "ESLI_intake","ESLI_PERMEAT FILTRATION", "ESLI_APRES FILTRES A CARTOUCHE","ESLI_PERMEAT RO",
        "ION_intake","ION_PERMEAT FILTRATION","ION_Bac_stockage","ION_APRES FILTRES A CARTOUCHE","ION_PERMEAT RO",
        "MCT_intake","MCT_APRES FILTRES A CARTOUCHE","MCT_PERMEAT RO"]
    data = {}
    for sheet in sheets:
            data[sheet] = pd.read_excel(uploaded_file,sheet_name=sheet)
#----------------------------------------------------body-----------------------------------------------------------------
    don = st.sidebar.radio('Données:',
                                    [
                                        "Laboratoire",
                                        "Paramètres de marche",
                                        "Laboratoire & Paramètres de marche",
                                        "Volume produit"
                                        ])
    if  don == "Laboratoire":
        don1 = st.sidebar.radio('Visualisation:',
                                    [
                                        "Visualisation des paramètres",
                                        "Comparaison des phases de traitement",
                                        "Comparaison des unitées"
                                        ])       
        if don1 == "Visualisation des paramètres":
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
                df = pd.read_excel(uploaded_file,sheet_name="QT_intake")
                col1,col2 = st.columns((2))
                df['date'] = pd.to_datetime(df['date'])

                startDate = pd.to_datetime(df["date"]).min()
                endDate = pd.to_datetime(df["date"]).max()

                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("Start Date", startDate))
                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("End Date", endDate))

                if st.sidebar.button("Apply"):
                    Visualisation_des_paramètres(uploaded_file,unity,phase,date1,date2)         
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif don1 == "Comparaison des phases de traitement":          
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
                col1,col2 = st.columns((2))
                startDate = pd.to_datetime(data["QT_intake"]["date"]).min()
                endDate = pd.to_datetime(data["QT_intake"]["date"]).max() 
                
                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("Start date: ", startDate))

                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("End date:", endDate))  
                graphique = st.sidebar.selectbox('Type du graphique :',
                    ['Graphique à barres','Graphique en lignes','Graphique en aires','Graphique à points']) 
                if st.sidebar.button("Apply"):
                    Comparaison_des_phases_de_traitement(uploaded_file,[unity_to_compare, phase_to_compare, param_to_compare],date1,date2,graphique) 
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
        else:
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
                col1,col2 = st.columns((2))
                startDate = pd.to_datetime(data["QT_intake"]["date"]).min()
                endDate = pd.to_datetime(data["QT_intake"]["date"]).max() 
                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("de: ", startDate))

                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("à: ", endDate)) 
   
                if st.sidebar.button("Apply"):
                    unity_compare(uploaded_file,unity_to_compare1,phase_traitement,paramètre,date1,date2)
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
    elif don == "Laboratoire & Paramètres de marche":
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
                    data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT.xlsx',sheet_name=sheet)
                phase_op = st.sidebar.radio("Phase operationnelle:",["UF","FC","RO"])
                phase_labo = st.sidebar.radio('Phase laboratoire:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO',
                                            'sortie_global'])
                
                para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel[phase_op].columns[1:])
                para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"QT_{phase_labo}"].columns[1:])
                if st.sidebar.button("Apply"):
                    labo_oper(data,data_opertionel,f"QT_{phase_labo}",phase_op,para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif unity =="ESLI":
            try:
                sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
                data_opertionel = {}
                for sheet in sheets:
                    data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
                phase_op = st.sidebar.radio("Phase operationnelle:",["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
                phase_labo = st.sidebar.radio('Phase laboratoire:',
                                            [
                                            'intake',
                                            'PERMEAT FILTRATION',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                
                para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel[phase_op].columns[1:])
                para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"ESLI_{phase_labo}"].columns[1:])
                if st.sidebar.button("Apply"):
                    labo_oper(data,data_opertionel,f"ESLI_{phase_labo}",phase_op,para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)  
        elif unity =="MCT":
            try:
                data_opertionel = {}
                data_opertionel["tr"] = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT.xlsx',sheet_name="tr")
                phase_labo = st.sidebar.radio('Phase laboratoire:',
                                            [
                                            'intake',
                                            'APRES FILTRES A CARTOUCHE',
                                            'PERMEAT RO'])
                
                para_op = st.sidebar.selectbox("paramètres operationels:",data_opertionel["tr"].columns[1:])

                para_labo = st.sidebar.selectbox("paramètres laboratoire:",data[f"MCT_{phase_labo}"].columns[1:])
                if st.sidebar.button("Apply"):
                    labo_oper2(data,data_opertionel,f"MCT_{phase_labo}",para_labo,para_op)
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True) 
    elif don  == "Paramètres de marche":
        don1 = st.sidebar.radio('Visualisation:',
                                    [
                                        "Visualisation des paramètres",
                                        "Comparaison des phases de traitement",
                                        "Comparaison des unitées"
                                        ])       
        if don1 == "Visualisation des paramètres":
            unity = st.sidebar.radio('Unité:',
                                            [
                                                "QT",
                                                "ESLI",
                                                "MCT"])
            data_opertionel = {}
            try:
                if (unity == "MCT"):
                    data_opertionel["tr"] = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT.xlsx',sheet_name="tr")
                    phase = st.sidebar.radio('Phase:',
                                            ["tr"])
                    df = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT.xlsx',sheet_name="tr")
                elif  (unity == "QT"):
                    sheets =["UF","FC","RO"]
                    for sheet in sheets:
                     data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT.xlsx',sheet_name=sheet)
                    phase = st.sidebar.radio('Phase:',
                                            ["UF","FC","RO"]
                                            )
                    df = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT.xlsx',sheet_name="UF")
                elif(unity == "ESLI"):
                    sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
                    for sheet in sheets:
                        data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
                    phase = st.sidebar.radio('Phase:',
                                           ["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
                    df = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name="UF")
                

                col1,col2 = st.columns((2))

                startDate = pd.to_datetime(df["date"]).min()
                endDate = pd.to_datetime(df["date"]).max()

                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("Start Date", startDate))

                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("End Date", endDate))

                if st.sidebar.button("Apply"):
                    vis_op(data_opertionel,phase,date1,date2) 
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True) 
        elif  don1 == "Comparaison des phases de traitement":
            unity = st.sidebar.radio('Unité:',
                                            [
                                                "QT",
                                                "ESLI",
                                                "MCT"]) 
            data_opertionel = {}
            try:
                if (unity == "MCT"):
                    data_opertionel["tr"] = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT 27-08-2024.xlsx',sheet_name="tr")
                    phase = st.sidebar.multiselect('Phase:',
                                            ["tr"])
                elif  (unity == "QT"):
                    sheets =["UF","FC","RO"]
                    for sheet in sheets:
                        data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT 27-08-2024.xlsx',sheet_name=sheet)
                    phase = st.sidebar.multiselect('Phase:',
                                            ["UF","FC","RO"]
                                            )
                elif(unity == "ESLI"):
                    sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
                    for sheet in sheets:
                        data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
                    phase = st.sidebar.multiselect('Phase:',
                                           ["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
                    
                param_to_compare = {}

                if phase:
                    for j in range(len(phase)):  
                        param_to_compare[f"{phase[j]}"] = st.sidebar.multiselect(f'paramètres d\'{phase[j]}',
                                            data_opertionel[f"{phase[j]}"].columns[1:])
                df = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT.xlsx',sheet_name="FC")

                col1,col2 = st.columns((2))
                df['date'] = pd.to_datetime(df['date'])

                startDate = pd.to_datetime(df["date"]).min()
                endDate = pd.to_datetime(df["date"]).max()

                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("Start Date", startDate))

                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("End Date", endDate))

                if st.sidebar.button("Apply"):
                    compare_op(data_opertionel,phase,param_to_compare,date1,date2) 
            except Exception as e:
                 st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)                        
        else:
            unity_to_compare = st.sidebar.multiselect('Unité:',
                                    [
                                        "QT",
                                        "ESLI",
                                        "MCT"])
            try:
                data_opertionel={}
                phase_traitement = {}
                paramètre = {}
                for i in range(len(unity_to_compare)):
                    if unity_to_compare[i]  == "MCT":
                        data_opertionel[f"{unity_to_compare[i]}_tr"] = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT 27-08-2024.xlsx',sheet_name="tr")
                        phase_traitement[f"{unity_to_compare[i]}"] = st.sidebar.radio(f"phases de {unity_to_compare[i]}",
                                            [
                                            "tr"
                                        ])
                    elif unity_to_compare[i]  == "QT":
                        sheets =["UF","FC","RO"]
                        for sheet in sheets:
                            data_opertionel[f"{unity_to_compare[i]}_{sheet}"] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT 27-08-2024.xlsx',sheet_name=sheet)
                        phase_traitement[f"{unity_to_compare[i]}"] = st.sidebar.radio(f"phases de {unity_to_compare[i]}",
                                          ["UF","FC","RO"])
                    else:
                        sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
                        for sheet in sheets:
                             data_opertionel[f"{unity_to_compare[i]}_{sheet}"] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
                        phase_traitement[f"{unity_to_compare[i]}"] = st.sidebar.radio(f"phases de {unity_to_compare[i]}",
                                            [
                                           "UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
    
                    paramètre[f"{unity_to_compare[i]}_{phase_traitement[unity_to_compare[i]]}"] = st.sidebar.multiselect(f"paramètres de {unity_to_compare[i]}_{phase_traitement[unity_to_compare[i]]}",
                                                                                            data_opertionel[f"{unity_to_compare[i]}_{phase_traitement[unity_to_compare[i]]}"].columns[1:])
                col1,col2 = st.columns((2))
                startDate = pd.to_datetime(data["QT_intake"]["date"]).min()
                endDate = pd.to_datetime(data["QT_intake"]["date"]).max() 
                with col1:
                    date1 = pd.to_datetime(st.sidebar.date_input("de: ", startDate))

                with col2:
                    date2 = pd.to_datetime(st.sidebar.date_input("à: ", endDate)) 
   
                if st.sidebar.button("Apply"):
                    compar_unity_op(data_opertionel,unity_to_compare,phase_traitement,paramètre,date1,date2)
            except Exception as e:
                st.markdown(f"<h3 style='text-align: center;color:red;'></h3>", unsafe_allow_html=True)
    else:
        don = st.sidebar.radio('Visualisation:',
                                    [
                                        "Volume produit (m3)",
                                        "Volume & Paramètres de marche",
                                        ])      
        df = pd.read_excel('data/Copie de Résultat de Production et TRG - Eau Dessalement Mobile et Fixe au   25 08 2024.xlsb .xlsx',sheet_name="Volume")
        
        if don == "Volume produit (m3)":
            df = pd.read_excel('data/Copie de Résultat de Production et TRG - Eau Dessalement Mobile et Fixe au   25 08 2024.xlsb .xlsx',sheet_name="Volume")
            col1,col2 = st.columns((2))
        
            startDate = pd.to_datetime(df["Date"]).min()
            endDate = pd.to_datetime(df["Date"]).max()

            with col1:
                date1 = pd.to_datetime(st.sidebar.date_input("Start Date", startDate))

            with col2:
                date2 = pd.to_datetime(st.sidebar.date_input("End Date", endDate))
            if st.sidebar.button("Aply"):
                visualisation_volume(df,date1,date2)
        elif don == "Volume & Paramètres de marche":
            df = pd.read_excel('data/Copie de Résultat de Production et TRG - Eau Dessalement Mobile et Fixe au   25 08 2024.xlsb .xlsx',sheet_name="Volume")
            data_opertionel={}
            unity_to_compare = st.sidebar.radio('Unité:',
                                            [
                                            "QT",
                                            "ESLI",
                                            "ION",
                                            "MCT"
                                            ])
            if (unity_to_compare == "MCT"):
                data_opertionel["tr"] = pd.read_excel('data/SUIVI DP et Q et CIP des RO  MCT.xlsx',sheet_name="tr")
                phase = st.sidebar.radio('Phase:',
                                        ["tr"])
            elif  (unity_to_compare == "QT"):
                sheets =["UF","FC","RO"]
                for sheet in sheets:
                    data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement QT.xlsx',sheet_name=sheet)
                phase = st.sidebar.radio('Phase:',
                                        ["UF","FC","RO"]
                                        )
            elif(unity_to_compare == "ESLI"):
                sheets =["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"]
                for sheet in sheets:
                    data_opertionel[sheet] = pd.read_excel('data/Suivi contrôle qualité d\'eau de dessalement ESLI.xlsx',sheet_name=sheet)
                phase = st.sidebar.radio('Phase:',
                                        ["UF","FC","RO ZONE A","RO ZONE B","RO ZONE C"])
            paramètre = st.sidebar.selectbox(f"paramètres de {unity_to_compare}_{phase}",
                                                                                           data_opertionel[phase].columns[1:])
            
            volume = st.sidebar.selectbox('Volume produit (m3):',
                                            df.columns[1:]) 
            if st.sidebar.button("Aply"):
                visualisation_volume_op(data_opertionel,df,phase,volume,paramètre)
    df = pd.read_excel(uploaded_file,sheet_name="QT_intake")  
    with open('config.json') as json_file:
        gmail_cfg = json.load(json_file)      
    # send_notification(df,40,'Cond. (mS/cm) à 25° C',gmail_cfg) 
else:
    st.markdown('<div class="centered">Veuillez charger un fichier bien adapter pour commencer.</div>', unsafe_allow_html=True)
