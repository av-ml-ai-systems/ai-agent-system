"""
Module: clock.py

Location:
    src/ai_agent_system/tools/

Purpose:
    Provide the current system date and time as a LangChain Tool.

Description:
    Educational Clock Tool for Phase 5 of the AI Agent System
    roadmap.
"""

from datetime import datetime

from langchain_core.tools import tool

def _get_current_datetime() -> str:
    """
    Return the current system date and time.

    Returns
    -------
    str
        Current datetime formatted using ISO 8601.
    """

    return datetime.now().isoformat(timespec="seconds")

@tool
def current_datetime() -> str:
    """
    Return the current system date and time.

    Returns
    -------
    str
        Current system datetime.
    """

    return _get_current_datetime()