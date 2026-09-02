import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)


# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("MISTRAL_API_KEY")


# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
)


# Check API key
if not api_key:
    st.error("MISTRAL_API_KEY is missing from your .env file.")
    st.stop()


# Model
@st.cache_resource
def get_model():
    return ChatMistralAI(
        model="open-mistral-7b",  # Free tier model
        temperature=0.7,
        api_key=api_key,
    )


# Title
st.title("🤖 AI Chatbot")
st.caption("Powered by Mistral AI")


# Sidebar
with st.sidebar:

    st.header("⚙️ Chatbot Settings")

    personality = st.selectbox(
        "Choose personality",
        [
            "😡 Angry AI",
            "😂 Funny AI",
            "😏 Sarcastic AI",
        ],
    )

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = [
            SystemMessage(content="")
        ]

        st.rerun()


# System prompt
if personality == "😡 Angry AI":

    system_prompt = """
You are an angry AI assistant.

You are impatient, irritated and dramatic,
but you must still be helpful and respectful.

Never use hateful or threatening language.
"""

elif personality == "😂 Funny AI":

    system_prompt = """
You are a funny AI assistant.

Be humorous, playful and entertaining.
Use jokes when appropriate, but always answer
the user's question correctly.
"""

else:

    system_prompt = """
You are a sarcastic AI assistant.

Use clever and witty sarcasm.
Keep the sarcasm playful rather than offensive.
Always answer the user's question helpfully.
"""


# Initialize chat
if (
    "messages" not in st.session_state
    or st.session_state.get("personality") != personality
):

    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

    st.session_state.personality = personality


# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


# User input
prompt = st.chat_input("Type your message...")


if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Get model only when needed
    model = get_model()

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.invoke(
                    st.session_state.messages
                )

                answer = response.content

                if not isinstance(answer, str):
                    answer = str(answer)

                st.markdown(answer)

                st.session_state.messages.append(
                    AIMessage(content=answer)
                )

            except Exception as e:

                st.error(f"Error: {e}")