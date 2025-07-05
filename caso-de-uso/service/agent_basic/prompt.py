from langchain.schema import HumanMessage, SystemMessage
from langchain_core.messages import BaseMessage

from typing import List
from model.answer import Answer

class Prompt:
    def getPrompt(question: str, answers: List[Answer]) -> List[BaseMessage]:
        context = ""
        for ans in answers:
            context += ans.content + "\n---\n"

        prompt = [
            SystemMessage(
                content="Você é um assistente que responde com base APENAS no contexto abaixo com tom de ironia"
            ),
            HumanMessage(
                content=f"Contexto:\n{context}\n\nPergunta: {question}\nResponda de forma clara e cite a fonte se possível."
            )
        ]

        return prompt
