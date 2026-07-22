"""
Module: ollama_llm.py

Location:
    src/ai_agent_system/

Purpose:
    Provides a concrete implementation of the LLM interface that communicates
    with a locally running Ollama server.
"""

import httpx

from .llm import LLM


class OllamaLLM(LLM):
    """LLM implementation that communicates with an Ollama server."""

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
    ) -> None:
        self.model = model
        self.base_url = base_url

    def invoke(self, prompt: str) -> str:
        """Generate a response using an Ollama model."""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        response = httpx.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=180.0,
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]