from typing import List
from model.answer import Answer
from model.type import ConnectionType

from service.agent_basic.connection import BaseConnectionToOpenAI
from service.agent_tools.connection import ConnectionWithToolsToOpenAI

import logging
logger = logging.getLogger(__name__)

def selectServices(answers: List[Answer], question: str, api_key: str, type: ConnectionType):

    params = {
        "question": question,
        "api_key": api_key,
        "answers": answers
    }

    services = {
        ConnectionType.BASIC_CONNECTION: BaseConnectionToOpenAI(),
        ConnectionType.CONNECTION_WITH_TOOLS: ConnectionWithToolsToOpenAI()
    }

    service = services.get(type)

    if not service:
       logger.error(f"Tipo de conexão inválido: {type}")

    service.connect(**params)
