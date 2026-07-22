"""
Module: test_ollama_llm.py

Location:
    tests/integration/

Purpose:
    Verifies that OllamaLLM can communicate with a running Ollama server.
"""

from ai_agent_system.ollama_llm import OllamaLLM


def test_ollama_llm_generation() -> None:
    """
    Integration test requiring a running Ollama instance.
    """

    llm = OllamaLLM(model="qwen3:4b")

    response = llm.invoke(
    "Hi."
    )

    assert isinstance(response, str)
    assert response.strip()