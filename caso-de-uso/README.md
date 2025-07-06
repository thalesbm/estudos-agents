#### Este projeto é um agente RAG construído em Python com LangChain, que:

- [DONE] Utiliza RAG para responder perguntas baseadas em documentos PDF
- [DONE] Enriquecido com tools externas via function calling, para complementar respostas com dados dinâmicos
- [DONE] Utiliza uma interface para enviar as perguntas (Streamlit) 
- [DONE] Utiliza Ragas para avaliar se o RAG realmente responde corretamente (Context Recall, Faithfulness, Answer Relevance)
- [DOING] Utiliza outros conceitos de prompt Engineering
- ReAct
- Adicione memoria

#### Código:

Na classe `MainController` altera a `connection_type` e o prompt_type para mudar o tipo de conexão ou o tipo de `prompt_type`:

```python
result = SelectServices.run(
    answers=chunks,
    question=question, 
    api_key=self.api_key, 
    connection_type=ConnectionType.BASIC_CONNECTION,
    prompt_type=PromptType.ZERO_SHOT_PROMPT
)
```

#### Comandos:
```bash
pip3 install -r requirements.txt

python3 -m venv .venv

source .venv/bin/activate

python3 -m streamlit run caso-de-uso/app.py

python3 ./caso-de-uso/app.py
```