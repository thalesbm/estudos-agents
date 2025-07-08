from langchain.prompts import ChatPromptTemplate

class Prompt:

    def get_entry_prompt():
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "Você é um assistente que universitario que retorna as informações de forma clara e objetiva"
                "Se o usuário perguntar sobre a quantidade de celulares em que o aplicativo pode rodar, OBRIGATORIAMENTE chame a função celulares_atualizados. "
                "NUNCA tente responder com conhecimento próprio, só use a função celulares_atualizados.\n"
                "Contexto: {context}\n"
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
