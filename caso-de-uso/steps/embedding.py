from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

from typing import List

def embeddingDocument(chunks: List[Document]) -> Chroma:
    print("Inicializando embedding do documento...")

    embeddings = OpenAIEmbeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    print("... finalizando embedding do documento \n")

    return vector_store
