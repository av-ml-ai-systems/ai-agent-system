"""
Module: test_file_reader_integration.py

Location:
    tests/integration/

Purpose:
    Integration tests for the File Reader Tool.

Description:
    Verify that the LangChain Tool correctly integrates with
    the business logic.
"""

from pathlib import Path

from ai_agent_system.tools.file_reader import read_text_file


def test_file_reader_tool_integration() -> None:
    """
    Verify the File Reader Tool through the LangChain interface.
    """

    sample_file = Path(__file__).parent.parent.parent / "examples" / "sample_notes.txt"

    result = read_text_file.invoke({"file_path": str(sample_file)})

    assert "Machine Learning" in result
    assert "LangChain" in result
