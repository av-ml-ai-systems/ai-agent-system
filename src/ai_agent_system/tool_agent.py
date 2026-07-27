"""
Module: tool_agent.py

Location:
    src/ai_agent_system/

Purpose:
    Define an educational AI Agent capable of using external
    Tools through LangChain.

Description:
    This module introduces Tool Integration by connecting a
    language model with multiple LangChain Tools while
    preserving a clean software architecture.
"""

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama

from ai_agent_system.tools.calculator import calculator
from ai_agent_system.tools.clock import current_datetime
from ai_agent_system.tools.file_reader import read_text_file

TOOLS = [
    calculator,
    current_datetime,
    read_text_file,
]

CHAT_MODEL = ChatOllama(
    model="qwen3:4b",
)

TOOL_AWARE_MODEL = CHAT_MODEL.bind_tools(TOOLS)


class ToolAgent:
    """
    Educational AI Agent capable of using LangChain Tools.
    """

    def __init__(self) -> None:
        self._model = TOOL_AWARE_MODEL

        self._tool_registry = {tool.name: tool for tool in TOOLS}

    def invoke(self, user_message: str):
        """
        Execute one complete reasoning cycle.
        """

        messages = [
            HumanMessage(content=user_message),
        ]

        response = self._model.invoke(messages)

        if not response.tool_calls:
            return response

        messages.append(response)

        tool_call = response.tool_calls[0]

        tool = self._tool_registry[tool_call["name"]]

        tool_result = tool.invoke(tool_call["args"])

        tool_message = ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"],
        )

        messages.append(tool_message)

        final_response = self._model.invoke(messages)

        return final_response
