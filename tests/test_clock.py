"""
Module: test_clock.py

Location:
    tests/unit/

Purpose:
    Unit tests for the Clock LangChain Tool.

Description:
    Verify the correctness of the Clock Tool business logic
    and its LangChain interface.
"""

from datetime import datetime

from ai_agent_system.tools.clock import (
    _get_current_datetime,
    current_datetime,
)


def test_get_current_datetime_returns_string() -> None:
    """
    Verify that the helper returns a string.
    """

    result = _get_current_datetime()

    assert isinstance(result, str)


def test_get_current_datetime_returns_iso_format() -> None:
    """
    Verify that the returned string is a valid ISO datetime.
    """

    result = _get_current_datetime()

    parsed_datetime = datetime.fromisoformat(result)

    assert isinstance(parsed_datetime, datetime)


def test_clock_tool_invoke_returns_string() -> None:
    """
    Verify that the LangChain Tool returns a string.
    """

    result = current_datetime.invoke({})

    assert isinstance(result, str)


def test_clock_tool_returns_valid_iso_datetime() -> None:
    """
    Verify that the Tool returns a valid ISO datetime.
    """

    result = current_datetime.invoke({})

    parsed_datetime = datetime.fromisoformat(result)

    assert isinstance(parsed_datetime, datetime)