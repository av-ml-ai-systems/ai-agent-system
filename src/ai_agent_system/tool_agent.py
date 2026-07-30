"""
Module: tool_agent.py

Location:
    src/ai_agent_system/

Purpose:
    Define an AI Agent capable of using external
    Tools through LangChain.

Description:
    This module introduces Tool Integration by connecting a
    language model with multiple LangChain Tools while
    preserving a clean software architecture.
"""

from langchain_core.messages import SystemMessage, ToolMessage
from langchain_ollama import ChatOllama

from ai_agent_system.conversation import Conversation
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
    AI Agent capable of using LangChain Tools.
    """

    def __init__(self) -> None:
        self._model = TOOL_AWARE_MODEL

        self._conversation = Conversation()

        self._system_message = SystemMessage(
            content=(
                "You are a friendly AI assistant.\n\n"
                "Your internal reasoning is private and must never be "
                "shown to the user.\n\n"
                "Never explain whether tools were or were not selected.\n\n"
                "Use tools whenever necessary.\n\n"
                "Respond naturally and conversationally to greetings, "
                "introductions, and questions.\n\n"
                "If the user shares their name, acknowledge it naturally.\n\n"
                "Use conversation history when answering questions about "
                "previous messages."
            )
        )

        self._tool_registry = {tool.name: tool for tool in TOOLS}

    def _display_reasoning_step(
        self,
        title: str,
        content: str,
    ) -> None:
        """
        Display one educational reasoning step.

        Parameters
        ----------
        title:
            Name of the reasoning stage.

        content:
            Description of the reasoning stage.
        """

        print("\n" + "=" * 60)
        print(title.upper())
        print("=" * 60)
        print(content)

    def invoke(
        self,
        user_message: str,
    ):
        """
        Execute one complete reasoning cycle.
        """

        self._conversation.add_user_message(
            user_message,
        )

        self._display_reasoning_step(
            "Thought",
            (
                "The Agent analyzes the user's request and decides "
                "whether an external Tool is required."
            ),
        )

        messages = [
            self._system_message,
            *self._conversation.messages(),
        ]

        response = self._model.invoke(messages)

        if not response.tool_calls:
            self._display_reasoning_step(
                "Action",
                "No Tool required.",
            )

            self._conversation.add_ai_message(
                response.content,
            )

            self._display_reasoning_step(
                "Final Answer",
                response.content,
            )

            return response

        messages.append(response)

        tool_call = response.tool_calls[0]

        self._display_reasoning_step(
            "Action",
            f"Executing Tool: {tool_call['name']}",
        )

        tool = self._tool_registry[tool_call["name"]]

        tool_result = tool.invoke(tool_call["args"])

        self._display_reasoning_step(
            "Observation",
            str(tool_result),
        )

        tool_message = ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"],
        )

        messages.append(tool_message)

        self._display_reasoning_step(
            "Final Reasoning",
            (
                "The Agent incorporates the Tool observation into "
                "its reasoning before generating the final answer."
            ),
        )

        final_response = self._model.invoke(messages)

        self._conversation.add_ai_message(
            final_response.content,
        )

        self._display_reasoning_step(
            "Final Answer",
            final_response.content,
        )

        return final_response
