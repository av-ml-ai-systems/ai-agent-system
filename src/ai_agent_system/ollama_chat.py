"""
Module: ollama_chat.py

Location:
    src/ai_agent_system/

Purpose:
    Provides a concrete ChatModel implementation using LangChain ChatOllama.

The Agent does not depend on LangChain directly.
This adapter isolates framework-specific details.
"""

from langchain_core.messages import AIMessage, BaseMessage
from langchain_ollama import ChatOllama

from .chat_model import ChatModel


class OllamaChat(ChatModel):
    """
    ChatModel implementation using a local Ollama server.
    """

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
    ) -> None:
        self._chat_model = ChatOllama(
            model=model,
            base_url=base_url,
        )

    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> AIMessage:
        """
        Generate a response using the chat model.
        """

        response = self._chat_model.invoke(messages)

        return response
