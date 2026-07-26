"""
Module: clock_tool_demo.py

Location:
    examples/

Purpose:
    Demonstrate the Clock LangChain Tool.

Description:
    Educational example for Phase 5 of the AI Agent System
    roadmap.
"""

from ai_agent_system.tools.clock import current_datetime


def main() -> None:
    """
    Demonstrate the Clock Tool.
    """

    result = current_datetime.invoke({})

    print("Current Date and Time:")

    print(result)


if __name__ == "__main__":
    main()
