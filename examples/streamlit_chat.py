"""
Module: streamlit_chat.py

Location:
    examples/

Purpose:
    Demonstrate the AI Agent through a Streamlit interface.
"""

import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Agent System", page_icon="🤖")

st.title("🤖 AI Agent System")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Type your message...")

if user_message:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    response = requests.post(
        API_URL,
        json={"message": user_message},
        timeout=600,
    )

    assistant_message = response.json()["response"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_message)
