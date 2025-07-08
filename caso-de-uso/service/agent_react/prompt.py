from langchain.prompts import ChatPromptTemplate

class Prompt:

    def get_react_prompt():
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "Você é um assistente que universitario que retorna as informações de forma clara e objetiva"
                "Sempre explique seu raciocínio (Thought), execute uma ação (Action) e observe o resultado (Observation). "
                "Finalize apenas quando tiver uma resposta completa."
                "Caso o usuário pergunte sobre os modelos de celulares que são utilizados no brasil, chame a função celulares_atualizados() e retorne o resultado"
                "{context}"
                "{agent_scratchpad}"
            ),
            (
                "user",
                "{query}"
            )
        ])

        return prompt