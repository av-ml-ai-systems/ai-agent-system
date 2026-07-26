"""
Module: agent_demo.py

Location:
    examples/

Purpose:
    Demonstrates the complete application architecture by connecting
    the Agent to Ollama through LangChain abstractions.
"""

from ai_agent_system.agent import Agent
from ai_agent_system.conversation import Conversation
from ai_agent_system.langchain_prompt import LangChainPrompt
from ai_agent_system.ollama_chat import OllamaChat


def main() -> None:
    """Run a simple conversation with the Agent."""

    chat_model = OllamaChat(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    prompt = LangChainPrompt(
        system_message="You are a helpful assistant.",
        human_template="{question}",
    )

    conversation = Conversation()

    agent = Agent(
        chat_model,
        conversation,
        prompt,
    )

    response = agent.answer("Introduce yourself in one sentence.")

    print("\nAgent Response:\n")
    print(response)


if __name__ == "__main__":
    main()
