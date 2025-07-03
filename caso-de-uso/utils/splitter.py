from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from typing import List

import logging

logger = logging.getLogger(__name__)

def splitDocument(documents: List[Document]) -> List[Document]:
    logger.info("Iniciando split do documento...")

    if not documents:
        logger.warning("Nenhum documento recebido para split.")
        return []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    logger.info("Finalizando split do documento")

    return chunks