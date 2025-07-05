from service.agent_basic.prompt import Prompt
from infra.openai_client import OpenAIClientFactory

import logging

logger = logging.getLogger(__name__)

class BaseConnectionToOpenAI:

    def connect(self, context: str, question: str, api_key: str):
        logger.info("Iniciando conexão com a open AI do documento...")

        prompt = Prompt.getPrompt(question=question, context=context)

        chat = OpenAIClientFactory(api_key=api_key).create_basic_client()

        response = chat.invoke(prompt)

        logger.info("===================================")
        logger.info(f"OpenAI: {response.content}")
        logger.info("===================================")

        logger.info("Finalizando conexão com a open AI do documento")
