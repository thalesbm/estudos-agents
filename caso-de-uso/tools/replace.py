from langchain.agents import tool

@tool
def replaceString(texto: str, antigo: str, novo: str) -> str:
    """
    Substitui todas as ocorrências de uma substring por outra.
    """
    return texto.replace(antigo, novo)