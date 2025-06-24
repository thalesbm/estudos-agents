from langchain_community.document_loaders.pdf import PyPDFLoader

def loadDocument():
    print("Iniciando carregando do documento...")

    file = "files/LLM.pdf"
    loader = PyPDFLoader(file)
    document = loader.load()

    print("... finalizando carregando do documento")

    return document

