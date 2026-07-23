# Phase 2 - First Real LLM Integration

## 2.1 LLM Integration Foundations

Before integrating a real Large Language Model (LLM), it is important to understand the architectural principles that guide the design of the system.

The objective of this phase is not simply to connect an external AI model, but to integrate it while preserving a clean, maintainable, and extensible software architecture.

---

## LLM Abstraction

The project defines an `LLM` abstraction that represents the contract between the Agent and any Language Model.

The Agent never communicates directly with a specific provider or model. Instead, it interacts only with the `LLM` interface.

This design allows different implementations to be introduced without modifying the Agent.

Current architecture:

```
User

↓

Agent

↓

LLM (Contract)

↓

FakeLLM
```

The current implementation uses a FakeLLM exclusively for testing and educational purposes.

---

## Interface vs. Implementation

A fundamental software engineering principle is separating abstractions from implementations.

### Interface

The interface defines what an object is capable of doing.

For the current project, the LLM interface defines the operation required to obtain a response from a language model.

The interface does not contain implementation details.

### Implementation

An implementation defines how the interface is fulfilled.

Examples of possible implementations include:

- FakeLLM
- OllamaLLM
- OpenAILLM
- GeminiLLM

Each implementation satisfies the same interface while communicating with a different provider.

---

## Provider vs. Model

It is important to distinguish between providers and models.

A provider is the technology responsible for executing inference requests.

Examples include:

- Ollama
- OpenAI API
- Google Gemini API
- Azure OpenAI

A model is the actual Large Language Model executed by the provider.

Examples include:

- Llama 3
- DeepSeek
- Qwen
- Gemma
- Mistral

Changing the model does not necessarily require changing the software architecture.

---

## Layered Architecture

The project follows a layered architecture:

```
Application Layer

Agent

↓

Abstraction Layer

LLM

↓

Implementation Layer

OllamaLLM (future)

↓

Provider Layer

Ollama

↓

Model Layer

Llama 3

Each layer has a single responsibility.
```
---

## Dependency Inversion

The Agent depends only on the LLM abstraction.

It never depends directly on:

- Ollama
- OpenAI
- Gemini
- LangChain
- Any specific model

This follows the Dependency Inversion Principle.

When a new provider is introduced, a new implementation can be created without modifying the Agent.

For example:
```
Agent

↓

LLM

↓

GeminiLLM

↓

Google Gemini API

↓

Gemini 2.5 Pro

The same Agent can also operate with:

Agent

↓

LLM

↓

OllamaLLM

↓

Ollama

↓

Llama 3
```
---

## Separation of Responsibilities

Each component has a well-defined responsibility.

Agent

- Coordinates the interaction.
- Delegates requests to an LLM.
- Returns the generated response.

LLM

- Defines the contract.

LLM Implementation

- Communicates with a provider.
- Sends prompts.
- Receives responses.
- Returns results through the LLM interface.

Provider

- Executes inference requests.

Model

- Generates the response.

---

## Engineering Principles Applied

- Dependency Injection
- Dependency Inversion Principle
- Open/Closed Principle
- Single Responsibility Principle
- Separation of Concerns
- Programming to Abstractions

---

## Key Takeaways

- The Agent never communicates directly with a provider.
- The LLM interface isolates the application from infrastructure.
- Providers and models are different concepts.
- New providers are introduced through new implementations.
- The architecture remains stable even when technologies change.

---

## Summary

The project is now architecturally prepared to replace the FakeLLM with a real implementation while preserving a clean, modular, and extensible design.

The next section introduces Ollama and explains its role within this architecture before integrating the first real Language Model.

## 2.2 — Introduce Ollama

### 2.2.1 — Ollama Fundamentals

Before integrating a real Large Language Model into the project, it is important to understand the role of Ollama within the system architecture.

Ollama is not a Language Model. It is the software responsible for running Large Language Models locally and exposing an API that applications can use to perform inference.

The objective of this section is to understand how Ollama fits into the overall architecture before writing any integration code.

---

## What is Ollama?

Ollama is a local inference engine that allows applications to execute Large Language Models on a local machine.

Its responsibilities include:

- Downloading models.
- Loading models into memory.
- Executing inference.
- Exposing an HTTP API for applications.

Ollama is not the model itself.

Instead, it is capable of running many different models, including:

- Llama 3
- DeepSeek
- Qwen
- Gemma
- Mistral
- Phi

The relationship can be represented as:

Ollama

↓

Llama 3

or

Ollama

↓

DeepSeek

or

Ollama

↓

Qwen

The same Ollama installation can execute different models without changing the application architecture.

---

## Ollama in the System Architecture

Within the project architecture, Ollama belongs to the infrastructure layer.

Application Layer

Agent

↓

Abstraction Layer

LLM

↓

Implementation Layer

OllamaLLM

↓

Infrastructure Layer

Ollama

↓

Model Layer

Llama 3

The Agent never communicates directly with Ollama.

Instead, all communication occurs through an implementation of the LLM interface.

---

## How Ollama Works

Ollama runs as a local HTTP server.

By default, it listens on:

http://localhost:11434

When the application needs an answer, the communication flow is:

Agent

↓

OllamaLLM

↓

HTTP Request

↓

Ollama Server

↓

Model

↓

HTTP Response

↓

OllamaLLM

↓

Agent

The application never communicates directly with the model.

Instead, it sends HTTP requests to the Ollama server, which performs inference and returns the generated response.

---

## Responsibilities of OllamaLLM

The future OllamaLLM implementation will act as an adapter between the application and Ollama.

Its responsibilities include:

- Receiving prompts from the Agent.
- Building HTTP requests.
- Sending requests to Ollama.
- Receiving HTTP responses.
- Extracting the generated text.
- Returning the response through the LLM interface.

The Agent remains completely independent of:

- HTTP communication.
- API endpoints.
- JSON formats.
- Infrastructure details.

This preserves Separation of Concerns and Dependency Inversion.

---

## Ollama vs. LangChain

Ollama and LangChain solve different problems.

### Ollama

Responsible for:

- Running Language Models.
- Executing inference.
- Returning generated text.

### LangChain

Responsible for building LLM-powered applications by providing components such as:

- Prompt templates.
- Conversation memory.
- Tool calling.
- Chains.
- Retrieval (RAG).
- Structured outputs.
- Output parsers.

LangChain does not replace Ollama.

Likewise, Ollama does not replace LangChain.

They operate at different architectural layers.

Typical architecture:

Agent

↓

LangChain

↓

Ollama

↓

Llama 3

However, LangChain is optional.

The current project intentionally integrates Ollama directly before introducing LangChain in order to understand the underlying architecture.

---

## Local Development vs. Production

Ollama is an excellent choice for:

- Local development.
- Learning.
- Prototyping.
- Offline execution.
- Privacy-sensitive workloads.
- On-premises deployments.

Production systems frequently use managed cloud providers such as:

- OpenAI
- Azure OpenAI
- Amazon Bedrock
- Google Vertex AI

Managed providers offer:

- Automatic scaling.
- High availability.
- Managed infrastructure.
- Monitoring.
- Operational simplicity.

Because the project depends only on the LLM abstraction, replacing Ollama with a cloud provider requires only a new implementation of the LLM interface while leaving the Agent unchanged.

---

## Engineering Principles Applied

- Separation of Concerns
- Dependency Injection
- Dependency Inversion Principle
- Single Responsibility Principle
- Encapsulation
- Programming to Abstractions

---

## Key Takeaways

- Ollama is not a Language Model.
- Ollama is a local inference engine.
- Ollama exposes an HTTP API.
- The Agent never communicates directly with Ollama.
- OllamaLLM encapsulates all infrastructure-specific logic.
- LangChain and Ollama have different responsibilities.
- LangChain is optional; Ollama can be integrated directly.
- The project architecture allows providers to be replaced without modifying the Agent.

---

## Summary

The project now has a clear understanding of the role of Ollama within the system architecture.

The Agent remains isolated from infrastructure concerns through the LLM abstraction, while Ollama serves as the local inference engine responsible for executing Language Models.

This architectural foundation prepares the project to integrate the first real LLM while preserving a clean, modular, and extensible software design.

---

## Basic Ollama Commands

During development, four Ollama commands are used most frequently.

### Verify the Installation

```powershell
ollama --version
```

Displays the installed Ollama version and verifies that the CLI is correctly installed.

### List Installed Models

```powershell
ollama list
```

Displays all models currently installed in the local Ollama repository.

### Run a Model

```powershell
ollama run <model-name>
```

Example:

```powershell
ollama run qwen3:4b
```

Starts an interactive conversation with the selected model.

### View Running Models

```powershell
ollama ps
```

Displays the models currently loaded into memory.

These commands are sufficient for most local development workflows.

---

## Reasoning Models vs. General-Purpose Models

Not all Large Language Models behave the same way.

Some models are optimized for fast conversational responses, while others are designed to perform explicit reasoning before generating an answer.

During this phase, the project used **Qwen3:4b**, which is capable of reasoning before responding.

When executing a prompt, the model displayed an intermediate reasoning process:

```
Thinking...

...

...done thinking.
```

This behavior increases response latency but can improve performance on complex reasoning tasks.

Other models, such as Llama 3, generally produce responses immediately without exposing an explicit reasoning phase.

Neither approach is universally better.

The appropriate model depends on the application requirements.

---

## Understanding Local Model Resource Requirements

Choosing a model requires understanding several different resource considerations.

### Number of Parameters

A model described as **4B** contains approximately four billion learned parameters.

The parameter count measures the complexity of the neural network and should not be interpreted as the amount of memory required.

### Quantization

Modern local models are distributed using quantized representations.

Quantization reduces the storage and memory requirements by representing parameters using fewer bits while preserving most of the model's capabilities.

As a result, a 4B model may occupy only a few gigabytes on disk rather than the much larger size required by full-precision representations.

### Disk Usage

The model file is permanently stored on disk after downloading.

Installing multiple models increases the total disk space consumed.

### RAM Usage

When a model is executed, Ollama loads it into memory.

The runtime memory consumption is typically larger than the model file because additional memory is required for inference, context management, and runtime overhead.

### CPU and GPU Execution

Ollama can execute models using either the CPU or a compatible GPU.

GPU execution generally provides significantly faster inference, while CPU execution requires more processing time but allows local execution without dedicated AI hardware.

---

## Choosing a Model as an Engineering Decision

Model selection should always be driven by application requirements rather than by model size alone.

Important considerations include:

- Available hardware.
- Response latency.
- Memory constraints.
- Required reasoning capability.
- Number of concurrent users.
- Deployment cost.

A larger model is not automatically a better engineering choice.

For many applications, a smaller model provides an excellent balance between performance, resource consumption, and response quality.

An AI engineer chooses the model that best satisfies the requirements of the system rather than simply selecting the largest available model.

# 2.3 Create the First Real LLM Adapter

## Objective

The objective of this section was to create the first concrete implementation of the LLM abstraction and connect the application architecture with a real local Large Language Model.

The project moved from a simulated LLM environment using `FakeLLM` to a real inference environment using Ollama and Qwen3.

The main architectural goal was to integrate a real LLM without modifying the Agent logic.

---

# OllamaLLM Adapter

A new module was created:

```
src/ai_agent_system/ollama_llm.py
```

Purpose:

```
Provides a concrete implementation of the LLM interface that communicates
with a locally running Ollama server.
```

The module acts as an adapter between:

- The application architecture.
- The Ollama infrastructure.

The Agent does not know that Ollama exists.

The Agent only depends on the LLM contract.

---

# Adapter Pattern Applied

The project applies the Adapter Pattern to isolate infrastructure-specific communication.

The architecture is:

```
Agent

↓

LLM Interface

↓

OllamaLLM Adapter

↓

Ollama API

↓

Qwen3 Model
```

The Adapter translates the application's generic LLM request into the format required by Ollama.

Responsibilities of `OllamaLLM`:

- Receive prompts from the application.
- Build HTTP requests.
- Communicate with the Ollama server.
- Process the response.
- Return generated text.

The Agent remains independent from:

- HTTP communication.
- API endpoints.
- JSON structures.
- Model providers.

---

# Dependency Injection

The real LLM implementation is injected into the system instead of being created internally.

This preserves the Dependency Inversion Principle.

The Agent depends on:

```
LLM abstraction
```

and not on:

```
OllamaLLM
```

or:

```
Qwen3
```

This allows future replacement of the provider without changing the Agent.

Possible future implementations:

```
LLM
 |
 +-- FakeLLM
 |
 +-- OllamaLLM
 |
 +-- OpenAILLM
 |
 +-- AzureOpenAILLM
 |
 +-- BedrockLLM
```

---

# Integration Testing

A new integration test was created:

```
tests/integration/test_ollama_llm.py
```

Purpose:

```
Validate communication with a real Ollama instance.
```

The test verifies the complete request-response flow:

```
Python Application

↓

OllamaLLM

↓

Ollama Server

↓

Qwen3 Model

↓

Generated Response
```

Unlike unit tests, integration tests validate real infrastructure interaction.

---

# Unit Testing vs Integration Testing

The project now contains two different testing strategies.

## Unit Test

Location:

```
tests/test_agent.py
```

Uses:

```
FakeLLM
```

Purpose:

Validate Agent behavior without external dependencies.

Characteristics:

- Fast.
- Deterministic.
- Independent from infrastructure.

---

## Integration Test

Location:

```
tests/integration/test_ollama_llm.py
```

Uses:

```
OllamaLLM
```

Purpose:

Validate real communication with Ollama and a local model.

Characteristics:

- Requires Ollama running.
- Requires the model to be available.
- Slower than unit tests.

---

# Ollama Model Selection

The project initially considered using larger models such as Llama 3.1.

However, local hardware limitations were considered.

Llama 3.1:

- Larger model size.
- Higher memory requirements.
- Slower inference on CPU.

Qwen3:4b was selected for this phase because:

- Smaller model size.
- Lower resource requirements.
- Enough capability for architecture validation.
- Faster local experimentation.

The objective of this phase was not model performance evaluation.

The objective was validating the software architecture.

---

# Integration Test Optimization

The integration test initially used a longer prompt:

```
Say hello in one sentence.
```

The test execution was slow because the model was running locally using CPU inference.

The prompt was simplified:

```
Hi
```

The purpose of the integration test is not evaluating language quality.

The purpose is only validating:

```
Application → OllamaLLM → Ollama → Model → Response
```

Short prompts make integration tests faster and more reliable.

---

# Validation Pipeline

The complete engineering validation pipeline was executed successfully.

```
Ruff

↓

MyPy

↓

Pytest

↓

Pre-commit
```

Results:

```
Ruff       ✅
MyPy       ✅
Pytest     ✅
Pre-commit ✅
```

---

# Architectural Achievements

After this section, the project achieved:

- First real LLM integration.
- First local inference execution from application code.
- First production-style LLM adapter.
- Separation between application logic and infrastructure.
- Provider-independent architecture.
- Real integration testing strategy.

---

# Key Takeaways

- The Agent should never depend directly on a specific LLM provider.
- Interfaces allow different LLM implementations to coexist.
- Ollama is an infrastructure component, not the model itself.
- `OllamaLLM` isolates communication details from the application.
- Unit tests and integration tests serve different purposes.
- Local models are useful for development and learning.
- Cloud providers can replace Ollama later without modifying the Agent.

---

# Summary

The project successfully integrated its first real Large Language Model through a clean software architecture.

The Agent remains independent from infrastructure concerns while `OllamaLLM` provides the connection between the application and the local Ollama runtime.

This architectural foundation prepares the project for the next step: introducing LangChain while preserving the existing architecture and design principles.


# Phase 2.4 — Introduce LangChain

## Objective

Integrate LangChain into the AI Agent System while maintaining the existing software architecture principles.

The goal is not to make the Agent depend directly on LangChain, but to use LangChain as an external framework that simplifies interaction with language models.

---

## Previous Architecture (Before LangChain)

Before introducing LangChain, the project communicated directly with Ollama through HTTP requests.

```
Agent
  ↓
LLM Interface
  ↓
OllamaLLM Adapter
  ↓
Ollama API
  ↓
Qwen3 Model
```

The `OllamaLLM` adapter was responsible for:

- Building the HTTP request.
- Sending the request to Ollama.
- Parsing the response.
- Returning the generated text.

This approach works, but it requires implementing and maintaining provider-specific communication logic.

---

## Why Introduce LangChain?

LangChain provides abstractions and integrations for working with different language model providers.

It allows the project to:

- Use standardized LLM interfaces.
- Switch between providers more easily.
- Avoid implementing low-level API communication.
- Prepare the system for more advanced agent workflows.

Examples of possible future integrations:

- Ollama (local models).
- OpenAI models.
- Google Gemini.
- Anthropic Claude.
- Other LangChain-compatible providers.

---

## New Architecture with LangChain

After introducing LangChain:

```
Agent
  ↓
LLM Interface
  ↓
OllamaLLM Adapter
  ↓
LangChain Ollama Model
  ↓
Ollama API
  ↓
Qwen3 Model
```

The Agent architecture remains unchanged.

The Agent still depends only on the internal `LLM` interface.

LangChain is isolated behind the adapter layer.

---

## Implementation

A new dependency was added:

```
langchain
langchain-ollama
```

The project now uses:

```
src/ai_agent_system/ollama_llm.py
```

as an adapter between the internal architecture and LangChain.

Responsibilities:

- Receive a LangChain Ollama model.
- Expose the internal `LLM` interface.
- Translate application requests into LangChain calls.

---

## Important Design Principle

The Agent does not know that LangChain exists.

The dependency direction is:

```
Application Layer
        ↓
Internal Abstraction
        ↓
External Framework Adapter
        ↓
External Service
```

This follows the Dependency Inversion Principle:

High-level components should depend on abstractions, not concrete implementations.

---

# Phase 2.5 — Dependency Injection and Adapter Pattern

## Objective

Improve the architecture by separating object creation from object usage.

The goal is to make components easier to replace, test, and extend.

---

## Problem Before Refactoring

Initially, `OllamaLLM` created its own LangChain dependency.

Example:

```
OllamaLLM
    |
    └── creates LangChain Ollama model
```

This created two responsibilities:

1. Creating the LangChain model.
2. Using the LangChain model.

A class should ideally have one clear responsibility.

---

## Refactored Design

After applying Dependency Injection:

```
Application
    |
    | creates
    ↓
LangChain Ollama Model
    |
    | injects
    ↓
OllamaLLM Adapter
    |
    ↓
LLM Interface
    |
    ↓
Agent
```

Now:

- The application creates dependencies.
- The adapter uses the dependency.
- The Agent only consumes the abstraction.

---

## Dependency Injection Concept

Dependency Injection means that an object receives the dependencies it needs from outside instead of creating them internally.

Before:

```
Class
 |
 └── creates dependency
```

After:

```
External component
 |
 └── provides dependency
        |
        ↓
      Class
```

Benefits:

- Easier testing.
- Lower coupling.
- Easier replacement of implementations.
- Better maintainability.

---

## Composition Root

The place where dependencies are created and connected is called the Composition Root.

Currently:

```
examples/agent_demo.py
```

acts as the composition root.

It creates:

- LangChain Ollama model.
- OllamaLLM adapter.
- Agent.

Example flow:

```
agent_demo.py

creates LangChain model

        ↓

creates OllamaLLM adapter

        ↓

creates Agent

        ↓

executes request
```

Later, this responsibility can move to a dedicated application factory or dependency container.

---

## Current Architecture After Phase 2.5

```
examples/agent_demo.py
        |
        ↓
LangChain Ollama Model
        |
        ↓
OllamaLLM Adapter
        |
        ↓
LLM Interface
        |
        ↓
Agent
        |
        ↓
User Request
```

---

## Key Lessons Learned

### 1. Abstractions protect the system from change

The Agent depends on the `LLM` contract, not on Ollama or LangChain.

---

### 2. Frameworks should stay at the edges

LangChain is useful, but it should not dominate the internal architecture.

---

### 3. Adapters isolate external technologies

`OllamaLLM` translates between:

- Internal application design.
- LangChain implementation details.

---

### 4. Dependency Injection improves flexibility

Dependencies are provided from outside, allowing components to be replaced without modifying the core system.

---

## Validation

The following tests were executed successfully:

```
pytest tests/integration/test_ollama_llm.py -v

1 passed
```

and:

```
pre-commit run --all-files

ruff      Passed
mypy      Passed
pytest    Passed
```

The system successfully generates responses using:

```
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
LangChain Ollama
 ↓
Qwen3 Model
```
# Phase 2.4 — Introduce LangChain

## Objective

Integrate LangChain into the AI Agent System while maintaining the existing software architecture principles.

The goal is not to make the Agent depend directly on LangChain, but to use LangChain as an external framework that simplifies interaction with language models.

---

## Previous Architecture (Before LangChain)

Before introducing LangChain, the project communicated directly with Ollama through HTTP requests.

```text
Agent
  ↓
LLM Interface
  ↓
OllamaLLM Adapter
  ↓
Ollama API
  ↓
Qwen3 Model
```

The `OllamaLLM` adapter was responsible for:

- Building the HTTP request.
- Sending the request to Ollama.
- Parsing the response.
- Returning the generated text.

This approach works, but it requires implementing and maintaining provider-specific communication logic.

---

## Why Introduce LangChain?

LangChain provides abstractions and integrations for working with different language model providers.

It allows the project to:

- Use standardized LLM interfaces.
- Switch between providers more easily.
- Avoid implementing low-level API communication.
- Prepare the system for more advanced agent workflows.

Examples of possible future integrations:

- Ollama (local models).
- OpenAI models.
- Google Gemini.
- Anthropic Claude.
- Other LangChain-compatible providers.

---

## New Architecture with LangChain

After introducing LangChain:

```text
Agent
  ↓
LLM Interface
  ↓
OllamaLLM Adapter
  ↓
LangChain Ollama Model
  ↓
Ollama API
  ↓
Qwen3 Model
```

The Agent architecture remains unchanged.

The Agent still depends only on the internal `LLM` interface.

LangChain is isolated behind the adapter layer.

---

## Implementation

A new dependency was added:

```text
langchain
langchain-ollama
```

The project now uses:

```text
src/ai_agent_system/ollama_llm.py
```

as an adapter between the internal architecture and LangChain.

Responsibilities:

- Receive a LangChain Ollama model.
- Expose the internal `LLM` interface.
- Translate application requests into LangChain calls.

---

## Important Design Principle

The Agent does not know that LangChain exists.

The dependency direction is:

```text
Application Layer
        ↓
Internal Abstraction
        ↓
External Framework Adapter
        ↓
External Service
```

This follows the Dependency Inversion Principle:

High-level components should depend on abstractions, not concrete implementations.

---

# Phase 2.5 — Dependency Injection and Adapter Pattern

## Objective

Improve the architecture by separating object creation from object usage.

The goal is to make components easier to replace, test, and extend.

---

## Problem Before Refactoring

Initially, `OllamaLLM` created its own LangChain dependency.

Example:

```text
OllamaLLM
    |
    └── creates LangChain Ollama model
```

This created two responsibilities:

1. Creating the LangChain model.
2. Using the LangChain model.

A class should ideally have one clear responsibility.

---

## Refactored Design

After applying Dependency Injection:

```text
Application
    |
    | creates
    ↓
LangChain Ollama Model
    |
    | injects
    ↓
OllamaLLM Adapter
    |
    ↓
LLM Interface
    |
    ↓
Agent
```

Now:

- The application creates dependencies.
- The adapter uses the dependency.
- The Agent only consumes the abstraction.

---

## Dependency Injection Concept

Dependency Injection means that an object receives the dependencies it needs from outside instead of creating them internally.

Before:

```text
Class
 |
 └── creates dependency
```

After:

```text
External component
 |
 └── provides dependency
        |
        ↓
      Class
```

Benefits:

- Easier testing.
- Lower coupling.
- Easier replacement of implementations.
- Better maintainability.

---

## Composition Root

The place where dependencies are created and connected is called the Composition Root.

Currently:

```text
examples/agent_demo.py
```

acts as the composition root.

It creates:

- LangChain Ollama model.
- OllamaLLM adapter.
- Agent.

Example flow:

```text
agent_demo.py

creates LangChain model

        ↓

creates OllamaLLM adapter

        ↓

creates Agent

        ↓

executes request
```

Later, this responsibility can move to a dedicated application factory or dependency container.

---

## Current Architecture After Phase 2.5

```text
examples/agent_demo.py
        |
        ↓
LangChain Ollama Model
        |
        ↓
OllamaLLM Adapter
        |
        ↓
LLM Interface
        |
        ↓
Agent
        |
        ↓
User Request
```

---

## Key Lessons Learned

### 1. Abstractions protect the system from change

The Agent depends on the `LLM` contract, not on Ollama or LangChain.

---

### 2. Frameworks should stay at the edges

LangChain is useful, but it should not dominate the internal architecture.

---

### 3. Adapters isolate external technologies

`OllamaLLM` translates between:

- Internal application design.
- LangChain implementation details.

---

### 4. Dependency Injection improves flexibility

Dependencies are provided from outside, allowing components to be replaced without modifying the core system.

---

## Validation

The following tests were executed successfully:

```text
pytest tests/integration/test_ollama_llm.py -v

1 passed
```

and:

```text
pre-commit run --all-files

ruff      Passed
mypy      Passed
pytest    Passed
```

The system successfully generates responses using:

```text
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
LangChain Ollama
 ↓
Qwen3 Model
```

# Phase 2.4 — Introduce LangChain

## Objective

Integrate LangChain into the AI Agent System while maintaining the existing software architecture principles.

The goal is not to make the Agent depend directly on LangChain, but to use LangChain as an external framework that simplifies interaction with language models.

---

## Previous Architecture (Before LangChain)

Before introducing LangChain, the project communicated directly with Ollama through HTTP requests.

```
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
Ollama API
 ↓
Qwen3 Model
```

The `OllamaLLM` adapter was responsible for:

- Building HTTP requests.
- Sending requests to Ollama.
- Parsing responses.
- Returning generated text.

This approach works, but it requires implementing and maintaining provider-specific communication logic.

---

## Why Introduce LangChain?

LangChain provides abstractions and integrations for working with different language model providers.

It allows the project to:

- Use standardized LLM interfaces.
- Switch between providers more easily.
- Avoid implementing low-level API communication.
- Prepare the system for more advanced agent workflows.

Possible future integrations:

- Ollama local models.
- OpenAI models.
- Google Gemini.
- Anthropic Claude.
- Other LangChain-compatible providers.

---

## New Architecture with LangChain

After introducing LangChain:

```
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
LangChain Ollama Model
 ↓
Ollama API
 ↓
Qwen3 Model
```

The Agent architecture remains unchanged.

The Agent still depends only on the internal `LLM` interface.

LangChain is isolated behind the adapter layer.

---

## Implementation

New dependencies were added:

```
langchain
langchain-ollama
```

The project now uses:

```
src/ai_agent_system/ollama_llm.py
```

as an adapter between the internal architecture and LangChain.

Responsibilities:

- Receive a LangChain Ollama model.
- Expose the internal `LLM` interface.
- Translate application requests into LangChain calls.

---

## Important Design Principle

The Agent does not know that LangChain exists.

The dependency direction is:

```
Application Layer
        ↓
Internal Abstraction
        ↓
External Framework Adapter
        ↓
External Service
```

This follows the Dependency Inversion Principle:

High-level components should depend on abstractions, not concrete implementations.

---

# Phase 2.5 — Dependency Injection and Adapter Pattern

## Objective

Improve the architecture by separating object creation from object usage.

The goal is to make components easier to replace, test, and extend.

---

## Problem Before Refactoring

Initially, `OllamaLLM` created its own LangChain dependency.

Example:

```
OllamaLLM
    |
    └── creates LangChain Ollama model
```

This created two responsibilities:

1. Creating the LangChain model.
2. Using the LangChain model.

A class should ideally have one clear responsibility.

---

## Refactored Design

After applying Dependency Injection:

```
Application
    |
    | creates
    ↓
LangChain Ollama Model
    |
    | injects
    ↓
OllamaLLM Adapter
    |
    ↓
LLM Interface
    |
    ↓
Agent
```

Now:

- The application creates dependencies.
- The adapter uses the dependency.
- The Agent only consumes the abstraction.

---

## Dependency Injection Concept

Dependency Injection means that an object receives the dependencies it needs from outside instead of creating them internally.

Before:

```
Class
 |
 └── creates dependency
```

After:

```
External component
 |
 └── provides dependency
        |
        ↓
      Class
```

Benefits:

- Easier testing.
- Lower coupling.
- Easier replacement of implementations.
- Better maintainability.

---

## Composition Root

The place where dependencies are created and connected is called the Composition Root.

Currently:

```
examples/agent_demo.py
```

acts as the composition root.

It creates:

- LangChain Ollama model.
- OllamaLLM adapter.
- Agent.

Example flow:

```
agent_demo.py

creates LangChain model

        ↓

creates OllamaLLM adapter

        ↓

creates Agent

        ↓

executes request
```

Later, this responsibility can move to a dedicated application factory or dependency container.

---

## Current Architecture After Phase 2.5

```
examples/agent_demo.py
        |
        ↓
LangChain Ollama Model
        |
        ↓
OllamaLLM Adapter
        |
        ↓
LLM Interface
        |
        ↓
Agent
        |
        ↓
User Request
```

---

## Key Lessons Learned

### 1. Abstractions protect the system from change

The Agent depends on the `LLM` contract, not on Ollama or LangChain.

---

### 2. Frameworks should stay at the edges

LangChain is useful, but it should not dominate the internal architecture.

---

### 3. Adapters isolate external technologies

`OllamaLLM` translates between:

- Internal application design.
- LangChain implementation details.

---

### 4. Dependency Injection improves flexibility

Dependencies are provided from outside, allowing components to be replaced without modifying the core system.

---

## Validation

The following tests were executed successfully:

```
pytest tests/integration/test_ollama_llm.py -v

1 passed
```

and:

```
pre-commit run --all-files

ruff      Passed
mypy      Passed
pytest    Passed
```

The system successfully generates responses using:

```
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
LangChain Ollama
 ↓
Qwen3 Model
```

# Phase 2.6 — Introduce LangChain Message Model

## Objective

Explore LangChain's message-based communication model and understand why modern AI Agent systems use structured messages instead of simple text prompts.

The goal of this phase was not to modify the Agent architecture yet, but to experimentally evaluate the difference between:

- Simple string-based LLM interaction.
- Structured message-based interaction.

---

## Previous Approach

Before this phase, the project communicated with the language model using a simple string prompt.

The architecture was:

```
Agent
 ↓
LLM Interface
 ↓
OllamaLLM Adapter
 ↓
Ollama Model
 ↓
Text Response
```

The communication contract was:

```
Input:

str


Output:

str
```

This approach is enough for simple interactions, but it does not naturally represent:

- System instructions.
- Conversation history.
- Different message roles.
- Tool interactions.

---

# LangChain Message Model

LangChain introduces a structured message abstraction for conversational AI systems.

Instead of sending only raw text, applications can represent interactions using different message types.

Main message types:

```
SystemMessage
      |
      ↓
HumanMessage
      |
      ↓
AIMessage
```

Each message has a specific role:

## SystemMessage

Defines the behavior and instructions for the model.

Example:

```
You are a concise AI assistant.
```

---

## HumanMessage

Represents the user's request.

Example:

```
Explain machine learning.
```

---

## AIMessage

Represents the model's generated response.

Example:

```
Machine learning is a field of AI...
```

---

# Experiment Implementation

A new educational example was created:

```
examples/langchain_messages_demo.py
```

The purpose of this file was to compare two interaction styles:

1. Simple string invocation.
2. Structured message invocation.

---

# Experiment 1 — String Prompt

The first experiment used:

```
"Introduce yourself in one sentence."
```

The flow was:

```
String Prompt
      |
      ↓
ChatOllama
      |
      ↓
Qwen3 Model
      |
      ↓
AIMessage
```

LangChain automatically converts the string into an internal message representation.

---

# Experiment 2 — Structured Messages

The second experiment explicitly created messages:

```
SystemMessage
        |
        ↓
HumanMessage
        |
        ↓
ChatOllama
        |
        ↓
Qwen3 Model
        |
        ↓
AIMessage
```

The model received:

```
System:
You are a concise AI assistant.

Human:
Introduce yourself in one sentence.
```

The response was generated successfully.

---

# Important Discovery

During the experiment, an important distinction was identified between LangChain model abstractions.

## OllamaLLM

The `OllamaLLM` class represents a traditional text completion model.

Behavior:

```
Input:

str


Output:

str
```

Example:

```
prompt
 ↓
OllamaLLM
 ↓
text response
```

---

## ChatOllama

The `ChatOllama` class represents a conversational model.

Behavior:

```
Input:

list[Message]


Output:

AIMessage
```

Example:

```
Messages
 ↓
ChatOllama
 ↓
AIMessage
```

The response can be accessed through:

```
response.content
```

---

# Architectural Implications

The experiment demonstrated that Agent systems usually require message-based communication.

Simple text prompts are limited because they cannot naturally represent:

- Previous conversation turns.
- Agent instructions.
- User roles.
- Assistant responses.
- Tool execution messages.

A more realistic Agent architecture requires structured communication.

---

# Evolution of the Architecture

Current architecture:

```
Agent
 |
 ↓
LLM Interface
 |
 ↓
OllamaLLM Adapter
 |
 ↓
Text Completion Model
 |
 ↓
String Response
```

Future architecture:

```
Agent
 |
 ↓
Chat Model Interface
 |
 ↓
ChatOllama Adapter
 |
 ↓
Chat Model
 |
 ↓
AIMessage Response
```

---

# Key Lessons Learned

## 1. LLMs and Chat Models are different abstractions

A traditional LLM interface focuses on text completion.

A chat model interface focuses on conversations using structured messages.

---

## 2. Messages provide context and roles

Structured messages allow the system to distinguish between:

- Instructions.
- User requests.
- Previous assistant responses.

---

## 3. Agent systems require richer communication

Future capabilities such as:

- Memory.
- Planning.
- Tool usage.
- Multi-step reasoning.

depend on message-based architectures.

---

## 4. Framework abstractions must be understood before adoption

Before changing the architecture, the project validated LangChain's behavior experimentally.

This avoids blindly adopting framework features without understanding their impact.

---

# Validation

The experiment was executed successfully:

```
python examples/langchain_messages_demo.py
```

Output:

```
=== Experiment 1: Simple String Prompt ===

Qwen response generated successfully.


=== Experiment 2: Structured Messages ===

Qwen response generated successfully.
```

The experiment confirmed that LangChain supports both:

```
Simple text invocation
```

and:

```
Structured message invocation
```

# Phase 2.7 — Migrate from LLM Interface to Chat Model Interface

## Objective

Replace the initial LLM abstraction based on simple string prompts with a Chat Model abstraction based on structured conversational messages.

The objective was to move the architecture closer to modern AI Agent systems, where models operate using:

- System messages.
- Human messages.
- AI responses.
- Conversation history.
- Future tool interactions.

---

# Previous Architecture

The initial implementation used a simple LLM interface:

```
Agent

 ↓

LLM Interface

 ↓

OllamaLLM Adapter

 ↓

LangChain Ollama LLM

 ↓

Qwen3 Model
```

The Agent sent a string prompt and received a string response.

Although this approach was useful for understanding basic model invocation, it had limitations:

- No native conversation structure.
- No distinction between user and assistant roles.
- No system instructions.
- Difficult extension toward memory and tools.
- Limited support for modern agent workflows.

---

# New Architecture

The system was migrated to a Chat Model architecture:

```
Agent

 ↓

ChatModel Interface

 ↓

OllamaChat Adapter

 ↓

LangChain ChatOllama

 ↓

Qwen3 Model
```

The Agent now works with structured messages instead of plain text prompts.

---

# New Components

## ChatModel Interface

Created:

```
src/ai_agent_system/chat_model.py
```

Purpose:

Define the abstraction that any conversational model must satisfy.

Responsibilities:

- Receive a list of messages.
- Send messages to a conversational model.
- Return an AI response message.

The Agent depends only on this abstraction.

The Agent does not know:

- LangChain.
- Ollama.
- Specific model providers.

---

## OllamaChat Adapter

Created:

```
src/ai_agent_system/ollama_chat.py
```

Purpose:

Provide a concrete implementation of the ChatModel interface using LangChain ChatOllama.

Responsibilities:

- Initialize the Ollama chat model.
- Communicate with the Ollama server.
- Return generated AI messages.

Architecture:

```
Application Layer

 ↓

OllamaChat Adapter

 ↓

LangChain ChatOllama

 ↓

Ollama Server

 ↓

Qwen3 Model
```

---

# Agent Migration

Updated:

```
src/ai_agent_system/agent.py
```

Before:

```
Agent

 ↓

Creates HumanMessage

 ↓

Calls Model
```

After:

```
Agent

 ↓

ChatModel

 ↓

Receives AIMessage
```

The Agent became independent of:

- LangChain message classes.
- Ollama implementation details.
- Specific model providers.

---

# Testing Changes

Updated:

```
tests/test_agent.py
```

The previous fake LLM implementation was replaced with:

```
FakeChatModel
```

The unit test validates:

```
Agent

 ↓

ChatModel

 ↓

Response
```

The test remains independent from:

- Ollama.
- External APIs.
- Network calls.

---

Created:

```
tests/integration/test_ollama_chat.py
```

Purpose:

Validate the real integration:

```
OllamaChat

 ↓

ChatOllama

 ↓

Ollama Server

 ↓

Qwen3 Model
```

---

# Demo Migration

Updated:

```
examples/agent_demo.py
```

The demo migrated from:

```
OllamaLLM
```

to:

```
OllamaChat
```

The example now represents the intended production architecture.

---

# Cleanup

Removed obsolete components:

```
src/ai_agent_system/llm.py

src/ai_agent_system/ollama_llm.py

tests/integration/test_ollama_llm.py
```

---

# Validation

The migration was validated using:

```
pre-commit run --all-files

ruff      Passed
mypy      Passed
pytest    Passed
```

---

# Key Learning

Modern AI Agents should not depend directly on a specific model provider.

The correct architecture is:

```
Agent

 ↓

Abstract Chat Model

 ↓

Provider Adapter

 ↓

Specific Model Provider
```

This design allows replacing providers without modifying the Agent.

Examples:

```
Ollama

OpenAI

Anthropic

Gemini

Azure OpenAI

AWS Bedrock
```

---

# Phase 2.8 — Introduce Prompt Templates

## Objective

Separate prompt creation from Agent logic.

The goal was to prevent the Agent from being responsible for:

- Creating messages.
- Defining prompt structure.
- Managing prompt formatting.

Prompt design becomes an independent component.

---

# Previous Architecture

Before this phase:

```
User Request

 ↓

Agent

 ↓

HumanMessage Creation

 ↓

ChatModel

 ↓

Response
```

The Agent had too many responsibilities:

- Receive user input.
- Build messages.
- Define prompt structure.
- Call the model.
- Return the response.

---

# New Architecture

After introducing Prompt Templates:

```
User Request

 ↓

Agent

 ↓

PromptTemplate

 ↓

Messages

 ↓

ChatModel

 ↓

OllamaChat

 ↓

Qwen3 Model
```

The Agent became an orchestrator instead of a prompt builder.

---

# New Components

## PromptTemplate Interface

Created:

```
src/ai_agent_system/prompt.py
```

Purpose:

Define the contract for prompt generation.

Responsibilities:

- Receive application variables.
- Generate model-ready messages.
- Keep prompt logic independent from the Agent.

---

## LangChainPrompt Adapter

Created:

```
src/ai_agent_system/langchain_prompt.py
```

Purpose:

Provide a LangChain implementation of the PromptTemplate interface.

Responsibilities:

- Wrap LangChain ChatPromptTemplate.
- Create system and human messages.
- Hide LangChain prompt details from the Agent.

Architecture:

```
PromptTemplate

 ↓

LangChainPrompt

 ↓

ChatPromptTemplate

 ↓

Messages
```

---

# Agent Refactoring

Updated:

```
src/ai_agent_system/agent.py
```

The Agent now receives:

```
PromptTemplate

+

ChatModel
```

Responsibilities:

- Receive user input.
- Request messages from PromptTemplate.
- Send messages to ChatModel.
- Return generated response.

The Agent no longer creates messages directly.

## Phase 2.9 — Conversation State & Memory

### Objective

The objective of this phase was to introduce the first memory capability into the Agent architecture by adding conversation state management.

Until this point, the Agent was stateless:

```
User Request

 ↓

Agent

 ↓

PromptTemplate

 ↓

ChatModel

 ↓

Response
```

Each interaction was independent. The system had no knowledge of previous messages.

Example:

```
User:
My name is Alvaro.

Assistant:
Nice to meet you, Alvaro.

User:
What is my name?

Assistant:
I don't know.
```

The Agent could generate responses but could not maintain context.

---

## Conversation State Abstraction

A new responsibility was introduced:

```
Conversation State

        ↓

Message History

        ↓

Prompt Construction

        ↓

ChatModel
```

The purpose of the Conversation abstraction is to store and manage messages independently from the Agent logic.

The Conversation component is responsible for:

- Storing messages.
- Maintaining conversation history.
- Providing previous messages to the Agent.
- Keeping memory logic separated from reasoning logic.

---

## New Architecture

The Agent architecture evolved from a stateless flow:

```
User Request

 ↓

Agent

 ↓

PromptTemplate

 ↓

ChatModel

 ↓

Response
```

into a stateful conversation workflow:

```
User Request

 ↓

Agent

 ↓

Conversation State

 ↓

Message History

 ↓

PromptTemplate

 ↓

ChatModel

 ↓

Response

 ↓

Update Conversation State
```

The Agent now manages a conversation instead of isolated questions.

---

## Important Design Principle

The Agent should not directly implement memory storage logic.

Bad design:

```
Agent

 ├── Prompt logic

 ├── Model logic

 └── Memory logic
```

This would make the Agent responsible for too many concerns.

The improved design follows the Single Responsibility Principle:

```
Agent

 ↓

Conversation

 ↓

PromptTemplate

 ↓

ChatModel
```

Each component has a clear responsibility:

- Agent → coordinates the workflow.
- Conversation → manages message history.
- PromptTemplate → builds model instructions.
- ChatModel → generates responses.

---

# Implementation

## Conversation Module

Created:

```
src/ai_agent_system/conversation.py
```

The Conversation class provides:

- Message storage.
- Message retrieval.
- State isolation.

The class does not generate responses and does not know about any LLM provider.

---

## Agent Integration

The Agent was updated to receive Conversation as a dependency.

Before:

```
Agent

 ↓

ChatModel

 ↓

Response
```

After:

```
Agent

 ↓

Conversation

 ↓

ChatModel

 ↓

Response
```

The Agent workflow is now:

1. Receive user input.
2. Convert input into a HumanMessage.
3. Store the message in Conversation.
4. Send the complete message history to ChatModel.
5. Receive AIMessage response.
6. Store the AIMessage in Conversation.
7. Return the generated response.

---

## Testing Strategy

New tests validate that:

- Conversation stores messages correctly.
- Agent updates conversation state.
- User messages are preserved.
- Assistant responses are preserved.
- Previous messages are available for future interactions.

The real model is not used during unit testing.

A FakeChatModel is used to verify Agent behavior independently.

---

## Stateful Conversation Validation

The architecture was validated using a memory-aware test scenario:

```
User:
My name is Alvaro.

 ↓

Conversation State

 ↓

User:
What is my name?

 ↓

ChatModel receives previous history

 ↓

Assistant:
Your name is Alvaro.
```

This confirms that message history is correctly maintained and provided to the model.

---

## Validation

The following checks were executed successfully:

```
pre-commit run --all-files

ruff      Passed
mypy      Passed
pytest    Passed
```

The complete test suite passed after introducing Conversation State.

---

## Phase 2.9 Result

Phase 2.9 successfully introduced the first memory capability into the Agent system.

The architecture now supports:

- Stateful conversations.
- Message history management.
- Separation of memory from reasoning.
- Future integration with advanced memory systems.

This prepares the project for:

- Tool calling.
- Planning workflows.
- Retrieval-Augmented Generation (RAG).
- LangGraph-style agent workflows.
- More autonomous AI systems.