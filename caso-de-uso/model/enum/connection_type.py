from enum import Enum

class ConnectionType(Enum):
    BASIC_CONNECTION = "conexao-simples-llm"
    CONNECTION_WITH_TOOLS = "conexao-com-tool"

    def __getitem__(self, name):
        return super().__getitem__(name)