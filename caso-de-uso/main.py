
from steps.loader import loadDocument
from steps.splitter import splitDocument
from steps.embedding import embeddingDocument

def init():
    print("bem vindo ao melhor programa do mundo")

    document = loadDocument()

    chunks = splitDocument(document=document)

    vector_store = embeddingDocument(chunks=chunks)

if __name__ == "__main__":
    init()

