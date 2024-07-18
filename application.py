# Bibliotecas utilizadas no aplicativo ---------------------------------------------------------------------------------------------
import os
import cohere 
import streamlit as st

from dotenv import load_dotenv, find_dotenv # variável global local



# Configurações Gerais -------------------------------------------------------------------------------------------------------------
# Configura nome e icon da aba
st.set_page_config(
    page_title="My Application",  # Título da aba do navegador
    page_icon="🌟",  # Ícone da aba do navegador
)

# Estilos geral (CSS) 
estilos = """
    <style>
    .titulo-centralizado {
        text-align: center;
        font-size: 2.5em; /* Tamanho da fonte do título */
        color: #000000; /* Cor do texto 'Preta'*/
        padding-bottom: 10px; /* Espaçamento inferior */
    }
    </style>
    """
# Renderizando o estilo CSS
st.markdown(estilos, unsafe_allow_html=True)

# Título da página
st.markdown('<h1 class="titulo-centralizado">My Application</h1>', unsafe_allow_html=True)