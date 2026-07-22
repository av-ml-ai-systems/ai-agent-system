"""
Module: ollama_llm.py

Location:
    src/ai_agent_system/

Purpose:
    Provides a concrete implementation of the LLM interface that communicates
    with a locally running Ollama server using LangChain.
"""

from langchain_ollama import OllamaLLM as LangChainOllamaLLM

from .llm import LLM


class OllamaLLM(LLM):
    """Adapter between the application and a LangChain Ollama model."""

    def __init__(self, llm: LangChainOllamaLLM) -> None:
        """
        Initialize the adapter.

        Parameters
        ----------
        llm : LangChainOllamaLLM
            A configured LangChain Ollama model.
        """
        self._llm = llm

    def invoke(self, prompt: str) -> str:
        """Generate a response using the configured LangChain model."""

        return self._llm.invoke(prompt)