"""
Module: calculator_tool_demo.py

Location:
    examples/

Purpose:
    Demonstrate the Calculator LangChain Tool.

Description:
    Educational example for Phase 5 of the AI Agent System
    roadmap.
"""

from ai_agent_system.tools.calculator import calculator


def main() -> None:
    """
    Demonstrate the Calculator Tool.
    """

    expression = "25 * (8 + 2)"

    result = calculator.invoke(
        {
            "expression": expression,
        }
    )

    print("Expression:")
    print(expression)

    print()

    print("Result:")
    print(result)


if __name__ == "__main__":
    main()
