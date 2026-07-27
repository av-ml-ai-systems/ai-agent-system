"""
Module: test_tool_agent.py

Location:
    tests/

Purpose:
    Unit tests for the educational ToolAgent.

Description:
    Validate the internal ToolAgent behavior,
    including tool registration and tool execution.
"""

from ai_agent_system.tool_agent import ToolAgent


def test_tool_agent_initialization() -> None:
    """
    Verify that ToolAgent initializes correctly.
    """

    agent = ToolAgent()

    assert agent is not None


def test_tool_registry_contains_tools() -> None:
    """
    Verify that the Agent knows the available tools.
    """

    agent = ToolAgent()

    assert "calculator" in agent._tool_registry
    assert "current_datetime" in agent._tool_registry
    assert "read_text_file" in agent._tool_registry
