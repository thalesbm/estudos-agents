from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores.chroma import Chroma

def connectToOpenAI(question: str, apiKey: str, vector_store: Chroma):
    print("Iniciando conexão com a open AI do documento...")

    chat = ChatOpenAI(model="gpt-4o-mini")

    vector = vector_store.as_retriever(search_type='mmr')

    chat_chain = RetrievalQA.from_chain_type(
        llm=chat,
        retriever=vector,
    )

    resposta = chat_chain.invoke({'query': question})
    print(resposta['result'])

    print("... finalizando conexão com a open AI do documento")
