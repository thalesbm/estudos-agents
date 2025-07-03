from typing import List
from model.answer import Answer
from model.type import ConnectionType

from service.basic_connection import connectToOpenAI as basicConnetion
from service.tools_connection import connectToOpenAI as toolsConnection

def selectServices(question: str, apiKey: str, answers: List[Answer], type: ConnectionType):
    if type == ConnectionType.BASIC_CONNECTION:
        
        basicConnetion(
            question=question,
            apiKey=apiKey,
            answers=answers
        )

    elif type == ConnectionType.CONNECTION_WITH_TOOLS:

        toolsConnection(     
            question=question,
            apiKey=apiKey,
            answers=answers
        )

