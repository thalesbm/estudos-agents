from typing import List
from model.answer import Answer
from model.type import ConnectionType

from service.agent_basic.connection import connectToOpenAI as basicConnetion
from service.agent_tools.connection import connectToOpenAI as toolsConnection

import logging
logger = logging.getLogger(__name__)

def selectServices(answers: List[Answer], question: str, api_key: str, type: ConnectionType):

    params = {
        "question": question,
        "api_key": api_key,
        "answers": answers
    }

    services = {
        ConnectionType.BASIC_CONNECTION: basicConnetion,
        ConnectionType.CONNECTION_WITH_TOOLS: toolsConnection
    }

    service = services.get(type)

    if not service:
       logger.error(f"Tipo de conexão inválido: {type}")

    service(**params)
