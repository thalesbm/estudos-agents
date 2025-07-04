from langchain_openai.chat_models import ChatOpenAI

from typing import List
from model.answer import Answer
from service.agent_basic.prompt import getPrompt

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
