from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.messages import BaseMessage

from typing import List
from model.answer import Answer

import logging

logger = logging.getLogger(__name__)

def connectToOpenAI(question: str, apiKey: str, answers: List[Answer]):
    logger.info("Iniciando conexão com a open AI do documento...")

    if not answers:
        logger.warning("Nenhum contexto foi passado para o prompt.")
        return

    chat = ChatOpenAI(model="gpt-4o-mini", api_key=apiKey)

    prompt = getPrompt(question=question, answers=answers)
    
    response = chat.invoke(prompt)

    logger.info("===================================")
    logger.info(f"OpenAI: {response.content}")
    logger.info("===================================")

    logger.info("Finalizando conexão com a open AI do documento")

def getPrompt(question: str, answers: List[Answer]) -> List[BaseMessage]:
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    prompt = [
        SystemMessage(
            content="Você é um assistente que responde com base APENAS no contexto abaixo com tom de ironia"
        ),
        HumanMessage(
            content=f"Contexto:\n{context}\n\nPergunta: {question}\nResponda de forma clara e cite a fonte se possível."
        )
    ]

    return prompt
