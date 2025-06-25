from steps.loader import loadDocument
from steps.splitter import splitDocument
from steps.embedding import embeddingDocument
from steps.retrieval import findSimilarity

from model.answer import Answer

from typing import List

def init():
    print("bem vindo ao melhor programa do mundo")

    document = loadDocument()

    chunks = splitDocument(document=document)

    vector_store = embeddingDocument(chunks=chunks)

    question = "o que é LLM?"
    answers = findSimilarity(question=question, vector_store=vector_store)

    printAnswers(answers=answers)

def printAnswers(answers: List[Answer]): 
    for item in answers:
        print(item.content)
        print(item.metadata)
        print("\n")

if __name__ == "__main__":
    init()
