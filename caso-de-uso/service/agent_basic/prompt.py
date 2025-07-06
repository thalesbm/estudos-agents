from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_core.messages import BaseMessage

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
    
    def get_few_show_prompt(self):
        prompt = [
            SystemMessage(content="Você é um aluno universitario que escreveu um TCC"),

            HumanMessage(content="Qual foi o objetivo do seu TCC?"),
            AIMessage(content="O objetivo do meu TCC foi desenvolver um app para ensino de física."),

            HumanMessage(content="Que plataforma foi usada para o desenvolvimento?"),
            AIMessage(content="Utilizei a plataforma Intel XDK."),

            HumanMessage(content="Qual foi o ano de o projeto foi apresentado?"),
            AIMessage(content="O ano foi 2014."),

            HumanMessage(content=f"Se baseia APENAS no contexto para sua resposta: {self.context}"),
            HumanMessage(content=f"Responda a pergunta de forma clara e objetiva: {self.question}"),
        ]

        return prompt

