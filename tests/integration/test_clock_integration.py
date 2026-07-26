"""
Module: test_clock_integration.py

Location:
    tests/integration/

Purpose:
    Integration tests for the Clock LangChain Tool.

Description:
    Verify that the LangChain Tool integrates correctly with
    the business logic that retrieves the current system
    date and time.
"""

from datetime import datetime

from ai_agent_system.tools.clock import current_datetime


def test_clock_tool_integration() -> None:
    """
    Verify the complete Clock Tool workflow.

    LangChain Tool
            ↓
    Tool Invocation
            ↓
    Business Logic
            ↓
    Current Datetime
    """

    result = current_datetime.invoke({})

    parsed_datetime = datetime.fromisoformat(result)

    assert isinstance(parsed_datetime, datetime)