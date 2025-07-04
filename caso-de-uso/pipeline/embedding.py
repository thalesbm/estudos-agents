from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

from typing import List

import logging

logger = logging.getLogger(__name__)

class Embedding:

    def embeddingDocument(chunks: List[Document], apiKey: str) -> Chroma:
        logger.info("Inicializando embedding do documento...")

        if not chunks:
            logger.warning("Lista de chunks vazia para embedding.")
            return None

        embeddings = OpenAIEmbeddings(openai_api_key=apiKey)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        logger.info("Finalizando embedding do documento")

        return vector_store
