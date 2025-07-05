#### Este projeto é um agente RAG construído em Python com LangChain, que:

- [DONE] Utiliza RAG para responder perguntas baseadas em documentos PDF
- [DONE] Enriquecido com tools externas via function calling, para complementar respostas com dados dinâmicos
- [DONE] Utiliza uma interface para enviar as perguntas (Streamlit) 
- [DOING] Utiliza Ragas para avaliar se o RAG realmente responde corretamente (Context Recall, Faithfulness, Answer Relevance)
- Outros conceitos de prompt Engineering
- ReAct
- Adicione memoria

#### Comandos:

pip3 install -r requirements.txt

python3 -m venv .venv

source .venv/bin/activate

python3 -m streamlit run caso-de-uso/app.py
python3 ./caso-de-uso/app.py