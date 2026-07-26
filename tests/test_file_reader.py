"""
Module: test_file_reader.py

Location:
    tests/

Purpose:
    Unit tests for the File Reader Tool.

Description:
    Verify that the business logic correctly reads text files
    and handles common error conditions.
"""

from pathlib import Path

from ai_agent_system.tools.file_reader import (
    _read_text_file,
    read_text_file,
)


def test_read_existing_file() -> None:
    """
    Verify that an existing text file is read correctly.
    """

    sample_file = Path(__file__).parent.parent / "examples" / "sample_notes.txt"

    result = _read_text_file(str(sample_file))

    assert "Machine Learning" in result


def test_read_missing_file() -> None:
    """
    Verify that a missing file returns an error message.
    """

    result = _read_text_file("does_not_exist.txt")

    assert "not found" in result.lower()


def test_file_reader_tool() -> None:
    """
    Verify the LangChain Tool interface.
    """

    sample_file = Path(__file__).parent.parent / "examples" / "sample_notes.txt"

    result = read_text_file.invoke({"file_path": str(sample_file)})

    assert "LangChain" in result
