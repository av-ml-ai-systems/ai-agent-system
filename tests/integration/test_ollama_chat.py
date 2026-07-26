"""
Module: test_ollama_chat.py

Location:
    tests/integration/

Purpose:
    Verifies that OllamaChat can communicate with a running
    Ollama server through LangChain ChatOllama.
"""

from langchain_core.messages import HumanMessage

from ai_agent_system.ollama_chat import OllamaChat


def test_ollama_chat_generation() -> None:
    """
    Integration test requiring a running Ollama instance.
    """

    chat_model = OllamaChat(
        model="qwen3:4b",
    )

    messages = [HumanMessage(content="Introduce yourself in one sentence.")]

    response = chat_model.invoke(messages)

    assert response.content
    assert isinstance(response.content, str)
