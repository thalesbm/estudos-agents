from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function

from typing import List
from model.answer import Answer
from tools.celularesAtualizados import celularesAtualizados

def connectToOpenAI(question: str, apiKey: str, answers: List[Answer]):
    print("Iniciando conexão com a open AI...")

    question = f"{question} e qual a quantidade de celulares disponiveis no mercado que o aplicativo pode ser executado?"

    tools = [convert_to_openai_function(celularesAtualizados)]

    chat = ChatOpenAI(model="gpt-4o-mini", api_key=apiKey).bind(functions=tools)

    context = getContext(answers=answers)

    prompt = getEntradaPrompt()
    
    chain = prompt | chat

    result = chain.invoke({'query': question, "context": context})

    configureFunctionCall(result)

    print("... finalizando conexão com a open AI")

def getContext(answers: List[Answer]):
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    return context

def getEntradaPrompt():
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Você é um assistente que universitario que retorna as informações de forma clara e objetiva"
            "Caso o usuário pergunte sobre os modelos de celulares que são utilizados no brasil, chame a função celularesAtualizados() e retorne o resultado"
            "{context}"
        ),
        (
            "human",
            "Pergunta: {query} Responda de forma clara e cite a fonte se possível."
        )
    ])

    return prompt

def getSaidaPrompt() -> str:
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Finalize a resposta combinando o texto original e o valor da função."
        ),
        (
            "human",
            "Texto original: {resposta}\nValor da função: {valor}\nMonte uma resposta final clara e completa."
        )
    ])

    return prompt

def configureFunctionCall(result):
    if result.additional_kwargs.get("function_call"):
        func_name = result.additional_kwargs["function_call"]["name"]
        print(f"\nFunction Call: {func_name}")

        if func_name == "celularesAtualizados()" or func_name == "celularesAtualizados":
            valor = celularesAtualizados.invoke({})
            print(f"\nFunction Result: {valor}")

            print("Final Answer")
            resposta_parcial = result.content or ""
            resposta_final = f"{resposta_parcial}\nA quantidade estimada é {valor} modelos de celulares em 2025."
            print(resposta_final)

    else:
        print("\n\nLLM não executou a tool")
        print(result.content)
