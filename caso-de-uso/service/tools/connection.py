from langchain_openai.chat_models import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function

from typing import List
from model.answer import Answer
from tools.celularesAtualizados import celularesAtualizados

from service.tools.prompt import getEntradaPrompt
from service.tools.prompt import getSaidaPrompt

import logging

logger = logging.getLogger(__name__)

def connectToOpenAI(question: str, apiKey: str, answers: List[Answer]):
    logger.info("Iniciando conexão com a open AI...")

    if not answers:
        logger.warning("Nenhum contexto fornecido. Verifique se a lista de answers está vazia.")
        return

    finalQuestion = f"{question} e qual a quantidade de celulares disponiveis no mercado que o aplicativo pode ser executado?"

    chat = configureOpenAI(apiKey=apiKey)

    context = getContext(answers=answers)

    prompt = getEntradaPrompt()
    
    chain = prompt | chat

    result = chain.invoke({'query': finalQuestion, "context": context})

    value = configureFunctionCall(result)

    follow_up_chain = getSaidaPrompt() | chat

    follow_up_result = follow_up_chain.invoke({
        "resposta": result.content,
        "valor": value
    })

    logger.info("===================================")
    logger.info(f"OpenAI: {follow_up_result.content}")
    logger.info("===================================")

    logger.info("Finalizando conexão com a open AI")

def configureOpenAI(apiKey: str) -> ChatOpenAI:
    tools = [convert_to_openai_function(celularesAtualizados)]
    return ChatOpenAI(model="gpt-4o-mini", api_key=apiKey).bind(functions=tools)

def getContext(answers: List[Answer]):
    context = ""
    for ans in answers:
        context += ans.content + "\n---\n"

    return context

def configureFunctionCall(result) -> str:
    if result.additional_kwargs.get("function_call"):
        func_name = result.additional_kwargs["function_call"]["name"]
        logger.info(f"Function Call: {func_name}")

        if func_name == "celularesAtualizados()" or func_name == "celularesAtualizados":
            valor = celularesAtualizados.invoke({})
            logger.info(f"Function Result: {valor}")
            return valor

    else:
        logger.warning("LLM não executou a tool")
        logger.warning(result.content)

        return ""
