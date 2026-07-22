"""
Module: test_ollama_llm.py

Location:
    tests/integration/

Purpose:
    Verifies that OllamaLLM can communicate with a running Ollama server.
"""

from langchain_ollama import OllamaLLM as LangChainOllamaLLM

from ai_agent_system.ollama_llm import OllamaLLM


def test_ollama_llm_generation() -> None:
    """
    Integration test requiring a running Ollama instance.
    """

    langchain_llm = LangChainOllamaLLM(
        model="qwen3:4b",
        base_url="http://localhost:11434",
    )

    llm = OllamaLLM(langchain_llm)

    response = llm.invoke("Hi.")

    print(type(response))

    assert isinstance(response, str)
    assert response.strip()