"""
Module: test_prompt.py

Purpose:
    Validates the PromptTemplate abstraction behavior.
"""

from langchain_core.messages import HumanMessage

from ai_agent_system.prompt import PromptTemplate


class FakePrompt(PromptTemplate):
    """
    Fake prompt implementation for testing.
    """

    def format_messages(
        self,
        **kwargs: str,
    ) -> list[HumanMessage]:

        return [HumanMessage(content=kwargs["question"])]


def test_prompt_template_creates_messages() -> None:
    """
    Verify that prompt templates generate messages.
    """

    prompt = FakePrompt()

    messages = prompt.format_messages(question="What is AI?")

    assert len(messages) == 1
    assert messages[0].content == "What is AI?"
