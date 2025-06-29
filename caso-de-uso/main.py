from utils.loader import loadDocument
from utils.splitter import splitDocument
from utils.embedding import embeddingDocument
from utils.retrieval import findSimilarity
from utils.openai import getOpenAIKey

# from service.chat import connectToOpenAI
from service.chat2 import connectToOpenAI

def init():
    print("bem vindo ao melhor programa do mundo")

    apiKey = getOpenAIKey()

    document = loadDocument()

    chunks = splitDocument(document=document)

    vector_store = embeddingDocument(chunks=chunks, apiKey=apiKey)

    question = "o que é LLM?"
    answers = findSimilarity(question=question, vector_store=vector_store)

    connectToOpenAI(question, apiKey=apiKey, answers=answers)

if __name__ == "__main__":
    init()
