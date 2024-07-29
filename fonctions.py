import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components


def filter(unity,phase):
    #filtrage selon l'unité QT
    if (unity == "QT") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_PF")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de Pelevement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) moyenne: {np.around(df['Turb (NTU)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb (NTU)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SiO2 (mg/l) moyenne: {np.around(df['SiO2 (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SiO2 (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES  (mg/l) moyenne: {np.around(df['MES (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI 15 moyenne: {np.around(df['SDI 15'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI 15")
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "QT") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_après")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de Pelevement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].replace('<3',1)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].replace(0,1)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].astype(float)
        df.loc[df['TOC (mg/l)'] > 3, 'TOC (mg/l)'] = 0

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyenne: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) moyenne: {np.around(df['PO43-  (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-  (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'> ORP (mV) P1 moyenne: {np.around(df[' ORP (mV) P1'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=" ORP (mV) P1")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) P2 moyenne: {np.around(df['ORP (mV) P2'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="ORP (mV) P2")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 moyenne: {np.around(df['SDI15'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) moyenne: {np.around(df['TOC (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TOC (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)        
    elif (unity == "QT") & (phase =="Perméat RO"): 
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_PRO")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de Pelevement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond D</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond D')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond F</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond F')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond G</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond G')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond H</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond H')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>pH B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>pH D</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH D')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>pH F</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH F')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH G</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH G')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>pH H</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH H')
            st.plotly_chart(fig,use_container_width=True,height = 200)

    #filtrage selon l'unité ESLI
    if (unity == "ESLI") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_PF")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de prélèvement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe2+ (mg/l) Zone A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe3+ (mg/l) Zone A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>MES (mg/l) Zone A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>SDI15 Zone A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe2+ (mg/l) Zone B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe3+ (mg/l) Zone B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>MES (mg/l) Zone B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>SDI15 Zone B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe2+ (mg/l) Zone C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe3+ (mg/l) Zone C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>MES (mg/l) Zone C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>SDI15 Zone C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_après")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de prélèvement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))

        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>T (°C)  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>ORP (mV)  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>SDI15  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>TDS (mg/l)  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
            st.markdown("<h2 style='text-align: center;'>pH ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH  ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>T (°C)  ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C) ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>ORP (mV)  ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>SDI15  ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>TDS (mg/l)  ZONE B</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
            st.markdown("<h2 style='text-align: center;'>pH ZONE C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>T (°C)  ZONE C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C) ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>ORP (mV)  ZONE A</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>SDI15  ZONE C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>TDS (mg/l)  ZONE C</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Perméat RO"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ESLI_PRO")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de prélèvement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond A1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond A2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond A3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond A4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond B1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond B2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond B3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond B4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond C1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond C2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Cond C3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Cond C4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph A1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph A2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph A3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph A4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph B1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph B2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph b2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph B3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph B4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph C1</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph C2</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Ph C3</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Ph C4</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
    #filtrage selon l'unité ION EXCHANGE
    if (unity == "ION EXCHANGE") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="ION_PF")
        print(df.columns)
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de prelevement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH HMMF A,B,C,D,E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH HMMF A,B,C,D,E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe2+ (mg/l) HMMF A,B,C,D,E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) HMMF A,B,C,D,E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe3+ (mg/l) HMMF A,B,C,D,E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) HMMF A,B,C,D,E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>ORP (mV) HMMF A,B,C,D,E</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) HMMF A,B,C,D,E')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>pH HMMF F,G,H,I,J</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH HMMF F,G,H,I,J')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>Fe2+ (mg/l) HMMF F,G,H,I,J</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) HMMF F,G,H,I,J')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown("<h2 style='text-align: center;'>Fe3+ (mg/l) HMMF F,G,H,I,J</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) HMMF F,G,H,I,J')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown("<h2 style='text-align: center;'>ORP (mV) HMMF F,G,H,I,J</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) HMMF F,G,H,I,J')
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
        fig.add_hline(y=450, line_dash="dash", line_color="white", line_width=2)
        st.plotly_chart(fig,use_container_width=True,height = 200) 
    # filtrage selon l'unité MCT
    if (unity == "MCT") & (phase =="Perméat filtration"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="MCT_PF")

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
    elif (unity == "MCT") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel('DATA/data préparé.xlsx', sheet_name="MCT_après")
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
    elif (unity == "MCT") & (phase =="Perméat RO"): 
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="MCT_PRO")
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
    elif(phase == "intake"):
        df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="intake")
        print(df.columns)
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['Date de prelevement'])

        startDate = pd.to_datetime(df["date"]).min()
        endDate = pd.to_datetime(df["date"]).max()

        with col1:
            date1 = pd.to_datetime(st.date_input("Start Date", startDate))

        with col2:
            date2 = pd.to_datetime(st.date_input("End Date", endDate))
        df = df[(df["date"] >= date1) & (df["date"] <= date2)]
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].replace('<3',1)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].replace(0,1)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].astype(float)
        df.loc[df['TOC (mg/l)'] > 3, 'TOC (mg/l)'] = 0
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43- (mg/l) moyen: {np.around(df['PO43- (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)        
            fig = px.line(df,x="date",y="PO43- (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SiO2 (mg/l) moyen: {np.around(df['SiO2 (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SiO2 (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) moyenne: {np.around(df['TOC (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TOC (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES  (mg/l) moyenne: {np.around(df['MES  (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES  (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cl2 libre (mg/l) moyenne: {np.around(df['Cl2 libre (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cl2 libre (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)

         
def rendement_mes(data):
    Mes_QT = ((data['QT_avant']['MES']-data['QT_PF']['MES'])/data['QT_avant']['MES']).mean()*100
    Mes_ESLI = ((data['ESLI_avant']['MES']-data['ESLI_PF']['MES'])/data['ESLI_avant']['MES']).mean()*100
    Mes_ION = ((data['ION_avant']['MES (mg/l)']-data['ION_PF']['MES (mg/l)'])/data['ION_avant']['MES (mg/l)']).mean()*100

    np.random.seed(42)
    rd =[Mes_QT,Mes_ESLI,Mes_ION]
    data = {
        'unity': ["QT","ESLI","ION"],
        'Yield': rd
    }
    df = pd.DataFrame(data)


    # Sélection des catégories à afficher dans le pie chart
    selected_categories = st.multiselect('Sélectionnez les Unité à inclure dans le graphique :', options=df['unity'].unique(), default=df['unity'].unique())

    # Filtre les données en fonction des catégories sélectionnées
    filtered_df = df[df['unity'].isin(selected_categories)]

    # Crée le pie chart avec Plotly
    fig = px.pie(filtered_df, names='unity', values='Yield', title='Répartition des valeurs par catégorie')
    fig.update_layout(title={'text': 'Répartition des rendements par unity', 'x': 0.36})
# Affiche le pie chart avec Streamlit
    st.plotly_chart(fig)

def rendement_PO43(data):
    po4_QT = (data['QT_après']['PO43-'].mean())
    po4_ESLI = (data['ESLI_après']['PO43-'].mean())
    po4_ION = (data['ION_après']['PO43-'].mean())

    np.random.seed(42)
    rd =[po4_QT,po4_ESLI,po4_ION]
    data = {
        'unity': ["QT","ESLI","ION"],
        'Yield': rd
    }
    df = pd.DataFrame(data)


    # Sélection des catégories à afficher dans le pie chart
    selected_categories = st.multiselect('Sélectionnez les Unité à inclure dans le graphique :', options=df['unity'].unique(), default=df['unity'].unique())

    # Filtre les données en fonction des catégories sélectionnées
    filtered_df = df[df['unity'].isin(selected_categories)]

    # Crée le pie chart avec Plotly
    fig = px.pie(filtered_df, names='unity', values='Yield', title='Répartition des valeurs par catégorie')
    fig.update_layout(title={'text': 'Répartition des rendements par unity', 'x': 0.36})
# Affiche le pie chart avec Streamlit
    st.plotly_chart(fig)
def rendement_Turb(data):
    Turb_QT = ((data['QT_avant']['Turb']-data['QT_PRO']['Turb'])/data['QT_avant']['Turb']).mean()
    Turb_ESLI = ((data['ESLI_avant']['Turb']-data['ESLI_PRO']['Turb'])/data['ESLI_avant']['Turb']).mean()
    Turb_ION_ABCDE = ((data['ION_avant']['Turb (NTU)Entrée A,B,C,D,E']-data['ION_PRO']['Turb'])/data['ION_avant']['Turb (NTU)Entrée A,B,C,D,E']).mean()
    Turb_ION_FGHIJ = ((data['ION_avant']['Turb (NTU)Entrée F,G,H,I,J']-data['ION_PRO']['Turb'])/data['ION_avant']['Turb (NTU)Entrée F,G,H,I,J']).mean()
    np.random.seed(42)
    rd =[Turb_QT,Turb_ESLI,Turb_ION_ABCDE,Turb_ION_FGHIJ]
    data = {
        'unity': ["QT","ESLI","Turb_ION_ABCDE","Turb_ION_FGHIJ"],
        'Yield': rd
    }
    df = pd.DataFrame(data)


    # Sélection des catégories à afficher dans le pie chart
    selected_categories = st.multiselect('Sélectionnez les Unité à inclure dans le graphique :', options=df['unity'].unique(), default=df['unity'].unique())

    # Filtre les données en fonction des catégories sélectionnées
    filtered_df = df[df['unity'].isin(selected_categories)]

    # Crée le pie chart avec Plotly
    fig = px.pie(filtered_df, names='unity', values='Yield', title='Répartition des valeurs par catégorie')
    fig.update_layout(title={'text': 'Répartition des rendements par unity', 'x': 0.36})
# Affiche le pie chart avec Streamlit
    st.plotly_chart(fig)

def compare(unity):
    #filtrage selon l'unité QT
    if (unity[0] == ["QT"]) & (unity[1]==["Avant filtraion fine"]):
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
        if unity[2] == ["pH"]:
            st.markdown(f"<h2 style='text-align: center;'>pH moyen: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.bar(df,x="date",y="pH")
            fig.add_hline(y=8, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        if unity[2] == ["Turb"]:
            st.markdown(f"<h2 style='text-align: center;'>Turbidité moyenne: {np.around(df['Turb'].mean(),2)} NTU</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb")
            fig.add_hline(y=5.13, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        if unity[2] == "Cond":
            st.markdown(f"<h2 style='text-align: center;'>Condectivté moyenne: {np.around(df['Cond. (mS/cm) à 25° C'].mean(),2)} mS/cm</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cond. (mS/cm) à 25° C")
            fig.add_hline(y=55, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
        if unity[2] == "MES":
            st.markdown(f"<h2 style='text-align: center;'>MES moyen: {np.around(df['MES'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES")
            fig.add_hline(y=10, line_dash="dash", line_color="red", line_width=2)
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity[0] == "QT") & (unity[1] =="Perméat filtration"):
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
    elif (unity[0] == "QT") & (unity[1] =="Après filtration à cartouche"):
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
    elif (unity[0] == "QT") & (unity[1] =="Perméat RO"): 
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
    elif (unity[0] == "ESLI") & (unity[1] =="Avant filtraion fine"):
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
    elif (unity[0] == "ESLI") & (unity[1] =="Perméat filtration"):
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
    elif (unity[0] == "ESLI") & (unity[1] =="Après filtration à cartouche"):
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
    elif (unity[0] == "ESLI") & (unity[1] =="Perméat RO"):
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
    elif (unity[0] == "ION EXCHANGE") & (unity[1] =="Avant filtraion fine"):
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
    elif (unity[0] == "ION EXCHANGE") & (unity[1] =="Perméat filtration"):
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
    elif (unity[0] == "ION EXCHANGE") & (unity[1] =="Après filtration à cartouche"):
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
    elif (unity[0] == "ION EXCHANGE") & (unity[1] =="Perméat RO"):
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

def filtrage(data):
    df ={}
    params = []

    for i in range(len(data[0])):
        for j in range(len(data[1])):
            df[f"{data[0][i]}_{data[1][j]}"] = pd.read_excel('DATA/data préparé.xlsx',sheet_name=f"{data[0][i]}_{data[1][j]}")
 
    for i in range(len(data[2])):
       params.append(data[2][i])
    date1 = pd.to_datetime(st.date_input("Date"))
    Variation_param_pendant_phase(df,params,date1)
         
def Variation_param_pendant_phase(df,params,date1):

        for k in df.keys():
            df[k]['date'] = pd.to_datetime(df[k]['date'])
            df[k] = df[k][df[k]["date"] == date1]
        for param in params:
            x1= []
            x2 = []
            for k in df.keys():
                if( param in df[k]):
                    x1.append(float(df[k][param].mean()))
                    x2.append(k)
            colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA']   
            fig = go.Figure(data=[go.Bar(x=x2, y=x1, marker_color=colors, text=x1, textposition='outside')])

            fig.update_layout(
                title={'text': f"Variation de {param} dans l'unité {k.split('_')[0]} pendant les phases de traitement", 'x': 0.36},
                height=400,  # Ajustez la hauteur ici
                margin=dict(l=400, r=400, t=40, b=40),
                bargap=0.7   # Ajustez l'espace entre les barres
            )
            st.plotly_chart(fig,use_container_width=True) 
    
         
def filtrage(data):
    df ={}
    params = []
    
    for i in range(len(data[0])):
        for j in range(len(data[1])):
            df[f"{data[0][i]}_{data[1][j]}"] = pd.read_excel('DATA/data préparé.xlsx',sheet_name=f"{data[0][i]}_{data[1][j]}")
 
    for i in range(len(data[2])):
       params.append(data[2][i])

    Variation_param_pendant_phase(df,params)
         
def Variation_param_pendant_phase(df,params):

        for k in df.keys():
            #df[k]['date'] = pd.to_datetime(df[k]['Date de Pelevement'])
            startDate = pd.to_datetime(df[k]["Date de Pelevement"]).min()
            endDate = pd.to_datetime(df[k]["Date de Pelevement"]).max()

            col1,col2 = st.columns((2)) 
            with col1:
                date1 = pd.to_datetime(st.date_input("Start Date", startDate))

            with col2:
                date2 = pd.to_datetime(st.date_input("End Date", endDate))
            print(df[k].info())
            df = df[k][(df[k]["Date de Pelevement"] >= date1) & (df[k]["Date de Pelevement"] <= date2)]
          
        for param in params:
            print(param)
            for k in df.keys():
                if( param in df.keys()):
                    df[k].replace('/', np.nan, inplace=True)
                    df[k].replace('en cours', np.nan, inplace=True)
                    st.markdown(f"<h2 style='text-align: center;'>{param} moyenne: mS/cm</h2>", unsafe_allow_html=True)
                    fig = px.line(df[k],x="Date de Pelevement",y=param)
                    fig.add_hline(y=55, line_dash="dash", line_color="red", line_width=2)
                    st.plotly_chart(fig,use_container_width=True,height = 200)