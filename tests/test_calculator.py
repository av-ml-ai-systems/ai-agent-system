"""
Module: test_calculator.py

Location:
    tests/

Purpose:
    Unit tests for the Calculator LangChain Tool.

Description:
    Verify the correctness of the arithmetic evaluator and
    the public LangChain Tool interface.
"""

import ast

import pytest

from ai_agent_system.tools.calculator import (
    _evaluate_expression,
    calculator,
)


def test_addition() -> None:
    """Evaluate a simple addition."""

    tree = ast.parse(
        "2 + 3",
        mode="eval",
    )

    result = _evaluate_expression(tree.body)

    assert result == 5


def test_parentheses() -> None:
    """Evaluate an expression with parentheses."""

    tree = ast.parse(
        "2 * (3 + 4)",
        mode="eval",
    )

    result = _evaluate_expression(tree.body)

    assert result == 14


def test_division() -> None:
    """Evaluate a division."""

    tree = ast.parse(
        "10 / 2",
        mode="eval",
    )

    result = _evaluate_expression(tree.body)

    assert result == 5


def test_negative_number() -> None:
    """Evaluate a negative number."""

    tree = ast.parse(
        "-5 + 3",
        mode="eval",
    )

    result = _evaluate_expression(tree.body)

    assert result == -2


def test_invalid_operator() -> None:
    """Exponentiation should not be supported."""

    tree = ast.parse(
        "2 ** 3",
        mode="eval",
    )

    with pytest.raises(ValueError):
        _evaluate_expression(tree.body)


def test_tool_invoke() -> None:
    """Verify the LangChain Tool interface."""

    result = calculator.invoke(
        {
            "expression": "25 * (8 + 2)",
        }
    )

    assert result == 250
