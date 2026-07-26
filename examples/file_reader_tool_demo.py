"""
Module: file_reader_tool_demo.py

Location:
    examples/

Purpose:
    Demonstrate the File Reader Tool using a local text file.

Description:
    Educational example for Phase 5.4 of the AI Agent System
    roadmap.
"""

from pathlib import Path

from ai_agent_system.tools.file_reader import read_text_file


def main() -> None:
    """
    Demonstrate the File Reader Tool.
    """

    sample_file = Path(__file__).parent / "sample_notes.txt"

    response = read_text_file.invoke({"file_path": str(sample_file)})

    print("File Contents:\n")
    print(response)


if __name__ == "__main__":
    main()
