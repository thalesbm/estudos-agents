from langchain.prompts import ChatPromptTemplate

class Prompt:

    def get_entry_prompt():
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "Você é um assistente que universitario que retorna as informações de forma clara e objetiva"
                "Caso o usuário pergunte sobre os modelos de celulares que são utilizados no brasil, chame a função celulares_atualizados() e retorne o resultado"
                "{context}"
            ),
            (
                "human",
                "Pergunta: {query} Responda de forma clara e cite a fonte se possível."
            )
        ])

        return prompt

    def get_exit_prompt() -> str:
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "Você é um assistente que reescreve a resposta final de forma NATURAL, "
                "unindo o texto original e o valor da função. "
                "NÃO diga que chamou uma função. "
                "Apenas escreva o resultado como se fosse informação que você mesmo sabe."
            ),
            (
                "human",
                "Texto original: {resposta}\n"
                "Valor da função: {valor}\n"
                "Reescreva tudo de forma clara e natural, sem mencionar funções."
            )
        ])

        return prompt
    
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
            # ,
            # (
            #     "human",
            #     "Pergunta: {query} Responda de forma clara e cite a fonte se possível."
            # )
        ])

        return prompt