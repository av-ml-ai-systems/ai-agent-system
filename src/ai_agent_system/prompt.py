"""
Module: prompt.py

Location:
    src/ai_agent_system/

Purpose:
    Defines the abstraction for creating prompts.
"""

from abc import ABC, abstractmethod

from langchain_core.messages import BaseMessage


class PromptTemplate(ABC):
    """
    Abstract prompt template contract.

    Implementations are responsible for transforming
    application data into model messages.
    """

    @abstractmethod
    def format_messages(
        self,
        **kwargs: str,
    ) -> list[BaseMessage]:
        """
        Create messages from input variables.

        Parameters
        ----------
        kwargs:
            Variables required by the prompt.

        Returns
        -------
        list[BaseMessage]
            Messages ready for a ChatModel.
        """

        pass
