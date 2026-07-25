# Phase 5 — Tool-Using Agent

## Session 1 — Tool Fundamentals

---

# Objective

Understand the role of tools in AI Agents.

The objective of this session is to understand why an LLM alone is not enough to create an Agent and how tools extend the capabilities of a language model.

The goal is not to build a complex Agent system, but to understand the fundamental mechanism behind tool-using Agents.

---

# What Is a Tool?

A tool is an external capability that an AI Agent can use to perform actions that are outside the natural abilities of a language model.

An LLM can:

- Understand language.
- Generate text.
- Reason over information contained in its context.

However, an LLM cannot directly:

- Execute calculations reliably.
- Access current information.
- Read local files.
- Interact with external systems.

A tool provides a controlled interface between the Agent and an external capability.

Conceptually:

```
User

↓

AI Agent

↓

Tool

↓

External Capability

↓

Result

↓

AI Agent

↓

Final Response
```

---

# Tool vs Normal Function

A tool is implemented as a function, but it has additional information that allows an Agent to understand when and how to use it.

A normal function:

```
Function

↓

Input

↓

Execution

↓

Output
```

A tool:

```
Tool

↓

Name

↓

Description

↓

Input Schema

↓

Execution Logic

↓

Output
```

The additional metadata allows the LLM to reason about available capabilities.

---

# Why Do Agents Need Tools?

LLMs have powerful language capabilities, but they have limitations.

Tools allow Agents to overcome these limitations.

Examples:

## Without Tools

User:

```
What is the current time?
```

LLM:

```
I do not know the current time.
```

The model has no access to real-time information.

---

## With Tools

```
User

↓

Agent

↓

Need current time?

↓

Clock Tool

↓

Current time

↓

Final response
```

The Agent extends its capability through the tool.

---

# LLM Limitations

## 1. No Real-Time Knowledge

Most LLMs have a knowledge cutoff.

They cannot automatically know:

- current time.
- current weather.
- latest events.
- current database information.

Tools provide access to updated information.

---

## 2. No Direct Access to External Systems

An LLM cannot directly:

- query databases.
- access files.
- call APIs.
- execute software.

Tools create controlled access to these systems.

---

## 3. Limited Computational Reliability

LLMs can perform reasoning, but they are not designed to be calculators.

For example:

```
123456 * 789123
```

A calculator tool provides deterministic computation.

---

## 4. No Independent Actions

A normal LLM generates responses.

It does not:

- decide to call external systems.
- execute operations.
- modify environments.

Tools combined with Agent logic enable action.

---

# Chatbot vs Agent

The main difference between a chatbot and an Agent is the ability to take actions using external capabilities.

---

# Traditional Chatbot

Architecture:

```
User

↓

Chatbot

↓

LLM

↓

Response
```

The model only generates text.

The interaction is limited to:

- receiving information.
- generating answers.

---

# Tool-Using Agent

Architecture:

```
User

↓

Agent

↓

Decision

↓

Need Tool?

↓

Yes

↓

Execute Tool

↓

Use Result

↓

Final Response
```

The Agent introduces decision-making and external interaction.

---

# Key Difference

A chatbot answers.

An Agent decides and acts.

A chatbot:

```
Input

↓

Generate Response
```

An Agent:

```
Input

↓

Understand Goal

↓

Decide Action

↓

Use Capability

↓

Observe Result

↓

Generate Response
```

---

# Tool Lifecycle

A tool-using Agent follows a sequence of steps.

---

## Step 1 — User Request

The user provides a goal.

Example:

```
Calculate 25 multiplied by 8.
```

---

## Step 2 — Agent Understanding

The Agent analyzes the request.

It determines:

- What does the user need?
- Can the LLM answer directly?
- Is an external capability required?

---

## Step 3 — Tool Selection

The Agent decides whether a tool is necessary.

Example:

```
Need calculation.

Select Calculator Tool.
```

---

## Step 4 — Tool Execution

The Agent sends the required input.

Example:

```
Calculator Tool

Input:
25 * 8

Output:
200
```

---

## Step 5 — Observation

The Agent receives the tool result.

The result becomes new information available to the Agent.

---

## Step 6 — Final Response

The Agent combines:

- user request.
- reasoning.
- tool result.

Then generates the final answer.

---

# Complete Tool Lifecycle Diagram

```
User Request

↓

Agent

↓

Decision

↓

Tool Required?

↓

Yes

↓

Tool Selection

↓

Tool Execution

↓

Observation

↓

Final Response
```

---

# Connection With Previous Phases

Tools build on concepts already learned.

## Phase 3 — LangChain Foundations

LangChain provides abstractions to organize:

- models.
- messages.
- prompts.
- components.

---

## Phase 4 — Structured Outputs

Structured outputs provide reliable communication between the LLM and the application.

Tools require structured information such as:

- tool name.
- parameters.
- expected outputs.

---

# Engineering Perspective

Tools represent a separation of responsibilities.

The LLM is responsible for:

- understanding language.
- reasoning.
- deciding.

The tool is responsible for:

- executing deterministic operations.

Conceptually:

```
LLM

Reasoning

+

Tool

Execution

=

Agent Capability
```

---

# Key Takeaways

- A tool extends an LLM with external capabilities.
- Agents need tools because LLMs cannot directly interact with the world.
- A chatbot generates responses; an Agent can decide and act.
- Tools require clear interfaces and responsibilities.
- Tool usage follows a lifecycle: request → decision → execution → observation → response.
- LangChain provides abstractions to build tool-using Agents.
- Understanding the underlying concepts is more important than using advanced 

## Session 2 — Tool Calling

---

# Objective

Understand how an AI Agent decides to use external tools and how LangChain supports this process.

The goal of this session is to understand the concepts behind Tool Calling before implementing any tools.

This session focuses on the reasoning process rather than the implementation details.

---

# What Is Tool Calling?

Tool Calling is the mechanism that allows an AI Agent to use external capabilities when answering a user's request.

Instead of always generating a response directly, the Agent can decide that solving the user's problem requires executing a tool.

Conceptually:

```
User Request

↓

Agent

↓

Reasoning

↓

Tool Needed?

↓

Yes

↓

Execute Tool

↓

Receive Result

↓

Generate Final Response
```

Tool Calling is therefore an extension of the Agent's reasoning process.

---

# Tool Calling vs Calling a Python Function

A normal Python program decides exactly when to execute a function.

Example:

```
Program

↓

calculator()

↓

Result
```

The programmer controls every decision.

---

An AI Agent behaves differently.

The programmer provides the available tools, but the Agent decides whether one of them should be used.

Conceptually:

```
Developer

↓

Provide Available Tools

↓

Agent

↓

Reasoning

↓

Choose Tool

↓

Execute Tool
```

The important difference is that the decision belongs to the Agent, not to the programmer.

---

# Why Doesn't the LLM Call Functions Directly?

An LLM only generates text (or structured outputs).

It cannot directly execute Python code.

Instead, it produces structured information describing:

- which tool should be used,
- what parameters should be passed,
- why the tool is required.

The application then executes the tool safely.

Conceptually:

```
LLM

↓

Tool Request

↓

Application

↓

Execute Tool

↓

Return Result

↓

LLM

↓

Final Response
```

This separation improves security and reliability.

---

# Tool Metadata

Every tool exposes descriptive information that allows the Agent to understand its purpose.

Typical metadata includes:

- Tool name
- Description
- Expected inputs
- Expected outputs

Example:

```
Calculator

Description:

Perform arithmetic calculations.
```

The Agent uses this information during its reasoning process.

---

# Tool Schema

A tool also defines the structure of its inputs.

Conceptually:

```
Calculator

Input

↓

Expression

↓

Output

↓

Number
```

The schema tells the Agent exactly how the tool should be called.

This idea is closely related to the data contracts introduced in Phase 4.

---

# How Does the Agent Choose a Tool?

The Agent performs an internal reasoning process.

Example:

User:

```
What is 25 × 18?
```

Reasoning:

```
This requires arithmetic.

↓

Calculator Tool

↓

Execute

↓

Receive Result

↓

Generate Response
```

The Agent selects the tool because it is better suited than the language model for this task.

---

# LangChain Tool Abstraction

LangChain provides a standard abstraction for tools.

Instead of manually managing:

- tool names,
- descriptions,
- input schemas,
- execution,

LangChain groups these concepts into a single Tool abstraction.

Conceptually:

```
Tool

↓

Metadata

+

Schema

+

Execution Logic
```

This allows the Agent to reason about tools in a consistent way.

---

# Tool Calling Lifecycle

A complete Tool Calling workflow follows these steps.

```
User Request

↓

Agent

↓

Reasoning

↓

Tool Selection

↓

Tool Execution

↓

Observation

↓

Final Response
```

Each step has a clear responsibility.

---

# Relationship with Structured Outputs

In Phase 4 we learned how an LLM can return structured data instead of free-form text.

Tool Calling uses the same philosophy.

Instead of returning only text, the LLM can generate structured information describing:

- selected tool,
- tool arguments,
- expected execution.

Conceptually:

```
Structured Output

↓

Tool Name

+

Arguments

↓

Application

↓

Tool Execution
```

Structured Outputs therefore provide the foundation for reliable Tool Calling.

---

# Our Educational Tools

During this project the Agent will learn to use only three tools.

## Calculator

Purpose:

Perform deterministic arithmetic calculations.

---

## Clock

Purpose:

Provide the current date and time.

---

## File Reader

Purpose:

Read local text files.

---

These tools were intentionally selected because they demonstrate three different categories of external capabilities:

```
Calculator

↓

Computation

------------------------

Clock

↓

Real-Time Information

------------------------

File Reader

↓

External Knowledge
```

Together they illustrate the most common reasons why an Agent needs tools.

---

# Engineering Perspective

Tool Calling demonstrates an important software engineering principle.

The Agent should not perform every responsibility itself.

Instead:

```
Agent

↓

Reasoning

------------------

Tool

↓

Execution
```

Reasoning and execution remain separate responsibilities.

This improves maintainability and extensibility.

---

# Connection with Previous Phases

Phase 3 introduced LangChain abstractions.

↓

Phase 4 introduced Structured Outputs and data contracts.

↓

Phase 5 combines both concepts so the Agent can make reliable decisions about external capabilities.

Each phase builds directly on the previous one.

---

# Key Takeaways

- Tool Calling allows an Agent to extend its capabilities beyond language generation.
- The Agent decides when a tool is required.
- The LLM does not directly execute Python code.
- Tool metadata helps the Agent understand available capabilities.
- Tool schemas define valid inputs.
- LangChain provides a standard abstraction for tools.
- Structured Outputs make Tool Calling reliable.
- Tool Calling separates reasoning from execution, following good software engineering practices.

## Session 3 — Agent Decisions

---

# Objective

Understand how an AI Agent decides whether it should answer a user's request directly or use an external tool.

The objective of this session is to understand the decision-making process that differentiates an AI Agent from a traditional chatbot.

An Agent is not simply a chatbot with access to tools.

An Agent reasons about the user's objective before deciding what action should be taken.

---

# What Is an Agent Decision?

Every user request requires the Agent to make a decision.

Conceptually:

```
User Request

↓

Understand Intent

↓

Can I answer directly?

↓

Yes ──────────────► Generate Response

↓

No

↓

Need External Capability?

↓

Select Tool

↓

Execute Tool

↓

Observe Result

↓

Generate Response
```

The Agent continuously evaluates the user's request before taking any action.

---

# Decision Before Execution

One of the most important architectural ideas is that deciding and executing are different responsibilities.

The Agent decides.

The Tool executes.

Conceptually:

```
Agent

↓

Decision

-----------------------

Tool

↓

Execution
```

The Agent never performs the work of the tool.

Instead, it delegates the task to the appropriate external capability.

---

# Decision Criteria

How does an Agent know whether a tool is needed?

The Agent compares the user's request with the available capabilities.

Examples:

---

## Arithmetic

User:

```
Calculate 125 × 48.
```

Reasoning:

```
This requires deterministic computation.

↓

Calculator Tool
```

---

## Current Time

User:

```
What time is it?
```

Reasoning:

```
Current information required.

↓

Clock Tool
```

---

## File Reading

User:

```
Summarize notes.txt
```

Reasoning:

```
Need file contents.

↓

File Reader Tool
```

---

## General Knowledge

User:

```
Explain supervised learning.
```

Reasoning:

```
No external capability required.

↓

Answer directly.
```

---

# Choosing Between Multiple Tools

As the number of available tools grows, the Agent must determine which one best satisfies the user's request.

Conceptually:

```
User Request

↓

Reasoning

↓

Available Tools

↓

Compare Descriptions

↓

Best Match

↓

Execute
```

The Agent should choose the tool whose purpose most closely matches the user's objective.

---

# When NOT to Use a Tool

A good Agent avoids unnecessary tool usage.

Example:

User:

```
Explain what overfitting means.
```

There is no need to:

- call the Calculator,
- call the Clock,
- read a file.

The LLM already possesses the knowledge required to answer.

Using a tool unnecessarily increases latency and complexity.

One characteristic of a good Agent is that it knows when *not* to use a tool.

---

# Examples

## Example 1

User:

```
What is 84 divided by 12?
```

Decision:

```
Calculator Tool
```

---

## Example 2

User:

```
What day is today?
```

Decision:

```
Clock Tool
```

---

## Example 3

User:

```
Summarize project.txt
```

Decision:

```
File Reader Tool
```

---

## Example 4

User:

```
Explain neural networks.
```

Decision:

```
No Tool

↓

Direct Response
```

---

# Incorrect Decisions

An Agent can also make poor decisions.

Example:

```
User

↓

Explain Machine Learning.

↓

Calculator Tool
```

The selected tool does not solve the user's problem.

Good tool descriptions and clear reasoning reduce these errors.

---

# Failure Scenarios

An Agent must also consider that tools are external systems.

Possible situations include:

- Tool unavailable.
- Invalid input.
- Unexpected error.
- Empty response.

Conceptually:

```
Agent

↓

Tool

↓

Failure

↓

Handle Error

↓

Generate Safe Response
```

In this project we will implement only simple error handling.

Advanced recovery strategies belong to more sophisticated Agent architectures.

---

# Engineering Perspective

Decision-making is an independent responsibility.

```
Agent

↓

Reasoning

↓

Decision

↓

Tool

↓

Execution
```

Keeping these responsibilities separate improves:

- readability,
- maintainability,
- extensibility.

This follows the Single Responsibility Principle introduced earlier in the roadmap.

---

# Connection with Previous Phases

Phase 3 introduced LangChain abstractions.

↓

Phase 4 introduced Structured Outputs and data contracts.

↓

Phase 5 combines both ideas so the Agent can reason about available capabilities and choose the correct tool.

The Agent's reasoning is therefore built upon everything learned in the previous phases.

---

# Looking Ahead

The next step is to implement our first real tool.

The Calculator Tool will allow the Agent to execute deterministic arithmetic operations.

This will be our first example of an Agent making a decision, selecting a tool, executing it, and incorporating the result into the final response.

---

# Key Takeaways

- An AI Agent makes decisions before taking actions.
- Decision-making and execution are separate responsibilities.
- The Agent selects tools based on the user's objective.
- Good Agents avoid unnecessary tool usage.
- Tool descriptions are essential for correct tool selection.
- External tools may fail, so the Agent must handle failures gracefully.
- Separating reasoning from execution leads to better software architecture.
- The concepts learned in Phases 3 and 4 provide the foundation for Agent decision-making.