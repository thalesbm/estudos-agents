from langchain_openai.chat_models import ChatOpenAI

from typing import List
from model.answer import Answer
from service.agent_basic.prompt import Prompt
from infra.openai_client import OpenAIClientFactory

import logging

logger = logging.getLogger(__name__)

class BaseConnectionToOpenAI:

    def connect(self, question: str, api_key: str, answers: List[Answer]):
        logger.info("Iniciando conexão com a open AI do documento...")

        if not answers:
            logger.warning("Nenhum contexto foi passado para o prompt.")
            return

        prompt = Prompt.getPrompt(question=question, answers=answers)

        chat = OpenAIClientFactory(api_key=api_key).create_basic_client()

        response = chat.invoke(prompt)

        logger.info("===================================")
        logger.info(f"OpenAI: {response.content}")
        logger.info("===================================")

        logger.info("Finalizando conexão com a open AI do documento")
