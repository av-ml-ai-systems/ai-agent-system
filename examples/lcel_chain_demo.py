"""
Module: lcel_chain_demo.py

Location:
    examples/

Purpose:
    Educational example demonstrating LangChain Expression Language (LCEL).

This example shows how LangChain components can be composed:

    ChatPromptTemplate
            |
            v
        ChatOllama
            |
            v
        Response

This is a learning example only.

It does not modify the AI Agent architecture.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def main() -> None:
    """
    Execute a simple LCEL pipeline.
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant.",
            ),
            (
                "human",
                "{question}",
            ),
        ]
    )

    model = ChatOllama(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    chain = prompt | model

    response = chain.invoke(
        {"question": "Explain what an AI agent is in one sentence."}
    )

    print(response.content)


if __name__ == "__main__":
    main()
