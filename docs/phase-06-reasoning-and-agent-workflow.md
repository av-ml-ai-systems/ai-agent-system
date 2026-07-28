# 🟡 Phase 6.1 — ReAct Pattern (Theory)

## What is ReAct?

**ReAct** stands for:

**Reason + Act**

It is a reasoning framework introduced by Google Research in 2022 that combines natural language reasoning with external actions.

Unlike a traditional Large Language Model, which only generates text, a ReAct Agent alternates between thinking and interacting with external resources.

The fundamental idea is that an Agent should not immediately generate a final answer. Instead, it should first reason about the problem, determine whether additional information or external capabilities are needed, execute the appropriate action, observe the result, and then continue reasoning before producing the final response.

---

# Why was ReAct created?

Traditional LLMs have an important limitation.

They can generate convincing text, but they cannot:

- Perform calculations reliably.
- Access current information.
- Read local files.
- Interact with APIs.
- Search databases.
- Execute external programs.

As a consequence, they often hallucinate or attempt to answer questions that require external information.

ReAct addresses this limitation by allowing the language model to decide when an external action is required.

Instead of relying only on its internal knowledge, the Agent can interact with the outside world through Tools.

---

# From Chatbot to Agent

A traditional chatbot follows a very simple workflow:

```
User

↓

Language Model

↓

Answer
```

A ReAct Agent introduces reasoning and actions:

```
User

↓

Thought

↓

Action

↓

Observation

↓

Thought

↓

Final Answer
```

The Agent no longer responds immediately.

Instead, it continuously evaluates the situation before deciding what to do next.

---

# The Four Components of ReAct

The ReAct pattern is built around four fundamental components.

## 1. Thought

The **Thought** represents the Agent's reasoning.

The Agent analyzes the user's request and decides what information is required.

Typical questions include:

- What is the user asking?
- Do I already know the answer?
- Do I need additional information?
- Should I use a Tool?

The Thought is an internal reasoning step.

Its purpose is decision making.

---

## 2. Action

The **Action** is the decision to perform an external operation.

Examples include:

- Calling a calculator.
- Reading a file.
- Checking the current date.
- Searching a database.
- Calling an external API.

The Action does not produce the final answer.

Instead, it gathers information required to continue reasoning.

---

## 3. Observation

The **Observation** is the result returned by the external action.

Examples:

Calculator:

```
Action:
Calculate 25 × 12

↓

Observation:
300
```

Clock:

```
Action:
Get current date

↓

Observation:
2026-07-27
```

The Observation becomes new information available to the Agent.

---

## 4. Final Answer

After receiving the Observation, the Agent reasons one final time and produces the response delivered to the user.

Unlike a standard chatbot, the final answer is informed by external evidence rather than relying only on the model's internal knowledge.

---

# ReAct is a Loop

An important characteristic of ReAct is that reasoning is iterative.

Instead of following a single sequence, the Agent may repeat the reasoning cycle multiple times.

```
Thought

↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation

↓

Final Answer
```

This iterative process allows Agents to solve problems requiring multiple steps.

---

# ReAct in Our Educational Agent

During Phase 5 we already implemented a simplified version of Tool Calling.

Our Agent currently performs the following workflow:

```
User Request

↓

Language Model

↓

Tool Selection

↓

Tool Execution

↓

Tool Result

↓

Language Model

↓

Final Answer
```

Although we did not explicitly implement the ReAct framework, the architecture already contains the essential components required for reasoning.

Phase 6 will make this reasoning process explicit and help us understand how modern AI Agents organize their decision-making.

---

# Educational Scope

In this repository we implement a simplified educational version of ReAct.

The objective is understanding the reasoning process rather than building an autonomous production Agent.

Therefore, this phase intentionally excludes:

- Multi-Agent systems.
- Autonomous planning.
- LangGraph workflows.
- Long-running Agents.
- Supervisors.
- Production orchestration.

Those topics belong to future repositories.

---

# Key Takeaways

- ReAct stands for **Reason + Act**.
- Agents reason before taking actions.
- External Tools extend the capabilities of an LLM.
- Every action generates an Observation.
- Observations become new information for subsequent reasoning.
- The reasoning process may repeat multiple times before producing the final answer.
- ReAct transforms a language model into an interactive problem-solving system rather than a text generator.

# 🟢 ReAct in Our AI Agent Architecture

## What We Already Have

At the end of Phase 5, our educational Agent is capable of:

- Receiving a user request.
- Understanding the request using an LLM.
- Deciding whether a Tool is required.
- Executing the selected Tool.
- Receiving the Tool output.
- Producing a final answer.

Conceptually, our current workflow is:

```
User Request

↓

LLM

↓

Tool Selection

↓

Tool Execution

↓

Tool Result

↓

LLM

↓

Final Answer
```

Although this architecture already works, one important step is hidden.

The LLM internally performs reasoning before deciding to call a Tool.

Phase 6 makes that reasoning explicit.

---

# Making the Hidden Reasoning Visible

Instead of thinking about Tool Calling as a black box, we can visualize the reasoning process.

```
User Request

↓

Thought

↓

Action

↓

Observation

↓

Final Answer
```

Each stage has a clear responsibility.

---

# Thought

The Agent analyzes the user's request.

Questions include:

- What does the user want?
- Can I answer directly?
- Do I need external information?
- Which Tool should I use?

The output of this stage is a decision.

No Tool has been executed yet.

---

# Action

The Agent performs the selected operation.

Examples:

- Calculator Tool
- Clock Tool
- File Reader Tool

The Action interacts with the external world.

---

# Observation

The Tool returns information.

Examples:

```
Calculator

↓

42
```

```
Clock

↓

2026-07-27 10:30
```

```
File Reader

↓

Contents of the file
```

The Observation becomes new knowledge for the Agent.

---

# Final Answer

Using both:

- the original user request, and
- the Tool observation,

the LLM generates the response delivered to the user.

---

# Relationship Between ReAct and Tool Calling

Tool Calling is **one capability** of an Agent.

ReAct is the **reasoning process** that decides whether Tool Calling is necessary.

In other words:

```
Reasoning

↓

Decision

↓

Tool Calling

↓

Observation

↓

Response
```

Tool Calling is therefore a consequence of reasoning.

---

# Why We Do Not Create New Components

An important design decision of this repository is to avoid unnecessary architecture.

Our current ToolAgent already performs:

- reasoning,
- Tool selection,
- Tool execution,
- response generation.

Therefore, Phase 6 will not introduce new architectural layers.

Instead, we will make the reasoning process explicit while keeping the implementation simple.

This follows our project principles:

- Educational before enterprise.
- Prefer the simplest solution that satisfies the educational objective.
- No scope creep.

---

# Engineering Perspective

From a software engineering perspective, ReAct is not a new class.

It is a workflow.

The responsibility of the ToolAgent remains unchanged.

The difference is that we now understand the internal reasoning stages that occur during its execution.

This reinforces an important engineering concept:

**A workflow describes how components collaborate without necessarily introducing additional classes or modules.**

# Phase 6.2 — Reasoning Loop

---

## Objective

Understand how an AI Agent performs iterative reasoning while preserving a simple educational implementation.

Our educational Agent executes a single reasoning cycle. Production AI Agents often execute multiple reasoning cycles before producing the final answer.

The objective of this section is to understand the architecture of reasoning loops without introducing unnecessary implementation complexity.

---

# What is a Reasoning Loop?

A reasoning loop is the iterative process through which an Agent repeatedly analyzes a problem, decides which action to perform, observes the result of that action, and determines whether additional reasoning is required.

Instead of immediately producing an answer, the Agent gradually builds the solution.

A reasoning loop can therefore be viewed as a sequence of repeated decision-making cycles.

---

# General Structure

A production reasoning loop typically follows this pattern:

```text
Thought

↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation

↓

...

↓

Final Answer
```

Each Observation becomes new information that the Agent uses during the next Thought.

---

# Single-Step vs Multi-Step Reasoning

## Single-Step Reasoning

The Agent performs only one reasoning cycle.

```text
Thought

↓

Action

↓

Observation

↓

Final Answer
```

Characteristics:

- Simple implementation.
- Easy to understand.
- Suitable for educational projects.
- Appropriate for simple Tool usage.

---

## Multi-Step Reasoning

The Agent performs several reasoning cycles.

```text
Thought

↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation

↓

Thought

↓

Final Answer
```

Characteristics:

- Allows solving more complex tasks.
- Supports planning.
- Supports multiple Tool calls.
- Enables adaptive decision making.

---

# Why Our Educational Agent Uses a Single Cycle

The purpose of this repository is to understand the architecture of Tool-Using Agents.

Implementing a complete reasoning loop would require additional concepts that belong to a different educational objective, including:

- Planning
- Loop orchestration
- Maximum iteration limits
- Failure recovery
- Recursive workflows
- Persistent execution state

Those concepts are intentionally postponed to future repositories focused on Agentic AI systems.

---

# Relationship with Modern Agent Frameworks

Modern frameworks such as LangGraph, AutoGen, CrewAI, and similar systems internally implement reasoning loops.

Rather than executing a single Tool call, these frameworks repeatedly perform:

- Reasoning
- Tool selection
- Observation
- Re-planning

until a termination condition is satisfied.

Our current Agent represents the smallest educational version of this architecture.

---

# Engineering Concepts

This section reinforces several software engineering concepts.

## Workflow Orchestration

The reasoning loop coordinates the order in which different components collaborate.

The Agent controls:

- Language Model
- Tools
- Observations
- Final response

while each component maintains a single responsibility.

---

## Responsibility Boundaries

Each component has a clearly defined responsibility.

ToolAgent

- Coordinates reasoning.

Tools

- Execute external actions.

Language Model

- Produces reasoning.

Conversation

- Stores interaction history.

This separation makes the system easier to maintain, test, and extend.

---

# Summary

The current educational Agent performs a single reasoning cycle.

This implementation intentionally prioritizes architectural clarity over algorithmic complexity.

Understanding this simplified workflow provides the conceptual foundation required to later study production Agent frameworks capable of iterative reasoning.

---

# Implementation Summary

## Objective

The objective of this phase was to understand how an AI Agent performs reasoning before generating a final response.

Rather than immediately answering the user, the Agent now follows an explicit reasoning workflow inspired by the ReAct (Reasoning + Acting) pattern.

The implementation prioritizes architectural clarity over production-level complexity.

---

# ReAct Pattern

The educational Agent now performs the following reasoning cycle:

```
User Request

↓

Thought

↓

Action

↓

Observation

↓

Final Reasoning

↓

Final Answer
```

Each stage is explicitly displayed during execution, allowing the complete reasoning process to be visualized.

---

# Tool Selection

The ToolAgent delegates Tool selection to the language model.

When the model determines that external information is required, it generates a Tool Call.

The Agent then:

1. Identifies the requested Tool.
2. Executes the Tool.
3. Receives the observation.
4. Sends the observation back to the language model.
5. Produces the final answer.

This separation keeps reasoning independent from Tool execution while maintaining clean software architecture.

---

# Reasoning Loop

Production AI Agents often execute multiple reasoning cycles before producing a final answer.

A simplified production workflow is:

```
Thought

↓

Action

↓

Observation

↓

Thought

↓

Action

↓

Observation

↓

...

↓

Final Answer
```

Each Observation becomes new information that the Agent uses during the next Thought.

For educational purposes, this repository intentionally implements a single reasoning cycle.

This decision keeps the architecture simple while illustrating the core concepts behind iterative Agent reasoning.

---

# Workflow Orchestration

The ToolAgent now acts as the workflow orchestrator.

Its responsibilities include:

- Receiving user requests.
- Invoking the language model.
- Detecting Tool Calls.
- Executing the appropriate Tool.
- Passing observations back to the language model.
- Returning the final response.

Individual Tools remain completely independent from the Agent.

---

# Responsibility Boundaries

The reasoning architecture preserves clear responsibility separation.

ToolAgent

- Coordinates the reasoning workflow.

Language Model

- Decides when a Tool is required.

Tools

- Execute external actions.

Conversation

- Maintains conversation history.

This separation improves readability, maintainability, testing, and future extensibility.

---

# Validation

The reasoning workflow was validated through:

- Unit tests.
- Integration tests.
- Manual demonstrations using Ollama.

The Agent successfully:

- Selected the appropriate Tool.
- Executed the Tool.
- Incorporated the observation.
- Generated a grounded final response.

---

# Lessons Learned

This phase demonstrated that modern AI Agents are more than language models.

An Agent combines:

- Language reasoning.
- External Tool usage.
- Workflow orchestration.
- Software engineering principles.

Although production Agent frameworks support iterative reasoning loops, planning, multiple Tool calls, and advanced execution graphs, a single reasoning cycle is sufficient to understand the underlying architecture.

This implementation establishes the conceptual foundation required for future Agentic AI systems.

---

# Engineering Concepts Reinforced

During this phase, the following software engineering concepts were reinforced:

- Workflow orchestration.
- Separation of responsibilities.
- Composition.
- Encapsulation.
- Modular architecture.
- Tool abstraction.
- Clean software boundaries.
- Educational implementation of the ReAct pattern.

---

# Conclusion

The AI Agent is now capable of reasoning about a user's request, selecting the appropriate Tool, incorporating external observations, and generating a grounded final answer.

With the completion of this phase, the project has evolved from a simple LLM wrapper into an educational Tool-Using AI Agent that demonstrates the essential architectural concepts behind modern Agentic AI systems.

The implementation intentionally stops after a single reasoning cycle to preserve the educational objective and avoid introducing the additional complexity of production-grade Agent frameworks.

The next phase introduces conversational memory, allowing the Agent to preserve context across multiple interactions while maintaining the same clean architectural principles.