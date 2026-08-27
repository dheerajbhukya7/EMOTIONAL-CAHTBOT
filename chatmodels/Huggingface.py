import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv(override=True)

print("HF token loaded:", bool(os.getenv("HF_TOKEN")))

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Write a short poem about AI.")

print(response.content)