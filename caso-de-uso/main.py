from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document

from pipeline.loader import Loader
from pipeline.splitter import Splitter
from pipeline.embedding import Embedding
from pipeline.retrieval import Retrieval
from pipeline.openai import Key

from service.select_service import selectServices
from model.type import ConnectionType

import logging

def init():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Bem vindo ao melhor mini agente do mundo")

    question = "qual foi o aplicativo escolhido para o projeto?"

    apiKey = Key.getOpenAIKey()

    # load
    document = RunnableLambda(Loader.loadDocument)
    
    # split
    chunks = RunnableLambda(Splitter.splitDocument)

    # embedding
    vector_store = RunnableLambda(Embedding.embeddingDocument).bind(apiKey=apiKey)

    # retrieval
    answers = RunnableLambda(Retrieval.retrieveSimilarDocuments).bind(question=question)

    # open AI
    openAI = RunnableLambda(selectServices).bind(question=question, apiKey=apiKey, type=ConnectionType.CONNECTION_WITH_TOOLS)
    
    pipeline = document | chunks | vector_store | answers | openAI
    chunks = pipeline.invoke(None)

if __name__ == "__main__":
    init()
