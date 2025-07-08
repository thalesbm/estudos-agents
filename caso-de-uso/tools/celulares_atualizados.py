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
    Retorna a quantidade de modelos de celulares disponíveis no mercado em 2025.
    Use essa função sempre que o usuário perguntar sobre celulares compatíveis ou disponíveis.
    """
    time.sleep(3)
    return "20.000"