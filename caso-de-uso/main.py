from utils.loader import loadDocument
from utils.splitter import splitDocument
from utils.embedding import embeddingDocument
from utils.retrieval import findSimilarity
from utils.openai import getOpenAIKey

from service.select_service import selectServices
from model.type import ConnectionType

def init():
    print("bem vindo ao melhor programa do mundo")

    question = "qual foi o aplicativo escolhido para o projeto?"

    apiKey = getOpenAIKey()

    document = loadDocument()

    chunks = splitDocument(
        document=document
    )

    vector_store = embeddingDocument(
        chunks=chunks, 
        apiKey=apiKey
    )

    answers = findSimilarity(
        question=question, 
        vector_store=vector_store
    )

    selectServices(
        question=question, 
        apiKey=apiKey, 
        answers=answers,
        type=ConnectionType.CONNECTION_WITH_TOOLS
    )

if __name__ == "__main__":
    init()
