"""
Module: calculator.py

Location:
    src/ai_agent_system/tools/

Purpose:
    Provide a LangChain tool for evaluating simple arithmetic
    expressions.

Description:
    Educational calculator tool used during Phase 5 of the
    AI Agent System roadmap.
"""

import ast
import operator

from langchain_core.tools import tool

_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _evaluate_expression(node: ast.AST) -> float:
    """
    Recursively evaluate an arithmetic expression represented
    as an Abstract Syntax Tree (AST).

    Only the following operations are supported:

    - Addition
    - Subtraction
    - Multiplication
    - Division
    """

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Only numeric constants are allowed.")

    if isinstance(node, ast.BinOp):
        left = _evaluate_expression(node.left)
        right = _evaluate_expression(node.right)

        operation = _ALLOWED_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator.")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -_evaluate_expression(node.operand)

        if isinstance(node.op, ast.UAdd):
            return _evaluate_expression(node.operand)

    raise ValueError("Invalid arithmetic expression.")


@tool
def calculator(expression: str) -> float:
    """
    Evaluate a simple arithmetic expression.

    Parameters
    ----------
    expression:
        Arithmetic expression to evaluate.

    Returns
    -------
    float
        Result of the evaluated expression.

    Raises
    ------
    ValueError
        If the expression contains unsupported operations or
        invalid syntax.
    """

    try:
        tree = ast.parse(
            expression,
            mode="eval",
        )

        return _evaluate_expression(tree.body)

    except SyntaxError as exc:
        raise ValueError("Invalid arithmetic expression.") from exc
