import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")
import streamlit as st



st.sidebar.image("logo.png")
st.title(":bar_chart:  Desslement de l'eau de mer")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


st.sidebar.header("Chose your filter: ")
unity = st.sidebar.selectbox('Sélectionner l\'unité', ["Options","QT","ESLI","ION EXCHANGE"])

phase = st.sidebar.selectbox('Sélectionner la phase de traitement',['Options','Aant filtraion fine','Perméat filtration','Après filtration à cartouche','Perméat RO'])

if (unity == "QT") & (phase =="Aant filtraion fine"):
    df = pd.read_excel('DATA/data préparé.xlsx',sheet_name="QT_avant")

    col1,col2, = st.columns((2))
    df['date'] = pd.to_datetime(df['date'])

    startDate = pd.to_datetime(df["date"]).min()
    endDate = pd.to_datetime(df["date"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    df = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()
    with col1:
        st.markdown("<h2 style='text-align: center;'>pH</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="pH")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col2:
        st.markdown("<h2 style='text-align: center;'>Turb</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="Turb \n(NTU)")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col1:
        st.markdown("<h2 style='text-align: center;'>Cond</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="Cond. (mS/cm) à 25° C")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col2:
        st.markdown("<h2 style='text-align: center;'>MES</h2>", unsafe_allow_html=True)
        fig = px.line(df,x="date",y="MES \n(mg/l)")
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

    df2 = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()
    with col1:
        st.markdown("<h2 style='text-align: center;'>SDI 15 P1</h2>", unsafe_allow_html=True)
        fig = px.line(df2,x="date",y="SDI 15 P1")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col2:
        st.markdown("<h2 style='text-align: center;'>SDI 15 P2</h2>", unsafe_allow_html=True)
        fig = px.line(df2,x="date",y="SDI 15 P2")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col1:
        st.markdown("<h2 style='text-align: center;'>Turb P1</h2>", unsafe_allow_html=True)
        fig = px.line(df2,x="date",y="Turb P1")
        st.plotly_chart(fig,use_container_width=True,height = 200)
    with col2:
        st.markdown("<h2 style='text-align: center;'>Turb P2</h2>", unsafe_allow_html=True)
        fig = px.line(df2,x="date",y="Turb P2")
        st.plotly_chart(fig,use_container_width=True,height = 200)