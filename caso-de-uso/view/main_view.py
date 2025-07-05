from model.answer import Answer
import streamlit as st

from typing import List

import logging

logger = logging.getLogger(__name__)

class MainView():

    def set_view():
        logging.info("Configurando View")
        st.write("")
        st.header("Podem perguntar sobre o meu TCC")

    def get_user_input() -> str:
        return st.text_input("Digite sua pergunta", value = "qual foi o aplicativo escolhido para o projeto?")

    def update_view_with_chunks(answers: List[Answer]):
        st.subheader("Chunks recuperados:")
        
        for answer in answers:
            st.write(answer.content)

    def update_view_with_result(result: str):
        st.subheader("Resposta final OpenAI:")
        st.write(result)

    def update_view_with_evaluate(evaluate: str):
        st.subheader("Evaluate:")
        st.write(evaluate)