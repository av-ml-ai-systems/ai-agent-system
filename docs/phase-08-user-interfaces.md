# Phase 8 — User Interfaces

---

# Objective

The objective of this phase is to expose the AI Agent through simple user interfaces.

Until this point, the Agent has been executed directly from Python scripts. Although this is sufficient for learning the internal architecture, real applications expose AI systems through interfaces that allow users to interact with them naturally.

This phase introduces three increasingly realistic interfaces:

- A REST API using FastAPI.
- A rapid experimentation interface using Streamlit.
- A simple web application using React.

The purpose is **not** to build a production-ready frontend.

Instead, the goal is to understand how the Agent integrates with external applications while preserving the software architecture developed throughout the previous phases.

---

# Learning Objectives

After completing this phase, the educational AI Agent will be able to:

- expose its functionality through HTTP,
- receive requests from external clients,
- return structured responses,
- separate backend logic from presentation,
- support multiple user interfaces using the same Agent implementation.

---

# Why User Interfaces Matter

Large Language Models rarely interact directly with end users.

Instead, users communicate with applications such as:

- Web pages
- Mobile applications
- Internal enterprise portals
- Desktop software
- APIs consumed by other services

The AI Agent therefore becomes one component inside a larger software system.

The user interface should never contain the Agent logic itself.

Instead, it should simply communicate with the backend responsible for executing the Agent.

---

# User Interface Architecture

Throughout this phase, the architecture evolves into the following structure:

```
                User

                  │

                  ▼

         User Interface
   (React / Streamlit)

                  │

                  ▼

            FastAPI API

                  │

                  ▼

             ToolAgent

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 Conversation          LangChain

        │                   │

        └─────────┬─────────┘

                  ▼

              ChatOllama

                  │

                  ▼

                Tools
```

Each layer has a single responsibility.

---

# Separation of Responsibilities

## User Interface

Responsible only for:

- collecting user input,
- displaying responses,
- presenting conversation history.

The interface should never implement reasoning logic.

---

## FastAPI

Responsible for:

- exposing HTTP endpoints,
- validating requests,
- invoking the Agent,
- returning responses.

FastAPI does not implement AI reasoning.

---

## ToolAgent

Responsible for:

- orchestrating reasoning,
- interacting with memory,
- deciding whether tools are required,
- coordinating the language model.

---

## Conversation

Responsible only for storing conversation state.

---

## Tools

Responsible only for performing external actions.

Examples include:

- Calculator
- Clock
- File Reader

---

# FastAPI

FastAPI is a modern Python framework for building REST APIs.

In this project it provides:

- HTTP endpoints,
- automatic request validation,
- automatic API documentation,
- OpenAPI specification generation.

FastAPI becomes the communication layer between the Agent and any external application.

---

# Streamlit

Streamlit provides an extremely simple way to create interactive AI demonstrations.

Its purpose in this project is educational.

Advantages include:

- very little code,
- rapid experimentation,
- immediate visualization,
- useful during development.

Streamlit is ideal for validating Agent behavior before investing in a complete frontend.

---

# React

React represents a more realistic frontend architecture.

Unlike Streamlit, React is a dedicated frontend framework responsible only for the presentation layer.

In this project the React application communicates with FastAPI using HTTP requests.

This demonstrates the standard separation between frontend and backend used in modern AI applications.

---

# Backend–Frontend Communication

The communication flow is intentionally simple.

```
User

↓

React / Streamlit

↓

HTTP Request

↓

FastAPI

↓

ToolAgent

↓

LLM + Tools

↓

FastAPI Response

↓

React / Streamlit

↓

User
```

The frontend never communicates directly with the language model.

---

# Educational Scope

This repository intentionally implements only a minimal interface.

The following enterprise features are intentionally excluded:

- Authentication
- Authorization
- User accounts
- Session persistence
- Databases
- Streaming responses
- WebSockets
- Deployment
- Docker Compose
- Reverse proxies
- Load balancing

These belong to future repositories.

---

# Engineering Concepts

## API Layer

The API layer separates external communication from the Agent implementation.

The Agent remains independent of the communication protocol.

---

## Frontend / Backend Separation

Presentation and business logic remain completely independent.

This separation improves:

- maintainability,
- scalability,
- testability,
- readability.

---

# Phase Summary

In this phase, the educational AI Agent evolves from a command-line application into a system that can be accessed through multiple interfaces.

The Agent itself does not change.

Only the way users communicate with it changes.

This reinforces one of the central ideas of software engineering:

> A well-designed application separates business logic from presentation, allowing multiple interfaces to reuse the same core system.

## Phase 8 Progress Notes — FastAPI Backend and Streamlit Interface

# 8.1 — FastAPI Backend Implementation

Implemented a FastAPI backend layer to expose the AI Agent system through an API interface.

The objective was to separate the user interface from the Agent implementation and create a clean API layer responsible for communication.

Architecture:

Client Interface

↓

FastAPI API Layer

↓

ToolAgent

↓

LangChain + Ollama

↓

Tools and Conversation State


Implemented components:

- FastAPI application.
- `/chat` endpoint.
- Request and response schemas.
- Agent integration.
- OpenAPI documentation.
- Swagger UI validation.

The API was successfully exposed through:

```
http://127.0.0.1:8000/docs
```

The Swagger interface was used to validate:

- User message submission.
- Agent response generation.
- Tool execution.
- Conversation behavior.

Example API interaction:

Request:

```json
{
  "message": "What time is it?"
}
```

Response:

```text
The current time is 6:46 PM on July 29, 2026.
```

The FastAPI layer successfully communicated with the AI Agent and returned generated responses.

---

# 8.2 — Streamlit Interface Implementation

Implemented a Streamlit-based frontend client to interact with the FastAPI backend.

The Streamlit interface does not directly access the Agent.

Instead, it communicates through the API layer:

Streamlit Interface

↓

FastAPI `/chat` Endpoint

↓

ToolAgent

↓

LangChain + Ollama


Implemented capabilities:

- Chat interface.
- Connection with FastAPI backend.
- Display of user and assistant messages.
- Conversation visualization.
- Dark theme configuration.
- End-to-end validation.

The complete user workflow was validated successfully.

Example interaction:

User:

```
My name is Jhon.
```

Assistant:

```
Hi Jhon! Nice to meet you. 😊
```


User:

```
What is my name?
```

Assistant:

```
Your name is Jhon! 😊
```


User:

```
What time is it?
```

Assistant:

```
It's currently 6:46 PM on July 29, 2026! 😊
```

This validated:

- Frontend communication.
- Backend processing.
- Agent execution.
- Conversation state handling.
- Tool usage.

---

# Agent Behavior Improvement — System Message Integration

During UI testing, an inconsistency was identified in the Agent responses.

Problem:

When users provided simple conversational information, the Agent sometimes exposed internal reasoning.

Example:

```
The user has stated their name but has not requested any action that requires the use of the provided tools.
```

This behavior was caused by the absence of explicit behavioral instructions provided to the LLM.

The Agent had access to tools and conversation history, but it did not receive a system-level instruction defining how it should behave.

---

# Solution

Added a `SystemMessage` inside the `ToolAgent` module.

The Agent now receives messages in the following order:

System Instructions

↓

Conversation History

↓

Current User Message


The SystemMessage defines:

- The Agent should behave as a friendly assistant.
- Internal reasoning must remain private.
- Tool selection decisions should not be exposed.
- Responses should be natural and conversational.
- User information shared during the conversation should be acknowledged.
- Conversation history should be used when appropriate.

---

# Engineering Decision

The system instructions were implemented inside `ToolAgent` instead of modifying previous prompt abstractions.

Reason:

`ToolAgent` owns:

- Agent orchestration.
- Tool execution.
- Communication with the LLM.

`Conversation` remains responsible only for:

- Storing messages.
- Managing conversation state.

This maintains clean responsibility boundaries.

---

# Integration Test Improvement

After adding the SystemMessage, an integration test failed.

Original test assumption:

The response had to contain the exact word:

```
time
```

However, LLM responses are variable.

Examples of valid responses:

```
The current time is 6:22 PM.
```

```
It's currently 6:22 PM.
```

```
The clock shows 18:22.
```

The Agent behavior was correct, but the test was too restrictive.

---

# Test Improvement

Updated the integration test to validate expected behavior instead of exact wording.

The test now checks semantic behavior rather than exact generated text.

Engineering lesson:

Traditional software testing:

```
Input → Exact Output
```

LLM application testing:

```
Input → Expected Behavior
```

LLM tests should validate correctness and intent rather than exact sentences.

---

# Phase 8 Validation Completed

Successfully executed:

- Ruff formatting.
- Ruff linting.
- MyPy static analysis.
- Pre-commit hooks.
- Unit tests.
- Integration tests.
- FastAPI Swagger validation.
- Streamlit end-to-end validation.

Current status:

## Phase 8.1 — FastAPI Backend

Completed:

- API creation.
- Chat endpoint.
- Agent integration.
- OpenAPI documentation.


## Phase 8.2 — Streamlit Interface

Completed:

- Experimentation interface.
- Chat window.
- Conversation visualization.
- Backend communication.
- Agent behavior validation.


## Remaining

## Phase 8.3 — React Frontend

Objectives:

- Create React chat interface.
- Connect React frontend with FastAPI backend.
- Display conversation history.
- Implement simple user interface.
