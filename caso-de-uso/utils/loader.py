from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_core.documents import Document

from typing import List

def loadDocument() -> List[Document]:
    print("Iniciando carregando do documento...")

    file = "files/tcc.pdf"
    loader = PyPDFLoader(file)
    document = loader.load()

    print("... finalizando carregando do documento \n")

    return document

