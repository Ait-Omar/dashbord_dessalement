import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components


def filter(unity,phase):
    #filtrage selon l'unité QT
    if (unity == "QT") & (phase =="Avant filtraion fine"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_avant")

        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turbidité moyenne: {np.around(df['Turb'].mean(),2)} NTU</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=5.13, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Condectivté moyenne: {np.around(df['Cond. (mS/cm) à 25° C'].mean(),2)} mS/cm</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cond. (mS/cm) à 25° C")
            fig.add_hline(y=55, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES moyen: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES")
            fig.add_hline(y=10, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "QT") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_PF")

        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI 15 P1 moyen: {np.around(df['SDI 15 P1'].mean(),2)}</h2>", unsafe_allow_html=True)        
            fig = px.line(df,x="date",y="SDI 15 P1")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI 15 P2 moyen: {np.around(df['SDI 15 P2'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI 15 P2")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb P1 moyenne: {np.around(df['Turb P1'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb P1")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb P2 moyenne: {np.around(df['Turb P1'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb P2")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES moyenne: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES")
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "QT") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx', sheet_name="QT_après")
        df['date'] = pd.to_datetime(df['date'])

        # Définir les dates minimales et maximales
        startDate = df['date'].min()
        endDate = df['date'].max()

        # Créer les colonnes pour la sélection des dates
        col1, col2 = st.columns(2)

        with col1:
            date1 = st.date_input("Start Date", startDate)

        with col2:
            date2 = st.date_input("End Date", endDate)

        # Filtrer les données en fonction des dates sélectionnées
        df = df[(df['date'] >= pd.to_datetime(date1)) & (df['date'] <= pd.to_datetime(date2))]

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(), 2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)

  
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(), 2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)

        # Visualiser PO43- avec coloration conditionnelle
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-: {np.around(df['PO43-'].mean(), 2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-")
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)

        # Visualiser SDI15 avec coloration conditionnelle
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 moyen: {np.around(df['SDI15'].mean(), 2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)

        # Visualiser TDS avec coloration conditionnelle
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TDS moyen: {np.around(df['TDS'].mean(), 2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS")
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "QT") & (phase =="Perméat RO"): 
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_PRO")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond </h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['Cond. (µS/cm) A','Cond. (µS/cm) B',
            'Cond. (µS/cm) C', 'Cond. (µS/cm) D', 'Cond. (µS/cm) E',
            'Cond. (µS/cm) F', 'Cond. (µS/cm) G', ' Cond. (µS/cm) H'])
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    #filtrage selon l'unité ESLI
    elif (unity == "ESLI") & (phase =="Avant filtraion fine"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_avant")

        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)} </h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=5.13, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Fe3+ moyenne: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Fe3+")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES")
            fig.add_hline(y=10, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_PF")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        st.markdown("<h2 style='text-align: center;'>SDI15</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['SDI 15 ZONE A',' SDI 15 Zone B', 'SDI 15 Zone C'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Turb Zone A','Turb Zone B','Turb Zone C'])
        st.plotly_chart(fig,use_container_width=True,height = 200)
    
        st.markdown(f"<h2 style='text-align: center;'>MES moyenne: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="MES")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_après")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond moyenne: {np.around(df['Cond'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cond")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43- moyen: {np.around(df['PO43-'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-")
            fig.add_hline(y=0.0, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 moyen: {np.around(df['SDI15'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TDS moyenne: {np.around(df['TDS'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS")
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Perméat RO"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_PRO")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        st.markdown("<h2 style='text-align: center;'>Cond</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Cond. (µS/cm) A1','Cond. (µS/cm) A2',
       'Cond. (µS/cm) A3', 'Cond. (µS/cm) A4', 'Cond. (µS/cm) B1',
       'Cond. (µS/cm) B2', 'Cond. (µS/cm) B3', 'Cond. (µS/cm) B4',
       'Cond. (µS/cm) C1', 'Cond. (µS/cm) C2', 'Cond. (µS/cm) C3',
       'Cond. (µS/cm) C4'])
        fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
        st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    #filtrage selon l'unité ION EXCHANGE
    elif (unity == "ION EXCHANGE") & (phase =="Avant filtraion fine"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ION_avant")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['pH Entrée A,B,C,D,E', 'pH Entrée F,G,H,I,J'])
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['Turb (NTU)Entrée A,B,C,D,E', 'Turb (NTU)Entrée F,G,H,I,J'])
            fig.add_hline(y=5.13, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe2+</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['Fe2+ (mg/l)Entrée A,B,C,D,E', 'Fe2+ (mg/l)Entrée F,G,H,I,J'])
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe3+</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['Fe3+ (mg/l)Entrée A,B,C,D,E', 'Fe3+ (mg/l)Entrée F,G,H,I,J'])
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES moyenne: {np.around(df['MES (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES (mg/l)")
            fig.add_hline(y=10, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ION EXCHANGE") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ION_PF")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['DATE'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]

        st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Turb Collecteur ', 'Turb HMMF \nA', 'Turb HMMF \nB', 'Turb HMMF \nC',
       'Turb HMMF \nD', 'Turb HMMF \nE', 'Turb HMMF \nF', 'Turb HMMF \nG',
       'Turb HMMF \nH', 'Turb HMMF \nI', 'Turb HMMF \nJ'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Fe3+ moyenne:{np.around(df['Fe3+ (mg/l)'].mean(),2)} mg/l </h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Fe3+ (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES moyenne: {np.around(df['MES (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ION EXCHANGE") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ION_après")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)} </h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(F"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
            
        with col1:
            st.markdown(F"<h2 style='text-align: center;'>PO43- moyen: {np.around(df['PO43-'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-")
            fig.add_hline(y=0.0, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(F"<h2 style='text-align: center;'>TDS moyenne: {np.around(df['TDS'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS")
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>SDI15</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['SDI15 A,B,C,D', 'SDI15 E,F,G,H'])
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe3+</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=['Fe3+ (mg/l) A,B,C,D', 'Fe3+ (mg/l) E,F,G,H'])
            st.plotly_chart(fig,use_container_width=True,height = 200)            
    elif (unity == "ION EXCHANGE") & (phase =="Perméat RO"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ION_PRO")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)  
        st.markdown("<h2 style='text-align: center;'>Cond</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Cond. (µS/cm) A', 'Cond. (µS/cm) B',
        'Cond. (µS/cm) C', 'Cond. (µS/cm) D', 'Cond. (µS/cm) E',
        'Cond. (µS/cm) F', 'Cond. (µS/cm) G', 'Cond. (µS/cm) H'])
        fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
        st.plotly_chart(fig,use_container_width=True,height = 200) 

def rendement_mes(data):
    Mes_QT = ((data['QT_avant']['MES']-data['QT_PF']['MES'])/data['QT_avant']['MES']).mean()*100
    Mes_ESLI = ((data['ESLI_avant']['MES']-data['ESLI_PF']['MES'])/data['ESLI_avant']['MES']).mean()*100
    Mes_ION = ((data['ION_avant']['MES (mg/l)']-data['ION_PF']['MES (mg/l)'])/data['ION_avant']['MES (mg/l)']).mean()*100

    np.random.seed(42)
    rd =[Mes_QT,Mes_ESLI,Mes_ION]
    data = {
        'Yield': rd,
        'unity': ["QT","ESLI","ION"]
    }
    df = pd.DataFrame(data)



    # Création de l'histogramme avec des labels
    fig = px.bar(df, x='unity', y='Yield')

    fig.update_layout(
        width=800,  # largeur en pixels
        height=600  # hauteur en pixels
    )
    plot_html = fig.to_html(full_html=False)

    # Utiliser HTML et CSS pour centrer le graphique
    html_string = f"""
    <div style="display: flex; justify-content: center;">
        {plot_html}
    </div>
    """
    components.html(html_string, height=600)

def rendement_PO43(data):
    po4_QT = (data['QT_après']['PO43-'].mean())
    po4_ESLI = (data['ESLI_après']['PO43-'].mean())
    po4_ION = (data['ION_après']['PO43-'].mean())

    np.random.seed(42)
    rd =[po4_QT,po4_ESLI,po4_ION]
    data = {
        'Yield': rd,
        'unity': ["QT","ESLI","ION"]
    }
    df = pd.DataFrame(data)



    # Création de l'histogramme avec des labels
    fig = px.bar(df, x='unity', y='Yield')

    fig.update_layout(
        width=800,  # largeur en pixels
        height=600  # hauteur en pixels
    )
    plot_html = fig.to_html(full_html=False)

    # Utiliser HTML et CSS pour centrer le graphique
    html_string = f"""
    <div style="display: flex; justify-content: center;">
        {plot_html}
    </div>
    """
    components.html(html_string, height=600)    

def rendement_Turb(data):
    Turb_QT = data['QT_avant']['Turb'].mean()/data['QT_PRO']['Turb'].mean()
    Turb_ESLI = data['ESLI_avant']['Turb'].mean()/data['ESLI_PRO']['Turb'].mean()
    Turb_ION = ((data['ION_avant']['Turb (NTU)Entrée A,B,C,D,E'].mean()+data['ION_avant']['Turb (NTU)Entrée A,B,C,D,E'].mean())/2)/data['ION_PRO']['Turb'].mean()

    np.random.seed(42)
    rd =[Turb_QT,Turb_ESLI,Turb_ION]
    data = {
        'Yield': rd,
        'unity': ["QT","ESLI","ION"]
    }
    df = pd.DataFrame(data)



    # Création de l'histogramme avec des labels
    fig = px.bar(df, x='unity', y='Yield')

    fig.update_layout(
        width=800,  # largeur en pixels
        height=600  # hauteur en pixels
    )
    plot_html = fig.to_html(full_html=False)

    # Utiliser HTML et CSS pour centrer le graphique
    html_string = f"""
    <div style="display: flex; justify-content: center;">
        {plot_html}
    </div>
    """
    components.html(html_string, height=600) 