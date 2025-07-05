import streamlit as st

import logging

logger = logging.getLogger(__name__)

class MainPage:

    def get_user_input():
        logging.info("Configurando View")

        st.header("Podem perguntar sobre o meu TCC")

        user_question = st.text_input("Digite sua pergunta", value = "qual foi o aplicativo escolhido para o projeto?")

        return user_question
