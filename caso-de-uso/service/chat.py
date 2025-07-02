from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from typing import List
from model.answer import Answer

def simpleConnectionToOpenAI(question: str, apiKey: str, answers: List[Answer]):
    print("Iniciando conexão com a open AI do documento...\n")

    chat = ChatOpenAI(model="gpt-4o-mini", api_key=apiKey)

    prompt = getPrompt(question=question, answers=answers)
    
    response = chat.invoke(prompt)

    print(response.content)

    print("\n... finalizando conexão com a open AI do documento")

def getPrompt(question: str, answers: List[Answer]):
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
