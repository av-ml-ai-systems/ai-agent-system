"""
Module: conversation.py

Location:
    src/ai_agent_system/

Purpose:
    Defines conversation state management.
"""

from langchain_core.messages import AIMessage
from langchain_core.messages import BaseMessage
from langchain_core.messages import HumanMessage


class Conversation:
    """
    Stores conversation history.

    This class is responsible only for maintaining messages.
    It does not generate responses.
    """

    def __init__(self) -> None:
        self._messages: list[BaseMessage] = []

    def add_message(
        self,
        message: BaseMessage,
    ) -> None:
        """
        Add a message to the conversation.
        """

        self._messages.append(message)

    def add_user_message(
        self,
        content: str,
    ) -> None:
        """
        Add a HumanMessage to the conversation.
        """

        self.add_message(
            HumanMessage(content=content),
        )

    def add_ai_message(
        self,
        content: str,
    ) -> None:
        """
        Add an AIMessage to the conversation.
        """

        self.add_message(
            AIMessage(content=content),
        )

    def messages(self) -> list[BaseMessage]:
        """
        Return the stored conversation history.
        """

        return self._messages.copy()

    def clear(self) -> None:
        """
        Remove all stored messages.
        """

        self._messages.clear()
