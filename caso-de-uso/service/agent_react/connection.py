from tools.celulares_atualizados import celulares_atualizados
from infra.openai_client import OpenAIClientFactory
from langchain.agents import AgentExecutor, create_openai_tools_agent
from tools.celulares_atualizados import ToolManager
from service.agent_react.prompt import Prompt

import logging

logger = logging.getLogger(__name__)

class ConnectionWithReactToOpenAI:

    def __init__(self, context: str, question: str):
        self.context = context
        self.question = question

    def connect(self, api_key: str) -> str:
        logger.info("Iniciando conexão com a open AI...")

        chat = OpenAIClientFactory(api_key=api_key).create_client_with_tools(ToolManager.get_tools())

        prompt = Prompt.get_react_prompt()
        tools = ToolManager.get_tools()
        agent = create_openai_tools_agent(chat, tools, prompt)
        executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        # chain = prompt | executor

        result = executor.invoke({"query": self.question, "context": self.context})

        logger.info("===================================")
        logger.info(f"OpenAI: {result.content}")
        logger.info("===================================")

        logger.info("Finalizando conexão com a open AI")

        return result.content

        # value = self.configure_function_call(result)

        # follow_up_chain = Prompt.get_exit_prompt() | chat

        # follow_up_result = follow_up_chain.invoke({
        #     "resposta": result.content,
        #     "valor": value
        # })

        # logger.info("===================================")
        # logger.info(f"OpenAI: {follow_up_result.content}")
        # logger.info("===================================")

        # logger.info("Finalizando conexão com a open AI")

        # return follow_up_result.content

    def configure_function_call(self, result) -> str:
        if result.additional_kwargs.get("function_call"):
            func_name = result.additional_kwargs["function_call"]["name"]
            logger.info(f"Function Call: {func_name}")

            if func_name in ["celulares_atualizados()", "celulares_atualizados"]:
                valor = celulares_atualizados.invoke({})
                logger.info(f"Function Result: {valor}")
                return valor

        logger.warning("LLM não executou a tool")
        logger.warning(result.content)
        return ""
