from typing import List
from model.answer import Answer
from model.connection_type import ConnectionType
from model.prompt_type import PromptType

from service.agent_basic.connection import BaseConnectionToOpenAI
from service.agent_tools.connection import ConnectionWithToolsToOpenAI

import logging
logger = logging.getLogger(__name__)

class SelectServices:

    def run(
        answers: List[Answer], 
        question: str, 
        api_key: str, 
        connection_type: ConnectionType,
        prompt_type: PromptType
    ):

        if not answers:
            logger.warning("Nenhum contexto fornecido. Verifique se a lista de answers está vazia.")
            return

        params = {
            "context": get_context(answers),
            "question": question,
            "api_key": api_key,
        }

        services = {
            ConnectionType.BASIC_CONNECTION: BaseConnectionToOpenAI(),
            ConnectionType.CONNECTION_WITH_TOOLS: ConnectionWithToolsToOpenAI()
        }

        service = services.get(connection_type)

        if not service:
            logger.error(f"Tipo de conexão inválido: {connection_type}")

        return service.connect(**params)
        

def get_context(answers: List[Answer]) -> str:
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    return context
