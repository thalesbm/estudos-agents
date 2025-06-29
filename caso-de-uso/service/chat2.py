from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function

from langchain.agents import tool

from typing import List
from model.answer import Answer

@tool
def replaceString(context: str, antigo: str, novo: str) -> str:
    """
    Substitui todas as ocorrências de uma substring por outra.
    """
    return context.replace(antigo, novo)

def connectToOpenAI(question: str, apiKey: str, answers: List[Answer]):
    print("Iniciando conexão com a open AI...")

    tools = [convert_to_openai_function(replaceString)]

    chat = ChatOpenAI(model="gpt-4o-mini", api_key=apiKey).bind(functions=tools)

    context = getContext(answers=answers)

    prompt = getPrompt()
    
    chain = prompt | chat

    result = chain.invoke({'query': question, "context": context})

    print("\n=== RAW RESULT ===")
    print(result)

    if result.additional_kwargs.get("function_call"):
        print("\n=== FUNCTION CALL ===")
        print(result.additional_kwargs["function_call"])
    else:
        print("\n=== LLM respondeu direto ===")
        print(result.content)

    print("... finalizando conexão com a open AI")

def getContext(answers: List[Answer]):
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    return context

def getPrompt():
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Responda apenas usando a função replaceString para substituir 'LLM' por 'Large (HUGE) Language Model'."
            "Você é um assistente que SEMPRE usa a função replaceString "
            "Você é um assistente que responde com base APENAS no contexto abaixo com tom de ironia"
            "quando o usuário pede para substituir palavras em um texto. "
            "Responda apenas usando function calling."
            "Pergunta: {context}\nResponda com esse contexto."
        ),
        (
            "human",
            "Pergunta: {query}\nResponda de forma clara e cite a fonte se possível."
        )
    ])

    return prompt
