"""
Module: agent_demo.py

Location:
    examples/

Purpose:
    Demonstrates the complete application architecture by connecting the Agent
    to a real Ollama model through the LLM abstraction. This example verifies
    that the Agent remains independent of both LangChain and Ollama.
"""

from langchain_ollama import OllamaLLM as LangChainOllamaLLM

from ai_agent_system.agent import Agent
from ai_agent_system.ollama_llm import OllamaLLM


def main() -> None:
    """Run a simple conversation with the Agent."""

    langchain_llm = LangChainOllamaLLM(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    llm = OllamaLLM(langchain_llm)

    agent = Agent(llm)

    response = agent.answer("Introduce yourself in one sentence.")

    print("\nAgent Response:\n")
    print(response)


if __name__ == "__main__":
    main()