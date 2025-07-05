from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_core.messages import BaseMessage

from typing import List

class Prompt:

    def __init__(self, question: str, context: str):
        self.question = question
        self.context = context

    def get_default_prompt(self) -> List[BaseMessage]:
        prompt = [
            SystemMessage(content="Você é um assistente que responde de forma simples e objetiva"),
            HumanMessage(content=f"Contexto:\n{self.context}\n\nPergunta: {self.question}\nResponda de forma clara e cite a fonte se possível.")
        ]

        return prompt

    def get_zero_show_prompt(self):
        prompt = [
            SystemMessage(content="Você é um aluno universitario que escreveu um TCC"),
            HumanMessage(content=f"Se baseia APENAS no contexto para sua resposta: {self.context}"),
            HumanMessage(content=f"Responda a pergunta de forma clara e objetiva: {self.question}")
        ]

        return prompt

