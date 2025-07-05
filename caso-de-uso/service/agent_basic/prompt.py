from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_core.messages import BaseMessage

from typing import List

class Prompt:

    def __init__(self, question: str, context: str):
        self.question = question
        self.context = context

    def get_zero_show_prompt(self):
        prompt = [
            SystemMessage(content="Você é um aluno universitario que escreveu um TCC"),
            HumanMessage(content=f"Se baseia APENAS no contexto para sua resposta: {self.context}"),
            HumanMessage(content=f"Responda a pergunta de forma clara e objetiva: {self.question}")
        ]

        return prompt

