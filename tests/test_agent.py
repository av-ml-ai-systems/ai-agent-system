"""
Module: test_agent.py

Location:
    tests/test_agent.py

Purpose:
    Unit tests for the Agent class.

The tests verify:
- Agent delegates generation to ChatModel.
- Agent manages conversation state.
- Previous messages are preserved.
- ChatModel receives the complete conversation history.
"""

from langchain_core.messages import AIMessage, BaseMessage

from ai_agent_system.agent import Agent
from ai_agent_system.chat_model import ChatModel
from ai_agent_system.conversation import Conversation


class FakeChatModel(ChatModel):
    """
    Fake ChatModel implementation.

    This class replaces the real model during testing.

    It provides deterministic responses and allows
    verification of message history handling.
    """

    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> AIMessage:
        """
        Generate a fake response.

        Parameters
        ----------
        messages:
            Conversation history received by the model.

        Returns
        -------
        AIMessage
            Fixed response.
        """

        return AIMessage(
            content="This is a fake response."
        )


class MemoryAwareFakeChatModel(ChatModel):
    """
    Fake ChatModel that simulates memory usage.

    It checks whether previous conversation messages
    are available.
    """

    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> AIMessage:
        """
        Generate a response based on message history.
        """

        if len(messages) >= 3:
            return AIMessage(
                content="Your name is Alvaro."
            )

        return AIMessage(
            content="I do not know your name."
        )


def test_agent_returns_chat_model_response() -> None:
    """
    Verify Agent returns the ChatModel response.
    """

    fake_chat_model = FakeChatModel()

    conversation = Conversation()

    agent = Agent(
        fake_chat_model,
        conversation,
    )

    response = agent.answer(
        "What is artificial intelligence?"
    )

    assert response == "This is a fake response."


def test_agent_updates_conversation_state() -> None:
    """
    Verify Agent stores user and assistant messages.
    """

    fake_chat_model = FakeChatModel()

    conversation = Conversation()

    agent = Agent(
        fake_chat_model,
        conversation,
    )

    agent.answer(
        "Hello"
    )

    messages = conversation.messages()

    assert len(messages) == 2
    assert messages[0].content == "Hello"
    assert messages[1].content == "This is a fake response."


def test_agent_uses_previous_conversation_context() -> None:
    """
    Verify that previous messages are available to ChatModel.
    """

    memory_model = MemoryAwareFakeChatModel()

    conversation = Conversation()

    agent = Agent(
        memory_model,
        conversation,
    )

    first_response = agent.answer(
        "My name is Alvaro."
    )

    second_response = agent.answer(
        "What is my name?"
    )

    assert first_response == "I do not know your name."
    assert second_response == "Your name is Alvaro."