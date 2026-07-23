"""
Module: test_agent.py

Location:
    tests/test_agent.py

Purpose:
    Unit tests for the Agent class.

The tests verify:
- Agent delegates generation to ChatModel.
- Agent uses PromptTemplate.
- Agent manages conversation state.
- Previous messages are preserved.
"""

from langchain_core.messages import AIMessage, BaseMessage

from ai_agent_system.agent import Agent
from ai_agent_system.chat_model import ChatModel
from ai_agent_system.conversation import Conversation
from ai_agent_system.prompt import PromptTemplate


class FakeChatModel(ChatModel):
    """
    Fake ChatModel implementation.
    """

    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> AIMessage:
        """
        Return deterministic response.
        """

        return AIMessage(
            content="This is a fake response."
        )


class FakePrompt(PromptTemplate):
    """
    Fake prompt implementation for testing Agent behavior.
    """

    def format_messages(
        self,
        **kwargs: str,
    ) -> list[BaseMessage]:
        """
        Create test messages.
        """

        from langchain_core.messages import HumanMessage

        return [
            HumanMessage(
                content=kwargs["question"],
            )
        ]


class MemoryAwareFakeChatModel(ChatModel):
    """
    Fake ChatModel that checks conversation history.
    """

    def invoke(
        self,
        messages: list[BaseMessage],
    ) -> AIMessage:

        if len(messages) >= 3:
            return AIMessage(
                content="Your name is Alvaro."
            )

        return AIMessage(
            content="I do not know your name."
        )


def create_agent(
    chat_model: ChatModel,
) -> Agent:
    """
    Helper function to create Agent instances.
    """

    return Agent(
        chat_model,
        Conversation(),
        FakePrompt(),
    )


def test_agent_returns_chat_model_response() -> None:
    """
    Verify Agent returns ChatModel response.
    """

    agent = create_agent(
        FakeChatModel()
    )

    response = agent.answer(
        "What is artificial intelligence?"
    )

    assert response == "This is a fake response."


def test_agent_updates_conversation_state() -> None:
    """
    Verify Agent stores messages.
    """

    conversation = Conversation()

    agent = Agent(
        FakeChatModel(),
        conversation,
        FakePrompt(),
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
    Verify previous messages are available.
    """

    conversation = Conversation()

    agent = Agent(
        MemoryAwareFakeChatModel(),
        conversation,
        FakePrompt(),
    )

    first_response = agent.answer(
        "My name is Alvaro."
    )

    second_response = agent.answer(
        "What is my name?"
    )

    assert first_response == "I do not know your name."
    assert second_response == "Your name is Alvaro."