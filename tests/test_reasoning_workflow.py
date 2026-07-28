"""
Module: test_reasoning_workflow.py

Location:
    tests/

Purpose:
    Validate the educational reasoning workflow implemented by
    ToolAgent.

Description:
    These tests verify that the Agent completes one reasoning
    cycle and returns an AIMessage.
"""

from langchain_core.messages import AIMessage

from ai_agent_system.tool_agent import ToolAgent


def test_reasoning_cycle_returns_ai_message() -> None:
    """
    Verify that one reasoning cycle produces an AIMessage.
    """

    agent = ToolAgent()

    response = agent.invoke("What time is it?")

    assert isinstance(response, AIMessage)
