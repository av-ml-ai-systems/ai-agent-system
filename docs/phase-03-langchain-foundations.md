# Phase 03 — LangChain Foundations

## Objective

Understand how LangChain helps organize LLM applications.

The objective of this phase is **not** to learn every LangChain feature.

Instead, the goal is to understand the core concepts that support modern LLM applications and AI agents.

---

## Learning Goals

- Understand why LangChain exists.
- Understand the problems it solves.
- Learn the main components of LangChain.
- Understand Chat Models.
- Understand Messages.
- Learn Prompt Templates.
- Learn the basics of LCEL (LangChain Expression Language).
- Build simple educational chains.

---

## Engineering Concepts

- Separation of concerns
- Dependency management
- Composition

---

# Session 1 — Why LangChain Exists

## Why Does LangChain Exist?

Large Language Models (LLMs) such as OpenAI, Ollama, Anthropic, and Gemini provide powerful language capabilities. However, interacting directly with each provider quickly becomes repetitive and difficult to maintain.

Every provider has its own API, configuration, request format, and response format.

Without a common framework, changing from one provider to another often requires modifying multiple parts of an application.

LangChain was created to provide a consistent programming model for building LLM applications while reducing provider-specific code.

---

## What Problem Does LangChain Solve?

LangChain addresses several common problems:

- Different LLM providers expose different APIs.
- Prompt construction becomes repetitive.
- Managing conversations requires handling message history.
- Applications often need reusable pipelines that combine prompts, models, and outputs.
- Switching providers should require minimal application changes.

Instead of solving these problems independently in every project, LangChain provides reusable abstractions.

---

## Why Not Call Ollama Directly?

Calling Ollama directly is perfectly acceptable for very small experiments.

Example:

```
Application

↓

Ollama
```

This approach is simple but tightly couples the application to a specific provider.

If the application later needs to use OpenAI or Anthropic, several parts of the code may need to change.

Using LangChain introduces an additional abstraction:

```
Application

↓

LangChain

↓

Ollama
```

Now the application communicates with LangChain, while LangChain communicates with the provider.

This separation makes applications easier to maintain, extend, and test.

---

## What Abstraction Does LangChain Provide?

LangChain does not replace LLM providers.

Instead, it provides common abstractions that work across many providers.

Some of the most important abstractions are:

- Chat Models
- Messages
- Prompt Templates
- Output Parsers
- Chains
- Tools
- Memory

These abstractions allow developers to focus on application logic rather than provider-specific implementation details.

---

## Relationship with Our Project

During Phase 2, we built a software architecture that already follows many of the same principles promoted by LangChain.

Current project architecture:

```
User

↓

Agent

↓

Prompt

↓

ChatModel

↓

OllamaChat

↓

Ollama
```

The Agent depends only on the `ChatModel` abstraction.

The provider-specific implementation (`OllamaChat`) is isolated behind that abstraction.

In the following sections of this phase, we will progressively replace low-level interactions with LangChain components while preserving the same overall architecture.

The Agent will continue depending on abstractions rather than directly interacting with Ollama.

---

## Key Takeaways

- LangChain standardizes interaction with different LLM providers.
- It reduces provider-specific code.
- It encourages reusable and modular application design.
- It provides abstractions for prompts, messages, models, chains, and tools.
- Our project already follows many of the same architectural principles introduced by LangChain.

---

# Session 2 — LangChain Core Components

## Overview

LangChain organizes LLM applications into reusable building blocks.

Instead of interacting directly with an LLM provider, applications are built by composing components with well-defined responsibilities.

The core components introduced in this session are:

- Chat Models
- Messages
- Prompt Templates
- Chains

Together, they form the foundation of most LangChain applications.

---

## Chat Models

A Chat Model represents a conversational Large Language Model.

LangChain provides a common interface for different providers.

Examples include:

- ChatOpenAI
- ChatOllama
- ChatAnthropic
- ChatGoogleGenerativeAI

Although these providers communicate with different APIs, LangChain exposes a similar interface for all of them.

This allows applications to switch providers with minimal changes.

Example:

```
Application

↓

Chat Model

↓

LLM Provider
```

---

## Messages

Unlike traditional text generation APIs that receive a single string, chat models operate on a conversation.

A conversation is represented as an ordered list of messages.

The three most common message types are:

- **SystemMessage**
  - Defines the assistant's behavior or instructions.

- **HumanMessage**
  - Represents user input.

- **AIMessage**
  - Represents the model's response.

Example conversation:

```
SystemMessage

↓

HumanMessage

↓

AIMessage

↓

HumanMessage

↓

AIMessage
```

This representation makes it easier to manage multi-turn conversations.

---

## Prompt Templates

A prompt should not be hardcoded whenever possible.

Instead, prompts can be represented as reusable templates.

Prompt templates separate:

- Static instructions.
- Dynamic user input.

This improves readability, maintainability, and reuse.

Later in this phase, we will study:

- PromptTemplate
- ChatPromptTemplate

---

## Chains

A Chain connects multiple components into a processing pipeline.

Instead of manually calling each component, LangChain allows them to be composed together.

Conceptually:

```
Prompt

↓

Chat Model

↓

Response
```

As applications become more sophisticated, additional components can be added to the pipeline.

Chains encourage modular design and reduce repetitive code.

---

## Relationship with Our Project

Many of these concepts already exist in our architecture.

For example:

```
User

↓

Agent

↓

Prompt

↓

ChatModel

↓

OllamaChat

↓

Ollama
```

Our `ChatModel` abstraction plays a role similar to LangChain's Chat Models.

Our Prompt abstraction prepares the application for LangChain Prompt Templates.

This means our current architecture aligns naturally with the concepts introduced by LangChain.

In the following sections, we will begin replacing custom implementations with LangChain components where appropriate, while preserving the overall architecture.

---

## Key Takeaways

- LangChain applications are built from reusable components.
- Chat Models provide a common interface for different LLM providers.
- Conversations are represented as lists of Messages.
- Prompt Templates separate prompt definition from application logic.
- Chains connect multiple components into a reusable workflow.
- Our project architecture already shares many of the same design principles.

---

# Session 3 — How Our Project Fits into LangChain

## Overview

By the end of Phase 2, our project already follows many of the architectural principles promoted by LangChain.

This was intentional.

Instead of tightly coupling the Agent to a specific LLM provider, we designed the application around abstractions with clear responsibilities.

Because of this, integrating LangChain becomes a natural evolution rather than a complete redesign.

---

## Before LangChain

Without a framework, the application communicates directly with the LLM provider.

Example:

```
User

↓

Agent

↓

Ollama
```

Although simple, this approach tightly couples the application to a specific provider.

Changing providers requires modifying the application.

---

## With LangChain

LangChain introduces reusable abstractions between the application and the provider.

Conceptually:

```
User

↓

Agent

↓

LangChain

↓

Ollama
```

The application no longer depends directly on Ollama.

Instead, it depends on LangChain abstractions.

This makes the application easier to maintain and extend.

---

## Our Current Architecture

After completing Phase 2, our architecture is:

```
User

↓

Agent

↓

Prompt

↓

ChatModel

↓

OllamaChat

↓

Ollama
```

Each component has a single responsibility.

- **Agent**
  - Coordinates the conversation.

- **Prompt**
  - Organizes prompt creation.

- **ChatModel**
  - Defines the abstraction for conversational models.

- **OllamaChat**
  - Implements the ChatModel abstraction using Ollama through LangChain.

This separation follows the same philosophy encouraged by LangChain.

---

## Why We Built This Architecture

The purpose was not to create a complex architecture.

The purpose was to prepare the project for the remaining phases.

Because responsibilities are already separated, we can now focus on learning LangChain features instead of redesigning the application.

The remaining phases will build on this foundation rather than replacing it.

---

## What Changes in Phase 3?

The architecture itself changes very little.

Instead, we begin learning how to use LangChain's existing components.

Examples include:

- PromptTemplate
- ChatPromptTemplate
- RunnableSequence (LCEL)

Rather than creating our own implementations, we will progressively adopt LangChain's abstractions where appropriate.

---

## Relationship with the Remaining Roadmap

The architecture completed in Phase 2 supports the rest of the project.

Future phases will focus on:

- Prompt engineering.
- Structured outputs.
- Tool calling.
- Reasoning.
- Memory.
- User interfaces.

The goal is to use LangChain effectively while keeping the project simple and educational.

---

## Key Takeaways

- Phase 2 established the architectural foundation.
- Phase 3 focuses on using LangChain rather than redesigning the application.
- Our current architecture already follows many LangChain design principles.
- Future phases will extend the application's capabilities without significantly increasing its complexity.
- The objective remains to **finish the first educational AI Agent**, not to build the ultimate AI Agent.

---
# 3.2 — Prompt Templates

# Session 4 — Prompt Templates Concepts

## Overview

Prompt templates are one of the core abstractions provided by LangChain.

They allow applications to separate prompt structure from dynamic user input.

Instead of creating prompts manually every time, developers define reusable templates that can receive different values.

This improves:

- Maintainability.
- Reusability.
- Readability.
- Separation between application logic and prompt design.

---

# PromptTemplate

## What is PromptTemplate?

`PromptTemplate` represents a reusable text template with variables that can be replaced dynamically.

Instead of creating a fixed prompt:

```
Answer this question:

What is artificial intelligence?
```

we create a template:

```
Answer this question:

{question}
```

The value of `{question}` can change depending on the user input.

---

## Why Use PromptTemplate?

Without templates:

- Prompts are hardcoded.
- Changing instructions requires modifying application code.
- Reusing prompts becomes difficult.

With templates:

- Prompt structure is defined once.
- Dynamic values are inserted when needed.
- Prompt management becomes easier.

---

# ChatPromptTemplate

## What is ChatPromptTemplate?

Modern LLM applications usually work with conversations instead of a single text string.

For this reason, LangChain provides `ChatPromptTemplate`.

It allows developers to define prompts using message roles:

- System messages.
- Human messages.
- AI messages.

A conversation prompt is represented as a sequence of messages.

```
System Message

↓

Human Message

↓

AI Response
```

---

## Why ChatPromptTemplate Exists

A simple text prompt does not explicitly represent conversation roles.

For example:

```
You are a helpful assistant.

Question:
What is machine learning?
```

contains instructions and user input in one text block.

A chat prompt separates responsibilities:

```
System Message

↓

Human Message
```

This makes the intention of each message clearer.

---

# Variables in Prompts

## What Are Prompt Variables?

Variables are placeholders inside a prompt that receive values at execution time.

Example concept:

```
Hello {name}
```

The value of `{name}` is provided later.

This allows the same prompt structure to be reused with different inputs.

---

## Why Variables Matter

Variables allow:

- Dynamic user inputs.
- Reusable prompt structures.
- Cleaner application code.
- Easier prompt modification.

The application provides the data.

The prompt template defines how that data is organized.

---

# Message Placeholders

## What Are Message Placeholders?

In conversational applications, prompts often need to include previous messages.

Message placeholders allow dynamic insertion of conversation history.

Example concept:

```
System Message

↓

Previous Conversation

↓

New User Message

↓

Chat Model
```

Instead of manually rebuilding the entire conversation every time, the application can insert the existing messages into the prompt.

---

## Why Message Placeholders Are Important

They prepare the application for:

- Conversation history.
- Short-term memory.
- Multi-turn interactions.

This concept will become important later in:

- Phase 5 — Tool-Using Agent.
- Phase 6 — Reasoning & Agent Workflow.
- Phase 7 — Memory & Conversation State.

---

# Relationship With Our Project

Before Prompt Templates:

```
Agent

↓

Prompt

↓

ChatModel

↓

Ollama
```

After introducing LangChain Prompt Templates:

```
Agent

↓

ChatPromptTemplate

↓

ChatModel

↓

Ollama
```

The Agent still coordinates the application flow.

The prompt responsibility moves into LangChain's prompt abstraction.

---

# Engineering Concepts

## Separation of Concerns

Prompt design should not be mixed with application logic.

The Agent should not contain large prompt strings.

Instead:

- Agent manages interaction.
- Prompt templates manage instructions.
- Chat models generate responses.

---

## Reusability

A prompt template can be reused with different inputs.

The structure remains constant while the data changes.

---

## Composition

Prompt templates are designed to be combined with other LangChain components.

Later, this will allow:

```
Prompt

↓

Chat Model

↓

Output
```

and eventually complete chains using LCEL.

---

# Key Takeaways

- PromptTemplate creates reusable prompts with variables.
- ChatPromptTemplate represents conversations using message roles.
- Variables allow dynamic information to be inserted into prompts.
- Message placeholders allow conversation history to be included dynamically.
- Prompt templates separate prompt design from application logic.
- Prompt templates are the foundation for LangChain chains and more advanced agent behaviors.

---

# Session 6 — Prompt Composition

## Overview

In LangChain, components are designed to be combined together.

Instead of creating one large object responsible for everything, applications are built by connecting smaller components with clear responsibilities.

This concept is called composition.

A prompt is one component.

A Chat Model is another component.

Together, they can form a processing workflow.

---

# What Is Prompt Composition?

Prompt composition means combining a prompt component with other components to create a complete LLM interaction.

A prompt does not generate answers.

A model does not know how to organize application instructions.

Each component has a specific responsibility.

Conceptually:

```
User Input

↓

Prompt Template

↓

Chat Model

↓

Response
```

The prompt prepares the information.

The model generates the answer.

---

# Why Composition Matters

Without composition, application logic often becomes tightly coupled.

Example:

```
Agent

├── Prompt creation
├── Message formatting
├── Model communication
└── Response handling
```

The Agent becomes responsible for too many things.

With composition:

```
Agent

↓

Prompt

↓

Chat Model

↓

Response
```

Each component focuses on one responsibility.

---

# Composition vs Inheritance

LangChain encourages composition instead of creating complex class hierarchies.

Composition means:

"Build larger behavior by combining smaller components."

Example:

```
Prompt

+

Chat Model

=

LLM Application Workflow
```

This approach is easier to understand, modify, and test.

---

# Relationship With Our Project

Our current architecture already follows this principle.

Current architecture:

```
Agent

↓

PromptTemplate

↓

ChatModel

↓

Ollama
```

Each component has a clear responsibility:

## Agent

Responsible for:

- Receiving user requests.
- Coordinating the interaction.
- Managing conversation flow.

## PromptTemplate

Responsible for:

- Creating messages.
- Organizing instructions.
- Formatting dynamic information.

## ChatModel

Responsible for:

- Sending messages to the LLM.
- Receiving model responses.

---

# Preparation for Chains

Prompt composition is the foundation for LangChain Chains.

A Chain connects components into a reusable workflow.

Conceptually:

```
Prompt

↓

Chat Model

↓

Output
```

Later, in Phase 3.3, we will learn how LangChain Expression Language (LCEL) allows these components to be connected.

---

# Important Design Principle

Composition should only be introduced when it improves clarity.

The goal is not to create many layers.

The goal is to connect responsibilities in a simple and understandable way.

For this educational project:

- We use composition to understand LangChain.
- We avoid unnecessary abstractions.
- We keep the Agent simple.

---

# Key Takeaways

- Composition means combining small components to create larger behavior.
- Prompt templates and chat models are independent components.
- LangChain applications are built by connecting components.
- Composition improves separation of responsibilities.
- Chains and LCEL are based on this composition principle.
- Our project architecture already follows this idea.

---

# Phase 3.3 — Chains

## Objective

Understand how LangChain connects components together.

The goal is not to build complex workflows or advanced agent architectures.

The goal is to understand the mechanism LangChain provides to compose smaller components into an LLM application pipeline.

---

# Why Chains Exist

An LLM application usually requires multiple steps.

For example:

- Create a prompt.
- Send the prompt to a model.
- Process the response.

Without a composition mechanism, the application code may become responsible for manually connecting every component.

Example:

```
Application

↓

Create Messages

↓

Call Model

↓

Process Response
```

As applications grow, manually managing these interactions can become harder to maintain.

LangChain introduces Chains to make component composition explicit.

---

# What Is a Chain?

A Chain is a sequence of connected components where the output of one component becomes the input of another component.

Conceptually:

```
Component A

↓

Component B

↓

Component C
```

For an LLM application:

```
Prompt

↓

Chat Model

↓

Response
```

Each component has a specific responsibility.

The Chain coordinates the data flow between them.

---

# Relationship With Previous Architecture

Before Chains:

```
Agent

↓

PromptTemplate

↓

ChatModel

↓

Response
```

The Agent manually coordinates the interaction between the prompt and the model.

After introducing Chains:

```
Agent

↓

Chain

↓

Prompt

↓

ChatModel

↓

Response
```

The Chain becomes responsible for connecting components.

The Agent remains responsible for high-level coordination.

---

# Important Design Principle

Chains do not replace good software architecture.

They are a composition mechanism.

A poorly designed application can still become complex even when using Chains.

The goal is to use abstractions only when they improve clarity.

For this educational project:

- We learn Chains.
- We understand their purpose.
- We use them in a simple example.
- We avoid unnecessary layers.

---

# Connection With Composition

Chains are based on the idea of composition.

Instead of creating one large component:

```
Agent

├── Prompt logic
├── Model logic
├── Processing logic
└── Response logic
```

we combine smaller components:

```
Prompt

+

Chat Model

+

Processing Step

=

Application Workflow
```

This improves separation of responsibilities.

---

# Preparation for LCEL

LangChain Expression Language (LCEL) is the syntax and system used by LangChain to compose runnable components.

LCEL allows developers to express workflows by connecting components together.

Conceptually:

```
Prompt

↓

Model

↓

Output
```

Later, we will implement this using LangChain's Runnable system.

---

# Key Learning Objectives

By the end of Phase 3.3, we should understand:

- Why LangChain uses Chains.
- How components are composed.
- What LCEL represents.
- How data flows through a chain.
- The difference between a direct model call and a composed pipeline.
- When composition improves clarity.

---

# Scope Limitations

This project will not include:

- Complex chain architectures.
- Multiple nested chains.
- Production workflow orchestration.
- Advanced LangChain features.

Those concepts belong to larger AI system projects.

The objective here is to understand the foundation.

---

---

# Session 1 — LCEL Fundamentals

## Objective

Understand the purpose of LangChain Expression Language (LCEL) and how it enables component composition in LangChain applications.

The objective is not to memorize syntax.

The objective is to understand the architectural idea behind LCEL:

> Connecting independent components into a workflow.

---

# Why LCEL Exists

LLM applications usually require multiple steps.

For example:

```
User Input

↓

Create Prompt

↓

Generate Messages

↓

Call Model

↓

Process Response
```

In a simple application, these steps can be manually implemented.

However, as applications grow, manually connecting components can make the code harder to maintain.

The developer becomes responsible for managing:

- data flow,
- component interaction,
- execution order,
- intermediate results.

LangChain introduced LCEL to make these connections explicit and easier to compose.

---

# What Is LCEL?

LCEL stands for:

**LangChain Expression Language**

LCEL is a way to compose LangChain components into runnable workflows.

Instead of manually orchestrating every step, components can be connected together.

Conceptually:

```
Component A

↓

Component B

↓

Component C
```

The output of one component becomes the input of the next component.

---

# Runnable Concept

LCEL is based on the concept of **Runnable components**.

A Runnable is a component that receives an input and produces an output.

Conceptually:

```
Input

↓

Runnable

↓

Output
```

Examples of LangChain components that can behave as Runnables:

- Prompt templates.
- Chat models.
- Output parsers.
- Other processing components.

Because these components follow a common interface, they can be composed together.

---

# Component Composition

The main idea behind LCEL is composition.

Instead of creating one large component:

```
Agent

├── Prompt creation
├── Model communication
├── Response processing
└── Workflow logic
```

LangChain encourages combining smaller components:

```
Prompt

+

Chat Model

+

Output Processing

=

Application Workflow
```

Each component maintains a clear responsibility.

---

# Pipe Operator

LCEL commonly uses the pipe operator:

```
|
```

The meaning is:

> The output of one component becomes the input of the next component.

Conceptually:

```
Component A

|

Component B
```

represents:

```
Input

↓

Component A

↓

Component B

↓

Output
```

The pipe operator makes the workflow structure visible.

---

# Prompt → Model Pipeline

A basic LLM workflow can be represented as:

```
Prompt

↓

Chat Model

↓

Response
```

The execution flow is:

1. The prompt receives application data.
2. The prompt creates the required messages.
3. The chat model receives those messages.
4. The model generates a response.

---

# Relationship With Our Agent Architecture

Before introducing Chains:

```
Agent

↓

PromptTemplate

↓

ChatModel

↓

Response
```

The Agent coordinates the interaction.

After introducing Chains:

```
Agent

↓

Chain

↓

Prompt

↓

ChatModel

↓

Response
```

The Chain becomes responsible for connecting components.

The Agent remains responsible for high-level coordination.

---

# LCEL Does Not Create an Agent

Important distinction:

LCEL is a composition mechanism.

It does not provide:

- decision making,
- tools,
- reasoning,
- memory,
- autonomous behavior.

Those concepts belong to later phases.

An Agent requires additional capabilities beyond a chain.

---

# Relationship Between Chains and LCEL

Chains in modern LangChain applications are commonly built using LCEL.

LCEL provides the mechanism to connect:

- prompts,
- models,
- parsers,
- other runnable components.

A Chain represents the composed workflow.

---

# Engineering Concepts

## Separation of Concerns

Each component focuses on one responsibility.

Example:

```
Prompt

Responsible for:

- Instructions
- Message creation
```

```
Chat Model

Responsible for:

- Communication with the LLM
```

---

## Composition

Complex behavior is created by combining smaller components.

Instead of increasing the complexity of individual classes, functionality is created through connections between components.

---

## Dependency Management

LangChain components can be replaced or modified because the application depends on clear interfaces.

---

# Key Takeaways

- LCEL is LangChain's composition language.
- LCEL connects runnable components into workflows.
- A Runnable receives input and produces output.
- The pipe operator represents component composition.
- Chains are created by composing components.
- LCEL improves readability and separation of responsibilities.
- LCEL is not an Agent framework; it is a workflow composition mechanism.

---

# Phase 3.3 Scope Reminder

For this educational project:

We will use LCEL to understand:

- component composition,
- prompt-model pipelines,
- simple chains.

We will not build:

- complex chain architectures,
- workflow engines,
- enterprise orchestration systems.

The objective is understanding, not creating a framework.

---

---

# Session 2 — Prompt → Model Pipeline Implementation

## Objective

Implement a small educational example to demonstrate how LangChain Expression Language (LCEL) connects components together.

The goal is not to modify the Agent architecture.

The goal is to observe how independent LangChain components can be composed into a simple workflow.

---

# What We Implemented

A simple LCEL pipeline was created:

```
ChatPromptTemplate

↓

ChatOllama

↓

Response
```

The implementation uses:

- `ChatPromptTemplate` to create messages.
- `ChatOllama` to communicate with the local LLM.
- LCEL composition to connect both components.

The execution flow is:

```
User Input

↓

Prompt Template

↓

Messages

↓

Chat Model

↓

AIMessage

↓

Response
```

---

# LCEL Composition

The central concept demonstrated is component composition.

The pipeline connects components using:

```
Prompt | Model
```

The meaning is:

"The output generated by the first component becomes the input of the next component."

In this example:

```
ChatPromptTemplate

↓

ChatOllama
```

The prompt receives the user input and generates the required messages.

The chat model receives those messages and generates the response.

---

# Why This Example Is Isolated

This example was intentionally created as a standalone learning artifact.

It does not modify the main Agent implementation.

Reason:

The objective of this session is to understand LCEL composition, not to redesign the application architecture.

The example focuses only on:

- LangChain components.
- Runnable composition.
- Data flow between components.

---

# Relationship With Main Agent Architecture

The main project architecture remains:

```
Agent

↓

PromptTemplate

↓

Conversation

↓

ChatModel

↓

Ollama
```

The Agent architecture focuses on software engineering principles:

- Separation of responsibilities.
- Dependency inversion.
- Testability.
- Clear component boundaries.

---

The LCEL example focuses on LangChain composition:

```
ChatPromptTemplate

↓

ChatOllama

↓

Response
```

It demonstrates how LangChain connects framework components.

---

# Why We Do Not Replace the Agent With LCEL Yet

Replacing the current architecture with an LCEL-based design would introduce a different learning objective:

- Architecture redesign.
- Responsibility changes.
- New abstractions.
- Additional testing requirements.

That is not required to understand LCEL.

The current architecture already provides a strong foundation for learning LangChain.

---

# Engineering Concepts Applied

## Composition

Small independent components are combined to create a workflow.

Example:

```
Prompt

+

Model

=

LLM Pipeline
```

---

## Separation of Concerns

Each component has a specific responsibility:

### Prompt

Responsible for:

- Instructions.
- Message formatting.
- Input transformation.

### Model

Responsible for:

- LLM communication.
- Response generation.

---

## Abstraction Boundaries

The project maintains two learning perspectives:

Application architecture:

```
Agent → Abstractions → Implementations
```

Framework composition:

```
LangChain Components → LCEL Pipeline
```

Both concepts are valuable and serve different purposes.

---

# Validation

Completed:

🟢 LCEL example execution

🟢 Ollama integration validation

🟢 Pre-commit validation

---

# Key Takeaways

- LCEL allows LangChain components to be composed into workflows.
- Prompts and models can be connected through a pipeline.
- The pipe operator represents data flow between components.
- A Chain is a composition of runnable components.
- LCEL is not the same as an Agent.
- Learning framework capabilities does not require redesigning the application architecture.

---

---

# Session 3 — RunnableSequence

## Objective

Understand how LangChain represents sequences of connected operations.

The goal is to understand:

- What a RunnableSequence is.
- How RunnableSequence relates to LCEL.
- How multiple components can be executed in order.
- The difference between deterministic workflows and Agents.

---

# What Is RunnableSequence?

A `RunnableSequence` represents a workflow where multiple runnable components are executed sequentially.

Each component receives the output from the previous component as its input.

Conceptually:

```
Runnable A

↓

Runnable B

↓

Runnable C
```

The sequence defines:

- execution order,
- data flow,
- component connection.

---

# Relationship With LCEL

LCEL allows developers to compose runnable components.

When using the pipe operator:

```
Component A | Component B
```

LangChain creates a composed workflow.

Conceptually:

```
Component A

↓

Component B
```

This composition is represented internally as a `RunnableSequence`.

---

# Example With LLM Components

A simple LLM pipeline:

```
ChatPromptTemplate

↓

ChatOllama

↓

Response
```

can be understood as:

```
RunnableSequence

    |

    ├── Prompt Runnable

    |

    └── Model Runnable
```

The prompt transforms input data into messages.

The model receives those messages and generates a response.

---

# Data Flow

The execution flow of a simple sequence is:

```
User Input

↓

Prompt Template

↓

Messages

↓

Chat Model

↓

AIMessage

↓

Response
```

Each component has a specific responsibility.

The sequence only coordinates the execution order.

---

# Why RunnableSequence Exists

Without composition, the application manually manages every step:

```
Input

↓

Call Prompt

↓

Receive Messages

↓

Call Model

↓

Receive Response
```

This approach works for small examples, but it becomes harder to maintain as workflows become larger.

RunnableSequence makes the workflow structure explicit:

```
Input

↓

RunnableSequence

↓

Output
```

---

# Composition Principle

RunnableSequence follows the software engineering principle of composition.

Instead of creating one large component:

```
LLM Application

├── Prompt logic
├── Model logic
├── Parsing logic
└── Validation logic
```

we combine smaller components:

```
Prompt

↓

Model

↓

Parser

↓

Validator
```

Each component maintains a clear responsibility.

---

# RunnableSequence vs Agent

A RunnableSequence is deterministic.

The execution path is predefined.

Example:

```
Input

↓

Step 1

↓

Step 2

↓

Step 3

↓

Output
```

The system always follows the same workflow.

---

An Agent is different.

An Agent introduces decision-making.

Conceptually:

```
User

↓

Agent

↓

Decision

↓

Tool

↓

Observation

↓

Decision

↓

Final Answer
```

An Agent can decide:

- which action to take,
- which tool to use,
- whether another step is required.

Agents will be explored later in:

- Phase 5 — Tool-Using Agent.
- Phase 6 — Reasoning & Agent Workflow.

---

# Relationship With Our Educational Project

Our LCEL demo:

```
ChatPromptTemplate

↓

ChatOllama

↓

Response
```

is a simple RunnableSequence.

The purpose was to learn:

- component composition,
- runnable workflows,
- data flow.

It was not intended to replace our Agent architecture.

---

# Why We Keep the Agent Architecture Separate

The current project architecture:

```
Agent

↓

PromptTemplate

↓

Conversation

↓

ChatModel

↓

Ollama
```

teaches software engineering concepts:

- separation of responsibilities,
- abstraction,
- dependency inversion,
- testability.

The LCEL example teaches:

```
LangChain Components

↓

Composition

↓

Workflow
```

Both concepts are useful but solve different problems.

---

# Engineering Concepts

## Composition

Complex workflows can be created by combining smaller components.

---

## Separation of Concerns

Each component focuses on one responsibility.

Example:

```
Prompt

Responsible for:

- Instructions
- Message creation
```

```
Model

Responsible for:

- LLM communication
- Response generation
```

---

## Workflow Design

A workflow describes how components interact and how data moves through the system.

---

# Scope Limitation

For this educational project, we only need to understand:

- Runnable components.
- Sequential execution.
- LCEL composition.
- Basic Chain concepts.

We will not implement:

- complex workflow engines,
- advanced orchestration,
- multiple nested chains.

Those belong to future AI system projects.

---

# Key Takeaways

- RunnableSequence represents ordered execution of runnable components.
- LCEL uses composition to create sequences.
- The pipe operator connects components together.
- Chains are compositions of runnable components.
- RunnableSequence is deterministic.
- Agents add decision-making capabilities on top of workflows.
- Understanding composition is a foundation for building larger AI systems.

---

## Phase 3 Status:

Completed ✅

Topics completed:

- Why LangChain exists
- LangChain architecture
- Chat Models
- Messages
- Prompt Templates
- ChatPromptTemplate
- Prompt variables
- LCEL fundamentals
- Prompt → Model pipeline
- RunnableSequence

## Implementation:

- LangChain prompt integration.
- LangChain Ollama integration.
- LCEL educational pipeline example.

## Validation:

- pre-commit run --all-files ✅