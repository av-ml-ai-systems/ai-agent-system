"""
Module: chat_model.py

Location:
    src/ai_agent_system/

Purpose:
    Defines the abstraction contract for conversational language models.

The Agent depends on this interface instead of depending on
specific frameworks such as LangChain or providers such as Ollama.
"""

from abc import ABC, abstractmethod

from langchain_core.messages import BaseMessage


class ChatModel(ABC):
    """
    Abstract interface for chat-based language models.
    """

    @abstractmethod
    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> BaseMessage:
        """
        Generate a response from a list of messages.

        Parameters
        ----------
        messages:
            Conversation messages.

        Returns
        -------
        BaseMessage:
            Generated model response.
        """
        pass