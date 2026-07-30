"""
Module: api.py

Location:
    src/ai_agent_system/

Purpose:
    Expose the educational AI Agent through a FastAPI backend.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent_system.tool_agent import ToolAgent

app = FastAPI(
    title="AI Agent Sysytem API",
    description="REST API exposing the AI Agent System.",
    version="1.0.0",
)

agent = ToolAgent()


class ChatRequest(BaseModel):
    """
    Incoming chat request.
    """

    message: str


class ChatResponse(BaseModel):
    """
    Outgoing chat response.
    """

    response: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """
    Process one user message through the ToolAgent.
    """

    result = agent.invoke(request.message)

    return ChatResponse(
        response=result.content,
    )
