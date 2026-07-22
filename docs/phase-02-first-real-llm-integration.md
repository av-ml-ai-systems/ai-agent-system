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
```