from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts =[
    "You are a helpful assistant.",
    "What is the capital of France?"
    "Hello, my dog is cute"
]

vectors = embeddings.embed_documents(texts)

print(vectors)