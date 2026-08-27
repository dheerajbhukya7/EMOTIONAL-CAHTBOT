from dotenv import load_dotenv
from pathlib import Path
import os

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

# Check API key
if not os.getenv("MISTRAL_API_KEY"):
    raise ValueError("MISTRAL_API_KEY is missing")


# Create model
model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)


# Choose chatbot personality
print("Choose a model from the following options:")
print("Press 1 for Angry AI Chatbot")
print("Press 2 for Funny AI Chatbot")
print("Press 3 for Sarcastic AI Chatbot")

model_choice = input("Enter your choice (1, 2, or 3): ")


if model_choice == "1":
    system_message = SystemMessage(
        content="You are an angry AI assistant. "
                "You should respond in an angry, frustrated, impatient, "
                "but still helpful and safe manner."
    )

elif model_choice == "2":
    system_message = SystemMessage(
        content="You are a funny AI assistant. "
                "Make your responses humorous, playful, and entertaining "
                "while still being helpful."
    )

elif model_choice == "3":
    system_message = SystemMessage(
        content="You are a sarcastic AI assistant. "
                "Respond with clever, witty sarcasm while remaining helpful "
                "and respectful."
    )

else:
    print("Invalid choice. Please select 1, 2, or 3.")
    exit()


# Start conversation with the selected system message
messages = [system_message]


print(
    "___________________welcome to the chatbot____"
    "Type 'exit' to quit"
    "_________________________"
)


while True:

    prompt = input("You: ")

    # Check exit BEFORE adding it to conversation
    if prompt.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    # Add user's message
    messages.append(HumanMessage(content=prompt))

    # Get AI response
    response = model.invoke(messages)

    # Add AI response to conversation
    messages.append(AIMessage(content=response.content))

    # Display response
    print("Bot:", response.content)