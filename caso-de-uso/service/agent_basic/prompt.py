from langchain.schema import HumanMessage, SystemMessage
from langchain_core.messages import BaseMessage

from typing import List

class Prompt:
    def getPrompt(question: str, context: str) -> List[BaseMessage]:

        prompt = [
            SystemMessage(
                content="Você é um assistente que responde de forma simples e objetiva"
            ),
            HumanMessage(
                content=f"Contexto:\n{context}\n\nPergunta: {question}\nResponda de forma clara e cite a fonte se possível."
            )
        ]

        return prompt
