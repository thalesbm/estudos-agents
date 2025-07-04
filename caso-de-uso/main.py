from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document

from utils.loader import loadDocument
from utils.splitter import splitDocument
from utils.embedding import embeddingDocument
from utils.retrieval import retrieveSimilarDocuments
from utils.openai import getOpenAIKey

from service.select_service import selectServices
from model.type import ConnectionType

import logging

def init():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Bem vindo ao melhor mini agente do mundo")

    question = "qual foi o aplicativo escolhido para o projeto?"

    apiKey = getOpenAIKey()

    # load
    document = RunnableLambda(loadDocument)
    
    # split
    chunks = RunnableLambda(splitDocument)

    # embedding
    vector_store = RunnableLambda(embeddingDocument).bind(apiKey=apiKey)

    # retrieval
    answers = RunnableLambda(retrieveSimilarDocuments).bind(question=question)

    # open AI
    openAI = RunnableLambda(selectServices).bind(question=question, apiKey=apiKey, type=ConnectionType.BASIC_CONNECTION)
    
    pipeline = document | chunks | vector_store | answers | openAI
    chunks = pipeline.invoke(None)

if __name__ == "__main__":
    init()
