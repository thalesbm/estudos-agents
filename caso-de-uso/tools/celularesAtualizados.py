from langchain.agents import tool
import time

@tool
def celularesAtualizados() -> str:
    """
    Retorna a quantiade de modelos de celulares disponiveis no mercado em 2025
    """
    time.sleep(3)
    return "20.000"