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

    def __init__(self):
        logger.info("Iniciando setup do RAG...")

        self.api_key = Key.get_openai_key()

        document = Loader.load_document()
        chunks = Splitter.split_document(document)
        self.vector_store = Embedding.embedding_document(chunks, self.api_key)

        logger.info("Setup do RAG finalizado!")

    def run(self, question: str, callback):
        logger.info(f"Pergunta recebida: {question}")

        # api_key = Key.get_openai_key()

        # # load
        # document = RunnableLambda(Loader.load_document)
        
        # # split
        # split = RunnableLambda(Splitter.split_document)

        # # embedding
        # embedding = RunnableLambda(Embedding.embedding_document).bind(api_key=api_key)

        # # retrieval
        # # answers = RunnableLambda(Retrieval.retrieve_similar_documents).bind(question=question)
        
        # retrieval_chain = document | split | embedding
        # vector_store = retrieval_chain.invoke(None)
        # callback(chunks)

        # retrieval
        chunks = Retrieval.retrieve_similar_documents(
            vector_store=self.vector_store, 
            question=question
        )
        callback(chunks)

        # open ai
        result = SelectServices.run(
            answers=chunks,
            question=question, 
            api_key=self.api_key, 
            type=ConnectionType.BASIC_CONNECTION
        )

        return result