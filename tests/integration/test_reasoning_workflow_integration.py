"""
Module: test_reasoning_workflow_integration.py

Location:
    tests/integration/

Purpose:
    Validate the complete educational reasoning workflow.

Description:
    This integration test verifies that the ToolAgent can
    complete one reasoning cycle using a real language model
    and return a valid AIMessage.
"""

from langchain_core.messages import AIMessage

from ai_agent_system.tool_agent import ToolAgent


def test_reasoning_workflow() -> None:
    """
    Verify the complete reasoning workflow.
    """

    agent = ToolAgent()

    response = agent.invoke("What time is it?")

    assert isinstance(response, AIMessage)

    assert response.content != ""
