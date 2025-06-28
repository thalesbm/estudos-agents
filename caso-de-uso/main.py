from steps.loader import loadDocument
from steps.splitter import splitDocument
from steps.embedding import embeddingDocument
from steps.retrieval import findSimilarity
from steps.chat import connectToOpenAI

def init():
    print("bem vindo ao melhor programa do mundo")

    document = loadDocument()

    chunks = splitDocument(document=document)

    vector_store = embeddingDocument(chunks=chunks)

    question = "o que é LLM?"
    answers = findSimilarity(question=question, vector_store=vector_store)

    connectToOpenAI(question)

if __name__ == "__main__":
    init()
