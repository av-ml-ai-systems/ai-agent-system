"""
Module: tool_agent_demo.py

Location:
    examples/

Purpose:
    Demonstrate conversational memory using the educational
    ToolAgent.
"""

from ai_agent_system.tool_agent import ToolAgent


def main() -> None:
    """
    Demonstrate a multi-turn conversation.
    """

    agent = ToolAgent()

    print("\nUSER:")
    print("My name is Alvaro.\n")

    response = agent.invoke("My name is Alvaro.")

    print("\nASSISTANT:")
    print(response.content)

    print("\n" + "=" * 70)

    print("\nUSER:")
    print("What is my name?\n")

    response = agent.invoke("What is my name?")

    print("\nASSISTANT:")
    print(response.content)


if __name__ == "__main__":
    main()
