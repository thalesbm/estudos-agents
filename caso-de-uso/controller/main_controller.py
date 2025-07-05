from langchain_core.runnables import RunnableLambda

from pipeline.loader import Loader
from pipeline.splitter import Splitter
from pipeline.embedding import Embedding
from pipeline.retrieval import Retrieval
from pipeline.openai import Key

from service.select_service import SelectServices
from model.type import ConnectionType

import logging

logger = logging.getLogger(__name__)

class MainController:

    def run(question: str):
        logger.info("Iniciando RAG...")

        api_key = Key.get_openai_key()

        # load
        document = RunnableLambda(Loader.load_document)
        
        # split
        chunks = RunnableLambda(Splitter.split_document)

        # embedding
        vector_store = RunnableLambda(Embedding.embedding_document).bind(api_key=api_key)

        # retrieval
        answers = RunnableLambda(Retrieval.retrieve_similar_documents).bind(question=question)

        # open AI
        openAI = RunnableLambda(SelectServices.run).bind(question=question, api_key=api_key, type=ConnectionType.CONNECTION_WITH_TOOLS)
        
        pipeline = document | chunks | vector_store | answers | openAI
        chunks = pipeline.invoke(None)

        logger.info("RAG finalizado")