"""
Module: test_langchain_prompt.py

Purpose:
    Validates LangChain prompt generation.
"""

from ai_agent_system.langchain_prompt import LangChainPrompt


def test_langchain_prompt_generates_messages() -> None:
    """
    Verify that the LangChain prompt adapter creates messages.
    """

    prompt = LangChainPrompt(
        system_message="You are a helpful assistant.",
        human_template="{question}",
    )

    messages = prompt.format_messages(
        question="What is machine learning?"
    )

    assert len(messages) == 2

    assert messages[0].content == (
        "You are a helpful assistant."
    )

    assert messages[1].content == (
        "What is machine learning?"
    )