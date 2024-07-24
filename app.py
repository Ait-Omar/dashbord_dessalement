import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from filters import filter
import os

st.set_page_config(page_title="DIPS", page_icon="logo.png",layout="wide")
import streamlit as st
import streamlit.components.v1 as components



st.sidebar.image("logo.png")
st.title(":bar_chart:  Desslement de l'eau de mer")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)


st.sidebar.header("Visualisation des paramètres: ")
unity = st.sidebar.selectbox('Unité:',
                              [" ",
                               "QT",
                                "ESLI",
                                "ION EXCHANGE"])

phase = st.sidebar.selectbox('Phase de traitement:',
                            [' ',
                            'Avant filtraion fine',
                            'Perméat filtration',
                            'Après filtration à cartouche',
                            'Perméat RO'])
filter(unity,phase)
st.sidebar.subheader('Comparaison des paramètres:')
selected_param = st.sidebar.selectbox('Paramètre:',
                              [" ",
                                "MES",
                                "Turb",
                                "Cond",
                                "PO13-"])

sheets =["QT_avant","QT_PF","QT_après","QT_PRO",
         "ESLI_avant","ESLI_PF", "ESLI_après","ESLI_PRO",
         "ION_avant","ION_PF","ION_après","ION_PRO"]
data = {}

for sheet in sheets:
    data[sheet] = df = pd.read_excel('DATA/data préparé.xlsx',sheet_name=sheet)

Mes_QT = (data['QT_avant']['MES']/data['QT_PF']['MES']).mean()
Mes_ESLI = (data['ESLI_avant']['MES']/data['ESLI_PF']['MES']).mean()
Mes_ION = (data['ION_avant']['MES (mg/l)']/data['ION_PF']['MES (mg/l)']).mean()

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

if selected_param == "MES":
    st.markdown(f"<h2 style='text-align: center;'>Histogrammes des rendements de MES:</h2>", unsafe_allow_html=True)
    components.html(html_string, height=600)

