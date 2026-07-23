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