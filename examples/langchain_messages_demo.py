"""
Module: langchain_messages_demo.py

Location:
    examples/

Purpose:
    Educational demonstration of how LangChain handles
    text completion models versus chat models.

This experiment does not modify the Agent architecture.
It only explores LangChain behavior.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama


def main() -> None:
    """Run LangChain message experiments."""

    llm = ChatOllama(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    print("\n=== Experiment 1: Simple String Prompt ===\n")

    response = llm.invoke("Introduce yourself in one sentence.")

    print(response.content)

    print("\n=== Experiment 2: Structured Messages ===\n")

    messages = [
        SystemMessage(content="You are a concise AI assistant."),
        HumanMessage(content="Introduce yourself in one sentence."),
    ]

    response = llm.invoke(messages)

    print(response.content)


if __name__ == "__main__":
    main()
