from controller.main_controller import MainController

import streamlit as st
import logging

from model.answer import Answer

from typing import List

logger = logging.getLogger(__name__)

def init():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

    logger.info("Bem vindo ao melhor mini agente do mundo")

    set_view()

    question = get_user_input()
    
    if question:
        result = MainController.run(question, update_view_with_chunks)
        update_view_with_result(result)

def set_view():
    logging.info("Configurando View")

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

if __name__ == "__main__":
    init()
