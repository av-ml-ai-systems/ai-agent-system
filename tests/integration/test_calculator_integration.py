"""
Module: test_calculator_integration.py

Location:
    tests/integration/

Purpose:
    Integration tests for the Calculator LangChain Tool.

Description:
    Verify that the LangChain Tool integrates correctly with
    the arithmetic evaluator.
"""

from ai_agent_system.tools.calculator import calculator


def test_calculator_tool_integration() -> None:
    """
    Verify the complete Calculator Tool workflow.

    LangChain Tool
            ↓
    Tool Invocation
            ↓
    Arithmetic Evaluation
            ↓
    Result
    """

    expression = "25 * (8 + 2)"

    result = calculator.invoke(
        {
            "expression": expression,
        }
    )

    assert result == 250