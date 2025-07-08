from typing import List
from model.answer import Answer
from model.enum.connection_type import ConnectionType
from model.enum.prompt_type import PromptType

from service.agent_basic.connection import BaseConnectionToOpenAI
from service.agent_tools.connection import ConnectionWithToolsToOpenAI

import logging
logger = logging.getLogger(__name__)

class SelectServices:

    def run(
        answers: List[Answer], 
        question: str, 
        api_key: str, 
        connection_type: str,
        prompt_type: str
    ):

        logger.info("Inicializando SelectServices")

        if not answers:
            logger.warning("Nenhum contexto fornecido. Verifique se a lista de answers está vazia.")
            return

        result = ""

        type = ConnectionType(connection_type)
        print(type)
        if type == ConnectionType.BASIC_CONNECTION:
            result = BaseConnectionToOpenAI(
                context=get_context(answers), 
                question=question, 
                prompt_type=PromptType(prompt_type)
            ).connect(api_key=api_key)

        elif type == ConnectionType.CONNECTION_WITH_TOOLS:
            result = ConnectionWithToolsToOpenAI(
                context=get_context(answers), 
                question=question, 
            ).connect(api_key=api_key)

        logger.info("Finalizado SelectServices")    

        return result
        

def get_context(answers: List[Answer]) -> str:
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    return context
