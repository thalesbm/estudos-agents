from typing import List
from model.answer import Answer
from model.type import ConnectionType

from service.basic.connection import connectToOpenAI as basicConnetion
from service.tools.connection import connectToOpenAI as toolsConnection

import logging
logger = logging.getLogger(__name__)

def selectServices(answers: List[Answer], question: str, apiKey: str, type: ConnectionType):

    params = {
        "question": question,
        "apiKey": apiKey,
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
