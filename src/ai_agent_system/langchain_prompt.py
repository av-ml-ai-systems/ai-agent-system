"""
Module: langchain_prompt.py

Location:
    src/ai_agent_system/

Purpose:
    Provides a concrete PromptTemplate implementation using LangChain
    ChatPromptTemplate.
"""

from langchain_core.messages import BaseMessage
from langchain_core.prompts import ChatPromptTemplate

from .prompt import PromptTemplate


class LangChainPrompt(PromptTemplate):
    """
    PromptTemplate implementation using LangChain.
    """

    def __init__(
        self,
        system_message: str,
        human_template: str,
    ) -> None:

        self._prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    system_message,
                ),
                (
                    "human",
                    human_template,
                ),
            ]
        )

    def format_messages(
        self,
        **kwargs: str,
    ) -> list[BaseMessage]:
        """
        Generate messages from template variables.
        """

        return self._prompt.format_messages(**kwargs)
