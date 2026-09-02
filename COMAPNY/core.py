from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
import os

load_dotenv()


model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY"),
)

response = model.invoke("Hello, how are you?")

print(response.content)

