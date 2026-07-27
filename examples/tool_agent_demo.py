"""
Module: tool_agent_demo.py

Location:
    examples/

Purpose:
    Demonstrate the educational Tool Agent.

Description:
    This example sends a request to the ToolAgent and prints
    the raw response returned by the tool-aware language model.
"""

from ai_agent_system.tool_agent import ToolAgent


def main() -> None:
    """
    Run the Tool Agent demonstration.
    """

    agent = ToolAgent()

    response = agent.invoke("What time is it?")

    print("\nResponse Type:\n")
    print(type(response))

    print("\nRaw Response:\n")
    print(response)


if __name__ == "__main__":
    main()
