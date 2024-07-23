import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np


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
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turbidité moyenne: {np.around(df['Turb'].mean(),2)} NTU</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Condectivté moyenne: {np.around(df['Cond. (mS/cm) à 25° C'].mean(),2)} mS/cm</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cond. (mS/cm) à 25° C")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES moyen: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES")
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
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_après")
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
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-: {np.around(df['PO43-'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 moyen: {np.around(df['SDI15'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TDS moyenne: {np.around(df['TDS'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS")
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
        st.markdown("<h2 style='text-align: center;'>Cond </h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Cond. (µS/cm) A','Cond. (µS/cm) B',
        'Cond. (µS/cm) C', 'Cond. (µS/cm) D', 'Cond. (µS/cm) E',
        'Cond. (µS/cm) F', 'Cond. (µS/cm) G', ' Cond. (µS/cm) H'])
        st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb moyenne: {np.around(df['Turb'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
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
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb \n(NTU)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe3+</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Fe3+\n (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>MES</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES \n(mg/l)")
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
    
        st.markdown("<h2 style='text-align: center;'>MES</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="MES\n (mg/l)")
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
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cond. (mS/cm)\nà 25° C")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb\n(NTU)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>PO43-</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-  \n(mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>SDI15</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>TDS</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS\n(mg/l)")
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
        st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb\n(NTU)")
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
     
        st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['pH Entrée A,B,C,D,E', 'pH Entrée F,G,H,I,J'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Turb (NTU)Entrée A,B,C,D,E', 'Turb (NTU)Entrée F,G,H,I,J'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        st.markdown("<h2 style='text-align: center;'>Fe2+</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Fe2+ (mg/l)Entrée A,B,C,D,E', 'Fe2+ (mg/l)Entrée F,G,H,I,J'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        st.markdown("<h2 style='text-align: center;'>Fe3+</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Fe3+ (mg/l)Entrée A,B,C,D,E', 'Fe3+ (mg/l)Entrée F,G,H,I,J'])
        st.plotly_chart(fig,use_container_width=True,height = 200)

        st.markdown("<h2 style='text-align: center;'>MES</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="MES (mg/l)")
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
            st.markdown("<h2 style='text-align: center;'>Fe3+ </h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Fe3+ (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col2:
            st.markdown("<h2 style='text-align: center;'>MES</h2>", unsafe_allow_html=True)
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

        st.markdown("<h2 style='text-align: center;'>SDI15</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['SDI15 A,B,C,D', 'SDI15 E,F,G,H'])
        st.plotly_chart(fig,use_container_width=True,height = 200)
        
        st.markdown("<h2 style='text-align: center;'>Fe3+</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Fe3+ (mg/l) A,B,C,D', 'Fe3+ (mg/l) E,F,G,H'])
        st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb\n(NTU)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
            
        with col1:
            st.markdown("<h2 style='text-align: center;'>PO43-</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-  \n(mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>TDS</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TDS\n(mg/l)")
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
        st.markdown("<h2 style='text-align: center;'>Cond</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y=['Cond. (µS/cm) A', 'Cond. (µS/cm) B',
       'Cond. (µS/cm) C', 'Cond. (µS/cm) D', 'Cond. (µS/cm) E',
       'Cond. (µS/cm) F', 'Cond. (µS/cm) G', 'Cond. (µS/cm) H'])
        st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb\n(NTU)")
            st.plotly_chart(fig,use_container_width=True,height = 200)   



   