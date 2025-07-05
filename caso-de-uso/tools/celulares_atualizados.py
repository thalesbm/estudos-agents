from langchain_core.utils.function_calling import convert_to_openai_function

from langchain.agents import tool
import time

class ToolManager:

    @staticmethod
    def get_tools():
        return [convert_to_openai_function(celulares_atualizados)]

@tool
def celulares_atualizados() -> str:
    """
    Retorna a quantiade de modelos de celulares disponiveis no mercado em 2025
    """
    time.sleep(3)
    return "20.000"