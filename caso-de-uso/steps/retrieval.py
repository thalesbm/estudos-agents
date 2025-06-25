from langchain_community.vectorstores.chroma import Chroma

from model.answer import Answer

from typing import List

def findSimilarity(question: str, vector_store: Chroma) -> List[Answer]: 
    print("Iniciando retrieval do documento...")

    docs = vector_store.similarity_search(question, k=3)

    answers = []

    for doc in docs:
        answers.append(Answer(content=doc.page_content, metadata=doc.metadata))

    print("... finalizando retrieval do documento \n")

    return answers
