import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components
import random


def filter(df,unity,phase):
    #filtrage selon l'unité QT
    if (unity == "QT") & (phase =="Perméat filtration"):
        df = pd.read_excel(df,sheet_name="QT_PF")
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
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) moyenne: {np.around(df['Turb (NTU)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Turb (NTU)")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=0.1,  # Position Y (sur la ligne horizontale)
                    text="Turb doit être égale à 0.1",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SiO2 (mg/l) moyenne: {np.around(df['SiO2 (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SiO2 (mg/l)")
            fig.add_hline(y=1.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=1.1,  # Position Y (sur la ligne horizontale)
                    text="SiO2 doit inférieur ou égale à 1.1",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES  (mg/l) moyenne: {np.around(df['MES (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES (mg/l)")
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=0,  # Position Y (sur la ligne horizontale)
                    text="MES doit être égale à 0",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI 15 moyenne: {np.around(df['SDI 15'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI 15")
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=2.5,  # Position Y (sur la ligne horizontale)
                    text="SDI 15 doit inférieur ouêtre égale à 2.5",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "QT") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel(df,sheet_name="QT_après")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
        df['TOC (mg/l)'] = df['TOC (mg/l)'].astype(float)
        df.loc[df['TOC (mg/l)'] < 3, 'TOC (mg/l)'] = 1
        df.loc[df['TOC (mg/l)'] > 3, 'TOC (mg/l)'] = 0

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH moyenne: {np.around(df['pH'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="pH")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) moyenne: {np.around(df['PO43-  (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="PO43-  (mg/l)")
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=0,  # Position Y (sur la ligne horizontale)
                    text="PO43- doit être égale à 0",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'> ORP (mV) P1 moyenne: {np.around(df[' ORP (mV) P1'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=" ORP (mV) P1")
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                y=250,  # Position Y (sur la ligne horizontale à 250)
                text="Min: 250 mV",  # Texte de l'annotation
                showarrow=True,  # Afficher une flèche pointant vers le point
                arrowhead=2,  # Type de flèche
                ax=0,  # Position X de la flèche par rapport au texte
                ay=-40  # Position Y de la flèche par rapport au texte
            )

            fig.add_annotation(
                x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                y=300,  # Position Y (sur la ligne horizontale à 300)
                text="Max: 300 mV",  # Texte de l'annotation
                showarrow=True,  # Afficher une flèche pointant vers le point
                arrowhead=2,  # Type de flèche
                ax=0,  # Position X de la flèche par rapport au texte
                ay=40  # Position Y de la flèche par rapport au texte
            )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) P2 moyenne: {np.around(df['ORP (mV) P2'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="ORP (mV) P2")
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                y=250,  # Position Y (sur la ligne horizontale à 250)
                text="Min: 250 mV",  # Texte de l'annotation
                showarrow=True,  # Afficher une flèche pointant vers le point
                arrowhead=2,  # Type de flèche
                ax=0,  # Position X de la flèche par rapport au texte
                ay=-40  # Position Y de la flèche par rapport au texte
            )

            fig.add_annotation(
                x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                y=300,  # Position Y (sur la ligne horizontale à 300)
                text="Max: 300 mV",  # Texte de l'annotation
                showarrow=True,  # Afficher une flèche pointant vers le point
                arrowhead=2,  # Type de flèche
                ax=0,  # Position X de la flèche par rapport au texte
                ay=40  # Position Y de la flèche par rapport au texte
            )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 moyenne: {np.around(df['SDI15'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SDI15")
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=2.5,  # Position Y (sur la ligne horizontale)
                    text="PO43- doit être égale à 2.5",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) moyenne: {np.around(df['TOC (mg/l)'].mean(),2)} mg/l</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TOC (mg/l)")
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=1,  # Position Y (sur la ligne horizontale)
                        text="TOC doit être égale à 1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)        
    elif (unity == "QT") & (phase =="Perméat RO"): 
        df = pd.read_excel(df,sheet_name="QT_PRO")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(F"<h2 style='text-align: center;'>Cond A moyen : {np.around(df['Cond A'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond A doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond B moyen : {np.around(df['Cond B'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond B doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond C moyen : {np.around(df['Cond C'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond C doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond D moyen : {np.around(df['Cond D'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond D')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond D doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond E moyen : {np.around(df['Cond E'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond E')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond E doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond F moyen : {np.around(df['Cond F'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond F')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond F doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond G moyen : {np.around(df['Cond G'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond G')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond G doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond H moyen : {np.around(df['Cond H'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond H')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond H doit être inférieure à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH A moyen : {np.around(df['pH A'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH A')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH A doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH B moyen : {np.around(df['pH B'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH B')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH B doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH C moyen : {np.around(df['pH C'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH C')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH C doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH D moyen : {np.around(df['pH D'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH D')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH D doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH E moyen : {np.around(df['pH E'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH E')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH E doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH F moyen : {np.around(df['pH F'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH F')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH F doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH G moyen : {np.around(df['pH G'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH G')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH G doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH H moyen : {np.around(df['pH H'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH H')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH H doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

    #filtrage selon l'unité ESLI
    if (unity == "ESLI") & (phase =="Perméat filtration"):
        df = pd.read_excel(df,sheet_name="ESLI_PF")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(f"<h2 style='text-align: center;'>Fe2+ (mg/l) Zone A  moyen : {np.around(df['Fe2+ (mg/l) Zone A'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone A')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe2+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Fe3+ (mg/l) Zone A  moyen : {np.around(pd.to_numeric(df['Fe3+ (mg/l) Zone A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone A')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe3+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES (mg/l) Zone A moyen : {np.around(pd.to_numeric(df['MES (mg/l) Zone A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone A')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="MES doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 Zone A moyen : {np.around(pd.to_numeric(df['SDI15 Zone A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone A')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieure à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Fe2+ (mg/l) Zone B moyen : {np.around(pd.to_numeric(df['Fe2+ (mg/l) Zone B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone B')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe2+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Fe3+ (mg/l) Zone B moyen : {np.around(pd.to_numeric(df['Fe3+ (mg/l) Zone B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone B')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe3+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES (mg/l) Zone B moyen : {np.around(pd.to_numeric(df['MES (mg/l) Zone B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone B')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="MES doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 Zone B moyen : {np.around(pd.to_numeric(df['SDI15 Zone B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone B')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieure à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Fe2+ (mg/l) Zone C moyen : {np.around(pd.to_numeric(df['Fe2+ (mg/l) Zone C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe2+ (mg/l) Zone C')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe2+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Fe3+ (mg/l) Zone C moyen : {np.around(pd.to_numeric(df['Fe3+ (mg/l) Zone C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Fe3+ (mg/l) Zone C')
            fig.add_hline(y=0.2, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.2,  # Position Y (sur la ligne horizontale)
                        text="Fe3+ doit être inférieure à 0.2",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>MES (mg/l) Zone C moyen : {np.around(pd.to_numeric(df['MES (mg/l) Zone C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='MES (mg/l) Zone C')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="MES doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 Zone C moyen : {np.around(pd.to_numeric(df['SDI15 Zone C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Zone C')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieure à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel(df,sheet_name="ESLI_après")
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
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH ZONE A moyen : {np.around(pd.to_numeric(df['pH ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>T (°C)  ZONE A moyen : {np.around(pd.to_numeric(df['T (°C)  ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C)  ZONE A')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV)  ZONE A moyen : {np.around(pd.to_numeric(df['ORP (mV)  ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV)  ZONE A')
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15  ZONE A moyen : {np.around(pd.to_numeric(df['SDI15  ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15  ZONE A')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.50,  # Position Y (sur la ligne horizontale)
                        text="SDI15  doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE A moyen : {np.around(pd.to_numeric(df['PO43-  (mg/l)  ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l)  ZONE A')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43-  doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l)  ZONE A moyen : {np.around(pd.to_numeric(df['TDS (mg/l)  ZONE A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l)  ZONE A')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS  doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
            st.markdown(f"<h2 style='text-align: center;'>pH ZONE B moyen : {np.around(pd.to_numeric(df['pH  ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH  ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>T (°C)  ZONE B moyen : {np.around(pd.to_numeric(df['T (°C) ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C) ZONE B')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV)  ZONE B moyen : {np.around(pd.to_numeric(df['ORP (mV) ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) ZONE B')
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15  ZONE B moyen : {np.around(pd.to_numeric(df['SDI15 ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 ZONE B')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.50,  # Position Y (sur la ligne horizontale)
                        text="SDI15  doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE B moyen : {np.around(pd.to_numeric(df['PO43-  (mg/l) ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) ZONE B')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43-  doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l)  ZONE B moyen : {np.around(pd.to_numeric(df['TDS (mg/l) ZONE B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) ZONE B')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS  doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
            st.markdown(f"<h2 style='text-align: center;'>pH ZONE C moyen : {np.around(pd.to_numeric(df['pH ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>T (°C)  ZONE C moyen : {np.around(pd.to_numeric(df['T (°C) ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='T (°C) ZONE C')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV)  ZONE C moyen : {np.around(pd.to_numeric(df['ORP (mV) ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) ZONE C')
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15  ZONE C moyen : {np.around(pd.to_numeric(df['SDI15 ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 ZONE C')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.50,  # Position Y (sur la ligne horizontale)
                        text="SDI15  doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l)  ZONE C moyen : {np.around(pd.to_numeric(df['PO43-  (mg/l) ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) ZONE C')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43-  doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l)  ZONE C moyen : {np.around(pd.to_numeric(df['TDS (mg/l) ZONE C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) ZONE C')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS  doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ESLI") & (phase =="Perméat RO"):
        df = pd.read_excel(df,sheet_name="ESLI_PRO")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(f"<h2 style='text-align: center;'>Cond A1 moyen : {np.around(pd.to_numeric(df['Cond A1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A1')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond A2 moyen : {np.around(pd.to_numeric(df['Cond A2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A2')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond A3 moyen : {np.around(pd.to_numeric(df['Cond A3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A3')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond A4 moyen : {np.around(pd.to_numeric(df['Cond A4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A4')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond B1 moyen : {np.around(pd.to_numeric(df['Cond B1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B1')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond B2 moyen : {np.around(pd.to_numeric(df['Cond B2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B2')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond B3 moyen : {np.around(pd.to_numeric(df['Cond B3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B3')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond B4 moyen : {np.around(pd.to_numeric(df['Cond B4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B4')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond C1 moyen : {np.around(pd.to_numeric(df['Cond C1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C1')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond C2 moyen : {np.around(pd.to_numeric(df['Cond C2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C2')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond C3 moyen : {np.around(pd.to_numeric(df['Cond C3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C3')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond C4 moyen : {np.around(pd.to_numeric(df['Cond C4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C4')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph A1 moyen : {np.around(pd.to_numeric(df['Ph A1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A1')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph A2 moyen : {np.around(pd.to_numeric(df['Ph A2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A2')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph A3 moyen : {np.around(pd.to_numeric(df['Ph A3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A3')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph A4 moyen : {np.around(pd.to_numeric(df['Ph A4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph A4')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph B1 moyen : {np.around(pd.to_numeric(df['Ph B1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B1')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph B2 moyen : {np.around(pd.to_numeric(df['Ph b2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph b2')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph B3 moyen : {np.around(pd.to_numeric(df['Ph B3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B3')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph B4 moyen : {np.around(pd.to_numeric(df['Ph B4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph B4')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph C1 moyen : {np.around(pd.to_numeric(df['Ph C1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C1')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph C2 moyen : {np.around(pd.to_numeric(df['Ph C2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C2')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Ph C3 moyen : {np.around(pd.to_numeric(df['Ph C3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C3')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Ph C4 moyen : {np.around(pd.to_numeric(df['Ph C4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Ph C4')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    #filtrage selon l'unité ION EXCHANGE
    if (unity == "ION EXCHANGE") & (phase =="Perméat filtration"):
        df = pd.read_excel(df,sheet_name="ION_PF")
        col1,col2, = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) HMMF A moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF A')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF A moyen : {np.around(pd.to_numeric(df['SDI15 HMMF A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF A')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF B moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF B')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF B moyen : {np.around(pd.to_numeric(df['SDI15 HMMF B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF B')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF C moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF C')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF C moyen : {np.around(pd.to_numeric(df['SDI15 HMMF C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF C')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200) 
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF D moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF D'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF D')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF D moyen : {np.around(pd.to_numeric(df['SDI15 HMMF D'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF D')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)  
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF E moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF B')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF E moyen : {np.around(pd.to_numeric(df['SDI15 HMMF E'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF E')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF F moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF F'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF F')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF F moyen : {np.around(pd.to_numeric(df['SDI15 HMMF F'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF F')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF G moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF G'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF G')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF G moyen : {np.around(pd.to_numeric(df['SDI15 HMMF G'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF G')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF H moyen: moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF H'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF H')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF H moyen : {np.around(pd.to_numeric(df['SDI15 HMMF H'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF H')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF I moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF I'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF I')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF I moyen : {np.around(pd.to_numeric(df['SDI15 HMMF I'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF I')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF J moyen : {np.around(pd.to_numeric(df['Turb (NTU) HMMF J'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) HMMF J')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 HMMF J moyen : {np.around(pd.to_numeric(df['SDI15 HMMF J'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 HMMF J')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI 15 Collecteur moyen: {np.around(df['SDI 15 Collecteur'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI 15 Collecteur')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ION EXCHANGE") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel(df,sheet_name="ION_après")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) Collecteur A,B,C,D,E moyen : {np.around(pd.to_numeric(df['ORP (mV) Collecteur A,B,C,D,E'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) Collecteur A,B,C,D,E')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) Collecteur F,G,H,I,J moyen : {np.around(pd.to_numeric(df['ORP (mV) Collecteur F,G,H,I,J'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) Collecteur F,G,H,I,J')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 Collecteur A,B,C,D,E moyen: {np.around(pd.to_numeric(df['SDI15 Collecteur A,B,C,D,E'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Collecteur A,B,C,D,E')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 Collecteur F,G,H,I,J moyen: {np.around(pd.to_numeric(df['SDI15 Collecteur F,G,H,I,J'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 Collecteur F,G,H,I,J')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    elif (unity == "ION EXCHANGE") & (phase =="Perméat RO"):
        df = pd.read_excel(df,sheet_name="ION_PRO")
        col1,col2 = st.columns((2))
        df['date'] = pd.to_datetime(df['date'])

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
            st.markdown(f"<h2 style='text-align: center;'>Cond A moyen : {np.around(pd.to_numeric(df['Cond A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond A')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond B moyen : {np.around(pd.to_numeric(df['Cond B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond B')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond C moyen : {np.around(pd.to_numeric(df['Cond C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond C')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond D moyen : {np.around(pd.to_numeric(df['Cond D'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond D')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond E moyen : {np.around(pd.to_numeric(df['Cond E'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond E')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond F moyen : {np.around(pd.to_numeric(df['Cond F'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond F')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond G moyen : {np.around(pd.to_numeric(df['Cond G'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond G')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Cond H moyen : {np.around(pd.to_numeric(df['Cond H'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond H')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH A moyen : {np.around(pd.to_numeric(df['pH A'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH A')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH B moyen : {np.around(pd.to_numeric(df['pH B'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH B')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH C moyen : {np.around(pd.to_numeric(df['pH C'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH C')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH D moyen : {np.around(pd.to_numeric(df['pH d '], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH d ')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH E moyen : {np.around(pd.to_numeric(df['pH E'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH E')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH F moyen : {np.around(pd.to_numeric(df['pH F '], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH F ')
            fig.add_hline(y=5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5,  # Position Y (sur la ligne horizontale)
                        text="pH doit être inférieur à 5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH G moyen : {np.around(pd.to_numeric(df['pH G'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH G')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH H moyen : {np.around(pd.to_numeric(df[' pH H'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y=' pH H')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
    # filtrage selon l'unité MCT
    elif (unity == "MCT") & (phase =="Après filtration à cartouche"):
        df = pd.read_excel(df, sheet_name="MCT_après")
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
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)

        df['TOC (mg/l) LIGNE 1'] = df['TOC (mg/l) LIGNE 1'].replace('<3',1)
        df['TOC (mg/l) LIGNE 1'] = df['TOC (mg/l) LIGNE 1'].replace(0,1)
        df['TOC (mg/l) LIGNE 1'] = df['TOC (mg/l) LIGNE 1'].astype(float)
        df.loc[df['TOC (mg/l) LIGNE 1'] < 3, 'TOC (mg/l) LIGNE 1'] = 1
        df.loc[df['TOC (mg/l) LIGNE 1'] > 3, 'TOC (mg/l) LIGNE 1'] = 0

        df['TOC (mg/l) LIGNE 2'] = df['TOC (mg/l) LIGNE 2'].replace('<3',1)
        df['TOC (mg/l) LIGNE 2'] = df['TOC (mg/l) LIGNE 2'].replace(0,1)
        df['TOC (mg/l) LIGNE 2'] = df['TOC (mg/l) LIGNE 2'].astype(float)
        df.loc[df['TOC (mg/l) LIGNE 2'] < 3, 'TOC (mg/l) LIGNE 2'] = 1
        df.loc[df['TOC (mg/l) LIGNE 2'] > 3, 'TOC (mg/l) LIGNE 2'] = 0

        df['TOC (mg/l) LIGNE 3'] = df['TOC (mg/l) LIGNE 3'].replace('<3',1)
        df['TOC (mg/l) LIGNE 3'] = df['TOC (mg/l) LIGNE 3'].replace(0,1)
        df['TOC (mg/l) LIGNE 3'] = df['TOC (mg/l) LIGNE 3'].astype(float)
        df.loc[df['TOC (mg/l) LIGNE 3'] < 3, 'TOC (mg/l) LIGNE 3'] = 1
        df.loc[df['TOC (mg/l) LIGNE 3'] > 3, 'TOC (mg/l) LIGNE 3'] = 0

        df['TOC (mg/l) LIGNE 4'] = df['TOC (mg/l) LIGNE 4'].replace('<3',1)
        df['TOC (mg/l) LIGNE 4'] = df['TOC (mg/l) LIGNE 4'].astype(float)
        df.loc[df['TOC (mg/l) LIGNE 4'] < 3, 'TOC (mg/l) LIGNE 4'] = 1
        df.loc[df['TOC (mg/l) LIGNE 4'] > 3, 'TOC (mg/l) LIGNE 4'] = 0

#LIGNE 1
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 1 moyen: {np.around(df['pH LIGNE 1'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 1')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) LIGNE 1 moyen: {np.around(pd.to_numeric(df['Turb (NTU) LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) LIGNE 1')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb LIGNE 1 doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) LIGNE 1 moyen: {np.around(pd.to_numeric(df['PO43-  (mg/l) LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) LIGNE 1')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43- LIGNE 1 doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) LIGNE 1 moyen: {np.around(pd.to_numeric(df['ORP (mV) LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) LIGNE 1')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 LIGNE 1 moyen: {np.around(pd.to_numeric(df['SDI15 LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 LIGNE 1')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 LIGNE 1 doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) LIGNE 1 moyen: {np.around(pd.to_numeric(df['TOC (mg/l) LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TOC (mg/l) LIGNE 1')
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=1,  # Position Y (sur la ligne horizontale)
                        text="TOC LIGNE 1 doit être égale à 1 (1 pour les valeurs <3 et 0 sinon)",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l) LIGNE 1 moyen: {np.around(pd.to_numeric(df['TDS (mg/l) LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) LIGNE 1')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS LIGNE 1 doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
#LIGNE 2      
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 2 moyen: {np.around(df['pH LIGNE 2'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 2')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) LIGNE 2 moyen: {np.around(pd.to_numeric(df['Turb (NTU) LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) LIGNE 2')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb LIGNE 2 doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) LIGNE 2 moyen: {np.around(pd.to_numeric(df['PO43-   (mg/l) LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-   (mg/l) LIGNE 2')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43- LIGNE 2 doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) LIGNE 2 moyen: {np.around(pd.to_numeric(df['ORP (mV) LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) LIGNE 2')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 LIGNE 2 moyen: {np.around(pd.to_numeric(df['SDI15 LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 LIGNE 2')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 LIGNE 2 doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) LIGNE 2 moyen: {np.around(pd.to_numeric(df['TOC (mg/l) LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TOC (mg/l) LIGNE 2')
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=1,  # Position Y (sur la ligne horizontale)
                        text="TOC LIGNE 2 doit être égale à 1 (1 pour les valeurs <3 et 0 sinon)",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l) LIGNE 2 moyen: {np.around(pd.to_numeric(df['TDS (mg/l) LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) LIGNE 2')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS LIGNE 2 doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
#LIGNE 3
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 3 moyen: {np.around(df['pH LIGNE 3'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 3')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) LIGNE 3 moyen: {np.around(pd.to_numeric(df['Turb (NTU) LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) LIGNE 3')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb LIGNE 3 doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) LIGNE 3 moyen: {np.around(pd.to_numeric(df['PO43-  (mg/l) LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) LIGNE 3')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43- LIGNE 3 doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) LIGNE 13 moyen: {np.around(pd.to_numeric(df['ORP (mV) LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) LIGNE 3')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 LIGNE 3 moyen: {np.around(pd.to_numeric(df['SDI15 LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 LIGNE 3')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 LIGNE 3 doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TOC LIGNE 3 moyen: {np.around(pd.to_numeric(df['TOC (mg/l) LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TOC (mg/l) LIGNE 3')
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=1,  # Position Y (sur la ligne horizontale)
                        text="TOC LIGNE 3 doit être égale à 1 (1 pour les valeurs <3 et 0 sinon)",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l) LIGNE 3 moyen: {np.around(pd.to_numeric(df['TDS (mg/l) LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) LIGNE 3')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS LIGNE 3 doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
#LIGNE 4
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 4 moyen: {np.around(df['pH  LIGNE 4'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH  LIGNE 4')
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Turb (NTU) LIGNE 4 moyen: {np.around(pd.to_numeric(df['Turb (NTU) LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Turb (NTU) LIGNE 4')
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0.1,  # Position Y (sur la ligne horizontale)
                        text="Turb LIGNE 4 doit être inférieur à 0.1",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>PO43-  (mg/l) LIGNE 4 moyen: {np.around(pd.to_numeric(df['PO43-  (mg/l) LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='PO43-  (mg/l) LIGNE 4')
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=0,  # Position Y (sur la ligne horizontale)
                        text="PO43- LIGNE 4 doit être égale à 0",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>ORP (mV) LIGNE 4 moyen: {np.around(pd.to_numeric(df['ORP (mV) LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='ORP (mV) LIGNE 4')
            fig.add_hline(y=250, line_dash="dash", line_color="red", line_width=2)
            fig.add_hline(y=300, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=250,  # Position Y (sur la ligne horizontale)
                        text="Min 250 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=300,  # Position Y (sur la ligne horizontale)
                        text="Max 300 mv",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SDI15 LIGNE 4 moyen: {np.around(pd.to_numeric(df['SDI15 LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='SDI15 LIGNE 4')
            fig.add_hline(y=2.5, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=2.5,  # Position Y (sur la ligne horizontale)
                        text="SDI15 LIGNE 4 doit être inférieur à 2.5",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) LIGNE 4 moyen: {np.around(pd.to_numeric(df['TOC (mg/l) LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TOC (mg/l) LIGNE 4')
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=1,  # Position Y (sur la ligne horizontale)
                        text="TOC LIGNE 4 doit être égale à 1 (1 pour les valeurs <3 et 0 sinon)",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>TDS (mg/l) LIGNE 4 moyen: {np.around(pd.to_numeric(df['TDS (mg/l) LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='TDS (mg/l) LIGNE 2')
            fig.add_hline(y=40000, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=40000,  # Position Y (sur la ligne horizontale)
                        text="TDS LIGNE 4 doit être inférieur à 40 000",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)   
    elif (unity == "MCT") & (phase =="Perméat RO"): 
        df = pd.read_excel(df,sheet_name="MCT_PRO")
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
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond LIGNE 1 moyen: {np.around(pd.to_numeric(df['Cond LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond LIGNE 1')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond LIGNE 1 doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 1 moyen: {np.around(pd.to_numeric(df['pH LIGNE 1'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 1')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH LIGNE 1 doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
                st.markdown(f"<h2 style='text-align: center;'>Cond LIGNE 2 moyen: {np.around(pd.to_numeric(df['Cond LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
                fig = px.line(df,x="date",y='Cond LIGNE 2')
                fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
                fig.add_annotation(
                            x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                            y=450,  # Position Y (sur la ligne horizontale)
                            text="Cond LIGNE 2 doit être inférieur à 450",  # Texte de l'annotation
                            showarrow=True,  # Afficher une flèche pointant vers le point
                            arrowhead=2,  # Type de flèche
                            ax=0,  # Position X de la flèche par rapport au texte
                            ay=-40  # Position Y de la flèche par rapport au texte
                        )
                st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 2 moyen: {np.around(pd.to_numeric(df['pH LIGNE 2'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 2')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH LIGNE 2 doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
                st.markdown(f"<h2 style='text-align: center;'>Cond LIGNE 3 moyen: {np.around(pd.to_numeric(df['Cond LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
                fig = px.line(df,x="date",y='Cond LIGNE 3')
                fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
                fig.add_annotation(
                            x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                            y=450,  # Position Y (sur la ligne horizontale)
                            text="Cond LIGNE 3 doit être inférieur à 450",  # Texte de l'annotation
                            showarrow=True,  # Afficher une flèche pointant vers le point
                            arrowhead=2,  # Type de flèche
                            ax=0,  # Position X de la flèche par rapport au texte
                            ay=-40  # Position Y de la flèche par rapport au texte
                        )
                st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 3 moyen: {np.around(pd.to_numeric(df['pH LIGNE 3'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 3')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH LIGNE 3 doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cond LIGNE 4 moyen: {np.around(pd.to_numeric(df['Cond LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='Cond LIGNE 4')
            fig.add_hline(y=450, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=450,  # Position Y (sur la ligne horizontale)
                        text="Cond LIGNE 4 doit être inférieur à 450",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>pH LIGNE 4 moyen: {np.around(pd.to_numeric(df['pH LIGNE 4'], errors='coerce').mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y='pH LIGNE 4')
            fig.add_hline(y=5.4, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                        x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                        y=5.4,  # Position Y (sur la ligne horizontale)
                        text="pH LIGNE 4 doit être supérieur à 5.4",  # Texte de l'annotation
                        showarrow=True,  # Afficher une flèche pointant vers le point
                        arrowhead=2,  # Type de flèche
                        ax=0,  # Position X de la flèche par rapport au texte
                        ay=-40  # Position Y de la flèche par rapport au texte
                    )
            st.plotly_chart(fig,use_container_width=True,height = 200)

    elif(phase == "intake"):
        df = pd.read_excel(df,sheet_name="intake")
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
        df.replace('/', np.nan, inplace=True)
        df.replace('en cours', np.nan, inplace=True)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].replace('<3',1)
        df['TOC (mg/l)'] = df['TOC (mg/l)'].astype(float)
        df.loc[df['TOC (mg/l)'] < 3, 'TOC (mg/l)'] = 1
        df.loc[df['TOC (mg/l)'] > 3, 'TOC (mg/l)'] = 0
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>PO43- (mg/l) moyen: {np.around(df['PO43- (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)        
            fig = px.line(df,x="date",y="PO43- (mg/l)")
            fig.add_hline(y=0.1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=0.1,  # Position Y (sur la ligne horizontale)
                    text="PO43- doit être inférieur ou égale à 0.1",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>SiO2 (mg/l) moyen: {np.around(df['SiO2 (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="SiO2 (mg/l)")
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>TOC (mg/l) moyenne: {np.around(df['TOC (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="TOC (mg/l)")
            fig.add_hline(y=1, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=1,  # Position Y (sur la ligne horizontale)
                    text="TOC doit être égale à 1",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col2:
            st.markdown(f"<h2 style='text-align: center;'>MES  (mg/l) moyenne: {np.around(df['MES  (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="MES  (mg/l)")
            fig.add_hline(y=10, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=10,  # Position Y (sur la ligne horizontale)
                    text="MES doit être inférieur ou égale à 10",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
            st.plotly_chart(fig,use_container_width=True,height = 200)
        with col1:
            st.markdown(f"<h2 style='text-align: center;'>Cl2 libre (mg/l) moyenne: {np.around(df['Cl2 libre (mg/l)'].mean(),2)}</h2>", unsafe_allow_html=True)
            fig = px.line(df,x="date",y="Cl2 libre (mg/l)")
            fig.add_hline(y=0, line_dash="dash", line_color="red", line_width=2)
            fig.add_annotation(
                    x=df['date'].iloc[-1],  # Position X (la dernière date dans ce cas)
                    y=0,  # Position Y (sur la ligne horizontale)
                    text="Cl2 libre doit être égale à 0",  # Texte de l'annotation
                    showarrow=True,  # Afficher une flèche pointant vers le point
                    arrowhead=2,  # Type de flèche
                    ax=0,  # Position X de la flèche par rapport au texte
                    ay=-40  # Position Y de la flèche par rapport au texte
                )
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
def filtrage(t,data):
    df ={}
    params = data[2]
    for i in range(len(data[0])):
        for j in range(len(data[1])):
            df[f"{data[1][j]}"] = pd.read_excel(t,sheet_name=f"{data[0][i]}_{data[1][j]}")
    df['intake'] = pd.read_excel(t,sheet_name="intake")

    date1 = pd.to_datetime(st.date_input("Date"))
    Variation_param_pendant_phase(df,params,date1)   
def Variation_param_pendant_phase(df,params,date1):
        
        for k in df.keys():
            df[k]['date'] = pd.to_datetime(df[k]['date'])
            df[k] = df[k][df[k]["date"] == date1]
            df[k].replace('/', np.nan, inplace=True)
            df[k].replace('en cours', np.nan, inplace=True) 
         
        x1 =[]
        x2 = []

        for param, value in params.items():
            if value:
                if param in df.keys():
                    x1.append(float(df[param][params[param][0]].mean()))
                    x2.append(param) 
  

        #colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA']  
        colors = generate_hex_colors(len(params)) 
        fig = go.Figure(data=[go.Bar(x=x2, y=x1, marker_color=colors, text=x1, textposition='outside')])
        fig.update_layout(
            title={'text': f"Variation de {params[param][0]} dans l'unité {k.split('_')[0]} pendant les phases de traitement", 'x': 0.36},
            height=400,  # Ajustez la hauteur ici
            margin=dict(l=400, r=400, t=40, b=40),
            bargap=0.7   # Ajustez l'espace entre les barres
        )
        st.plotly_chart(fig,use_container_width=True) 
def generate_hex_colors(n):
    colors = []
    for _ in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors