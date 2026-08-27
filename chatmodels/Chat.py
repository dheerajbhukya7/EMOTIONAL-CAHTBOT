from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

# Check key
if not os.getenv("MISTRAL_API_KEY"):
    raise ValueError("MISTRAL_API_KEY is missing")

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

response = model.invoke(
    "Write a short poem about AI."
)

print(response.content)