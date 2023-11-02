import plotly.express as px
import streamlit as st
from ler_excel import lerExcel

with st.sidebar:
        st.title("Arquivos")
        nome = st.radio(
               "Escolha uma tabela",
               ["Censo 2022 - Crescimento Populacional - Brasil", 
                "Censo 2022 - Pirâmide etária - Brasil",
                "Censo 2022 - População por sexo - Brasil",
                "Censo 2022 - Território - Brasil"],
        )
        # st.text_input(label="Pesquisar", placeholder="Buscando por...")
        # st.button("Pesquisar", type="primary", use_container_width=True)

# UI
# st.title("Em desenvolvimento")
# st.subheader("Teste de desenvolvimento")


# st.write(nome)
# st.text("""A prática cotidiana prova que a expansão dos mercados mundiais 
# ainda não demonstrou convincentemente que vai participar 
# na mudança das formas de ação.""")

# if(nome != "") :
#         try:   
# data_frame = lerExcel(nome)
# st.dataframe(data_frame)
        # except:
        #        st.write("Nenhuma planilha encontrada :(")
        
st.title(nome)
base_dados = lerExcel(nome)
st.write(base_dados)

# st.markdown(
#         """
# <style>

# </style>
#         """
# )

fig = px.bar(base_dados, 
             x="Grupo de idade",
             y=["População feminina(pessoas)",
                "População masculina(pessoas)"],
             title=f"{nome} - BarChart"
        )
st.plotly_chart(fig)