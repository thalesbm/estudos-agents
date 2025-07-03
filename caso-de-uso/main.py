from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document

from utils.loader import loadDocument
from utils.splitter import splitDocument
from utils.embedding import embeddingDocument
from utils.retrieval import findSimilarity
from utils.openai import getOpenAIKey

from service.select_service import selectServices
from model.type import ConnectionType

from typing import List
import logging


def init():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("bem vindo ao melhor programa do mundo")

    question = "qual foi o aplicativo escolhido para o projeto?"

    apiKey = getOpenAIKey()

    # load document
    runnable1 = RunnableLambda(loadDocument)
    document = runnable1.invoke(None)

    # split document
    runnable2 = RunnableLambda(splitDocument)
    chunks = runnable2.invoke(document)

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
