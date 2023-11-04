import plotly.express as px
import streamlit as st
from ler_excel import lerExcel

excels = ["Censo 2022 - Crescimento Populacional - Brasil", 
                "Censo 2022 - Pirâmide etária - Brasil",
                "Censo 2022 - População por sexo - Brasil",
                "Censo 2022 - Território - Brasil"]

with st.sidebar:
        st.title("Arquivos")
        nome = st.radio(
               "Escolha uma tabela",
               excels,
        )

st.title(nome)
base_dados = lerExcel(nome)
st.write(base_dados)

graficos = {
        excels[0]: {
                "x": "Ano da pesquisa",
                "y": "População(pessoas)",
                "colors": {'População(pessoas)': '#008000'}
        },
        excels[1]: {
                "x": "Grupo de idade",
                "y": ["População feminina(pessoas)",
                "População masculina(pessoas)"],
                "colors": {'População feminina(pessoas)': '#008000', 'População masculina(pessoas)': '#FFFF00'}
        },
        excels[2]: {
                "x": "Sexo",
                "y": "População(pessoas)",
                "colors": {'População(pessoas)': '#008000'}
        },
        excels[3]: {
                "x": "Ano da pesquisa",
                "y": ["Densidade demográfica(hab/km²)", "Área(km²)"],
                "colors": {'Área(km²)': '#008000', 'Densidade demográfica(hab/km²)': '#FFFF00'}
        },
}

graficoSelecionado = graficos[nome]

fig = px.bar(base_dados, 
             x=graficoSelecionado['x'],
             y=graficoSelecionado['y'],
             title=f"{nome} - BarChart",
             color_discrete_map = graficoSelecionado['colors']
        #      
        )
st.plotly_chart(fig)