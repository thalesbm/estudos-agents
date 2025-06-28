import os
from dotenv import load_dotenv

def getOpenAIKey():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    print(f"|{api_key}|")

    return api_key

