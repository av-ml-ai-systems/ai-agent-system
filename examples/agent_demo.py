"""
Module: agent_demo.py

Location:
    examples/

Purpose:
    Demonstrates the complete Agent architecture using:
    - Conversation State
    - ChatModel abstraction
    - OllamaChat adapter

The Agent remains independent from:
- Ollama
- LangChain
- Provider-specific implementations
"""

from ai_agent_system.agent import Agent
from ai_agent_system.conversation import Conversation
from ai_agent_system.ollama_chat import OllamaChat


def main() -> None:
    """
    Run a stateful conversation with the Agent.
    """

    chat_model = OllamaChat(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    conversation = Conversation()

    agent = Agent(
        chat_model,
        conversation,
    )

    first_response = agent.answer(
        "My name is Alvaro."
    )

    print("\nAssistant:\n")
    print(first_response)

    second_response = agent.answer(
        "What is my name?"
    )

    print("\nAssistant:\n")
    print(second_response)


if __name__ == "__main__":
    main()