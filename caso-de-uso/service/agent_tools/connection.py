from langchain_openai.chat_models import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function

from typing import List
from model.answer import Answer
from tools.celularesAtualizados import celularesAtualizados
from infra.openai_client import OpenAIClientFactory

from service.agent_tools.prompt import Prompt

import logging

logger = logging.getLogger(__name__)

class ConnectionWithToolsToOpenAI:

    def connect(self, question: str, api_key: str, answers: List[Answer]):
        logger.info("Iniciando conexão com a open AI...")

        if not answers:
            logger.warning("Nenhum contexto fornecido. Verifique se a lista de answers está vazia.")
            return

        finalQuestion = f"{question} e qual a quantidade de celulares disponiveis no mercado que o aplicativo pode ser executado?"

        chat = OpenAIClientFactory(api_key=api_key).create_client_with_tools()

        context = self.get_context(answers=answers)

        prompt = Prompt.get_entry_prompt()
        
        chain = prompt | chat

        result = chain.invoke({'query': finalQuestion, "context": context})

        value = self.configure_function_call(result)

        follow_up_chain = Prompt.get_exit_prompt() | chat

        follow_up_result = follow_up_chain.invoke({
            "resposta": result.content,
            "valor": value
        })

        logger.info("===================================")
        logger.info(f"OpenAI: {follow_up_result.content}")
        logger.info("===================================")

        logger.info("Finalizando conexão com a open AI")

    def get_context(self, answers: List[Answer]):
        context = ""
        for ans in answers:
            context += ans.content + "\n---\n"

        return context

    def configure_function_call(self, result) -> str:
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
