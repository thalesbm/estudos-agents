from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

from typing import List

import logging

logger = logging.getLogger(__name__)

class Embedding:

    def embedding_document(chunks: List[Document], api_key: str) -> Chroma:
        logger.info("Inicializando embedding do documento...")

        if not chunks:
            logger.warning("Lista de chunks vazia para embedding.")
            return None

        embeddings = OpenAIEmbeddings(openai_api_key=api_key)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./files/db"
        )
        vector_store.persist()

        logger.info("Finalizando embedding do documento")

        return vector_store
