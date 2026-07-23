"""
Module: agent.py

Location:
    src/ai_agent_system/

Purpose:
    Defines the Agent class, which coordinates user interaction
    with a chat-based language model and conversation state.

The Agent depends only on abstractions:
- ChatModel
- Conversation

It does not depend on LangChain providers or Ollama directly.
"""

from langchain_core.messages import AIMessage, HumanMessage

from ai_agent_system.chat_model import ChatModel
from ai_agent_system.conversation import Conversation


class Agent:
    """
    Educational AI Agent.

    Responsibilities:
    - Receive user input.
    - Manage conversation state.
    - Delegate generation to ChatModel.
    - Store generated responses.
    """


    def __init__(
        self,
        chat_model: ChatModel,
        conversation: Conversation,
    ) -> None:
        """
        Initialize the Agent.

        Parameters
        ----------
        chat_model:
            Conversational model implementation.

        conversation:
            Conversation state manager.
        """

        self.chat_model = chat_model
        self.conversation = conversation


    def answer(
        self,
        question: str,
    ) -> str:
        """
        Generate a response while maintaining conversation history.

        Parameters
        ----------
        question:
            User input.

        Returns
        -------
        str
            Generated response.
        """

        human_message = HumanMessage(
            content=question,
        )

        self.conversation.add_message(
            human_message,
        )

        response: AIMessage = self.chat_model.invoke(
            self.conversation.messages()
        )

        self.conversation.add_message(
            response,
        )

        return response.content