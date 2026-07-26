"""
Module: file_reader.py

Location:
    src/ai_agent_system/tools/

Purpose:
    Read the contents of a local text file as a LangChain Tool.

Description:
    Educational File Reader Tool for Phase 5 of the AI Agent
    System roadmap.
"""

from pathlib import Path

from langchain_core.tools import tool


def _read_text_file(file_path: str) -> str:
    """
    Read the contents of a local text file.

    Parameters
    ----------
    file_path : str
        Path to the text file.

    Returns
    -------
    str
        File contents or an error message.
    """

    path = Path(file_path)

    try:
        return path.read_text(encoding="utf-8")

    except FileNotFoundError:
        return f"Error: File '{file_path}' was not found."

    except Exception as error:
        return f"Error reading file: {error}"


@tool
def read_text_file(file_path: str) -> str:
    """
    Read the contents of a local text file.

    Parameters
    ----------
    file_path : str
        Path to the text file.

    Returns
    -------
    str
        File contents or an error message.
    """

    return _read_text_file(file_path)
