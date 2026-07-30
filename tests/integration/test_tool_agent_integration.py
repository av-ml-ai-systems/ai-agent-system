"""
Module: test_tool_agent_integration.py

Location:
    tests/integration/

Purpose:
    Integration tests for the educational ToolAgent.

Description:
    Validate the complete workflow:
    User request → LLM → Tool selection →
    Tool execution → Final response.
"""

from ai_agent_system.tool_agent import ToolAgent


def test_clock_tool_agent_workflow() -> None:
    """
    Verify that the Agent can select and execute
    the clock tool.
    """

    agent = ToolAgent()

    response = agent.invoke("What time is it?")

    assert response.content

    assert any(
        keyword in response.content.lower()
        for keyword in [
            "pm",
            "am",
            "hour",
            "clock",
            ":",
        ]
    )
