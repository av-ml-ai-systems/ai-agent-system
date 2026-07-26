"""
Module: test_conversation.py

Purpose:
    Tests conversation state management.
"""

from langchain_core.messages import HumanMessage

from ai_agent_system.conversation import Conversation


def test_conversation_stores_messages() -> None:
    """
    Verify that conversation history is preserved.
    """

    conversation = Conversation()

    conversation.add_message(HumanMessage(content="Hello"))

    messages = conversation.messages()

    assert len(messages) == 1
    assert messages[0].content == "Hello"
