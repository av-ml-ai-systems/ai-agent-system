# ============================================================================
# Module: llm.py
# Package: ai_agent_system
# Path: src/ai_agent_system/llm.py
#
# Purpose:
# Defines the contract that any Language Model (LLM) must satisfy in order
# to collaborate with the Agent.
#
# Responsibilities:
# - Define the minimum behavior expected from an LLM.
# - Decouple the Agent from any specific LLM implementation.
#
# This module does not implement a Language Model. It only defines the
# contract that collaborating LLMs must satisfy.
# ============================================================================

from typing import Protocol


class LLM(Protocol):
    """
    Contract for Language Models used by the Agent.

    Any object that implements this contract can collaborate with the Agent,
    regardless of the underlying LLM provider.
    """

    def invoke(self, question: str) -> str:
        """
        Generate a response for the given user question.

        Parameters
        ----------
        question : str
            The user's input.

        Returns
        -------
        str
            The generated response.
        """
        ...