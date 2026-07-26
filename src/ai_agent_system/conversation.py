"""
Module: conversation.py

Location:
    src/ai_agent_system/

Purpose:
    Defines conversation state management.
"""

from langchain_core.messages import BaseMessage


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

    def messages(self) -> list[BaseMessage]:
        """
        Return stored conversation messages.
        """

        return self._messages.copy()
