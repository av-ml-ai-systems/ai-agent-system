# Phase 1 — Software Engineering Foundation

## Objective

(Build this section later as we progress through the phase.)

## Architectural Decisions

### Why `src/` and a Package?

The project uses the `src` layout to separate importable application code from the rest of the repository (documentation, tests, configuration, editor settings, etc.).

Inside `src`, the `ai_agent_system` package groups all modules related to the application. This provides a clear namespace, improves maintainability, and supports software engineering principles such as Separation of Concerns and High Cohesion.

The `__init__.py` file explicitly marks the directory as a Python package. Although modern Python does not always require it, professional projects commonly include it because it makes the package structure explicit and can later define the package's public API when needed.

### Central Object of the Application

The core of the project is the **Agent**, not the user interface or the execution script.

Following object-oriented design, the application's main responsibility is represented by an `Agent` class located in `agent.py`.

The future `main.py` (or another entry point) will only be responsible for starting the application and creating the `Agent` object.

This follows the **Single Responsibility Principle (SRP)** by separating application startup from the agent's behavior.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Object-Oriented Design (OOD)
- KISS (Keep It Simple, Stupid)

### Responsibility-Driven Software Design

One of the fundamental ideas in software engineering is to organize a system according to responsibilities rather than convenience.

This principle applies at every architectural level:

- Repository → separates source code, tests, documentation, and configuration.
- Package → groups related modules.
- Module → contains a single responsibility.
- Class → models one primary concept or behavior.
- Method → performs one well-defined task.

As the AI Agent System grows, each new component should have a clear and focused responsibility. This improves readability, maintainability, and scalability.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Separation of Concerns
- High Cohesion
- Low Coupling
- Object-Oriented Design (OOD)
- KISS (Keep It Simple, Stupid)

### The Minimum Responsibilities of an AI Agent

An AI Agent is defined by its behavior, not by the technologies used to implement it.

For this educational project, the minimum responsibilities of an Agent are:

1. Receive a user request.
2. Reason about the request.
3. Decide how to respond.
4. Produce a response.

Components such as memory, tools, user interfaces, APIs, and autonomous workflows are valuable extensions, but they are not part of the minimum definition of an AI Agent.

By identifying the essential responsibilities first, we can build the system incrementally while keeping the architecture simple and understandable.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Separation of Concerns
- First-Principles Thinking
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It Yet)

### The Agent Collaborates with an LLM

The Agent is responsible for coordinating the execution of a task, but it is **not** responsible for generating the response itself.

Reasoning is delegated to a Language Model (LLM), which acts as the reasoning engine of the system.

This separation of responsibilities allows the Agent to focus on orchestration while the LLM focuses on natural language understanding and generation.

This design follows the principle of **composition over inheritance**:

- The Agent **has** an LLM.
- The Agent is **not** an LLM.

Using composition makes the architecture more flexible because the underlying LLM can be replaced (for example, Ollama, OpenAI, or Anthropic) without changing the Agent's primary responsibility.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Composition over Inheritance
- Object-Oriented Design (OOD)
- Dependency Management through Collaboration

### Objects Represent Responsibilities

In Object-Oriented Design, classes are not created simply because the programming language supports them. They are created to model meaningful concepts within the problem domain.

An object is a software representation of a concept that has one or more well-defined responsibilities.

For the AI Agent System, the first important concepts are:

- Agent
- LLM

Later, additional concepts such as Tools, Memory, and Prompt Templates will become objects only when they acquire their own clear responsibilities.

This approach helps avoid unnecessary classes and keeps the architecture simple and maintainable.

**Software Engineering Principles Applied**

- Object-Oriented Design (OOD)
- Single Responsibility Principle (SRP)
- High Cohesion
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It Yet)

### Designing the First Agent Class

Before implementing the `Agent` class, we identified its responsibilities and separated them into **state** and **behavior**.

**State (what the Agent knows):**

- An LLM instance.

**Behavior (what the Agent does):**

- Receive a user request.
- Delegate reasoning to the LLM.
- Return the generated response.

At this stage of the project, the Agent intentionally does **not** include memory, tools, planning, or autonomous workflows. These capabilities will be added incrementally as the architecture evolves.

Keeping the first version of the Agent small follows the project's educational philosophy: understand the minimum viable architecture before introducing additional complexity.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Object-Oriented Design (OOD)
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It Yet)
- Separation of Concerns

### Why the Agent Receives an LLM Instead of Creating It

The `Agent` should not be responsible for creating the Language Model (LLM). Instead, the LLM is created elsewhere and passed to the `Agent`.

This design keeps responsibilities separated:

- The `Agent` is responsible for coordinating the interaction.
- The LLM is responsible for reasoning and generating responses.

By receiving the LLM as a collaborator, the `Agent` becomes independent of a specific implementation. In the future, the same `Agent` could work with different LLM providers (such as Ollama or OpenAI) without changing its own code.

This approach also improves testability because a test can provide a mock or fake LLM without modifying the `Agent`.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Separation of Concerns
- Composition over Inheritance
- Low Coupling
- Dependency Injection (conceptual introduction)

## Understanding the Agent's Architecture

Before implementing the first `Agent` class, we answered several fundamental architectural questions. These questions define the purpose and responsibilities of the Agent before writing any code.

### What is an Agent?

An Agent is the central component of the application. Its purpose is to coordinate the execution of a user's request in order to achieve a goal.

An Agent is **not** the Language Model (LLM), the user interface, or a collection of tools. Instead, it orchestrates the interaction between those components.

For this educational project, the Agent is the core object of the system and represents the application's primary responsibility.

---

### What are the Agent's responsibilities?

The Agent has a single high-level responsibility:

> Coordinate the process of answering a user's request.

To accomplish this, the Agent is responsible for:

1. Receiving a user request.
2. Delegating reasoning to the LLM.
3. Coordinating any required collaborators (such as tools or memory in future phases).
4. Returning the final response to the user.

The Agent is intentionally **not** responsible for configuration, logging, API management, or creating other components.

---

### What does the Agent know?

In Object-Oriented Programming, every object has **state** (what it knows) and **behavior** (what it does).

At this stage of the project, the Agent only knows one thing:

- An LLM instance.

The Agent does **not** permanently store user questions, conversation history, tools, or memory because those concepts have not yet been introduced into the architecture.

Keeping the Agent's state small makes the class easier to understand, test, and maintain.

---

### What does the Agent do?

The Agent performs a simple workflow:

1. Receive a user's request.
2. Send the request to the LLM.
3. Receive the generated response.
4. Return the response to the caller.

This is the minimum behavior required for an educational AI Agent.

More advanced capabilities, such as tool usage, memory, planning, and autonomous reasoning, will be added gradually in later phases.

---

### Why does the Agent collaborate with an LLM?

The Agent and the LLM have different responsibilities.

The LLM is responsible for reasoning and generating natural language responses.

The Agent is responsible for coordinating the overall workflow.

Instead of performing the reasoning itself, the Agent delegates that responsibility to the LLM.

This separation of responsibilities keeps the architecture modular and follows the Single Responsibility Principle (SRP).

---

### Why shouldn't the Agent create the LLM itself?

Creating an LLM is a different responsibility from coordinating the workflow.

If the Agent created the LLM internally, it would become tightly coupled to a specific implementation (for example, Ollama).

Instead, the LLM is created elsewhere and provided to the Agent.

This design offers several advantages:

- The Agent remains independent of a specific LLM provider.
- Different LLMs (Ollama, OpenAI, Anthropic, etc.) can be used without modifying the Agent.
- Testing becomes easier because a mock or fake LLM can be provided during unit tests.
- The Agent focuses only on its primary responsibility: orchestration.

This is an early introduction to the concept of **Dependency Injection**, where objects receive the collaborators they need instead of creating them themselves.

---

## Software Engineering Principles Applied

- Object-Oriented Design (OOD)
- Single Responsibility Principle (SRP)
- Separation of Concerns
- High Cohesion
- Low Coupling
- Composition over Inheritance
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It Yet)
- Dependency Injection (conceptual introduction)

### Designing the Constructor (`__init__`)

Every object must begin its life in a valid state. In Python, this is the responsibility of the `__init__()` method, also known as the constructor.

The constructor is responsible for initializing the object's state, not for executing the object's main behavior.

For the educational AI Agent, the only required dependency at creation time is the LLM.

Therefore, the constructor will receive an LLM instance and store it as part of the Agent's state.

Thinking about constructors in terms of establishing a valid initial state leads to clearer and more maintainable object-oriented designs.

**Software Engineering Principles Applied**

- Object-Oriented Design (OOD)
- Single Responsibility Principle (SRP)
- High Cohesion
- KISS (Keep It Simple, Stupid)
- Dependency Injection (conceptual introduction)

### Architectural Insight

A constructor should not ask:

> "What variables should I create?"

Instead, it should ask:

> "What information does this object absolutely need in order to exist in a valid state?"

When the constructor is designed from responsibilities rather than implementation details, the resulting class is usually simpler, easier to test, and more aligned with good software engineering principles.

### Programming to a Contract Instead of a Concrete Class

The `Agent` does not require a specific LLM implementation such as Ollama or OpenAI.

Instead, it only requires an object that provides the capability it needs: generating a response from a user request.

This idea is known as **programming to a contract** rather than depending on a concrete implementation.

In Python, this contract can be expressed using a `Protocol`, which specifies the behavior expected from collaborating objects without requiring inheritance from a common base class.

For the educational AI Agent, the required contract is intentionally minimal:

- The object must provide an `invoke()` method.

Any object that satisfies this contract can collaborate with the `Agent`.

This approach keeps the architecture flexible, reduces coupling, and prepares the project for future integration with different LLM providers while maintaining a simple design.

**Software Engineering Principles Applied**

- Design by Contract
- Dependency Injection
- Low Coupling
- High Cohesion
- Object-Oriented Design (OOD)
- Separation of Concerns
- KISS
- YAGNI

### The LLM Module

The `llm.py` module defines the contract that every Language Model must satisfy in order to collaborate with the Agent.

Instead of depending on a specific implementation such as Ollama or OpenAI, the Agent depends on a simple contract.

This contract is expressed using Python's `Protocol`, which specifies the behavior required from collaborating objects.

At this stage of the project, the required behavior is intentionally minimal:

- `invoke(question: str) -> str`

The module does not implement any Language Model. It only defines the expected interface.

Separating the contract from the Agent improves readability, reduces coupling, and prepares the project for future integrations with different LLM providers.

**Software Engineering Principles Applied**

- Programming to a Contract
- Single Responsibility Principle (SRP)
- Separation of Concerns
- Low Coupling
- High Cohesion
- KISS
- YAGNI

### The Agent Module

The `agent.py` module defines the central component of the AI Agent System.

The Agent is responsible for coordinating the interaction between the user and the Language Model (LLM).

The Agent does not implement reasoning or generate responses itself. Instead, it delegates that responsibility to an object that satisfies the `LLM` contract defined in `llm.py`.

This design follows the principle of programming to a contract rather than depending on a concrete implementation.

The Agent currently has a single responsibility:

- Receive a user question.
- Delegate it to the LLM.
- Return the generated response.

Future capabilities such as memory, tools, planning, and autonomous workflows will be added incrementally without changing this core responsibility.

**Software Engineering Principles Applied**

- Single Responsibility Principle (SRP)
- Dependency Injection
- Programming to a Contract
- Low Coupling
- High Cohesion
- Separation of Concerns
- Clean Code
- KISS
- YAGNI

## Phase 1.1 - Architectural Validation

Before introducing external libraries or real Language Models, we validated the architecture conceptually.

A simple object implementing the `LLM` contract (for example, `FakeLLM`) can collaborate with the `Agent` without requiring any changes to the Agent itself.

Execution flow:

User
→ Agent.answer()
→ LLM.invoke()
→ Response

This validation confirms that the Agent depends on the behavior defined by the `LLM` contract rather than on a concrete implementation.

As a result, the same Agent can collaborate with different Language Models (such as Ollama or LangChain wrappers) without modifying its internal logic.

### Software Engineering Principles Validated

- Single Responsibility Principle (SRP)
- Dependency Injection
- Programming to a Contract
- Separation of Concerns
- Low Coupling
- High Cohesion
- KISS
- YAGNI

### Conclusion

The initial architecture has been successfully validated and provides a solid foundation for the next phase of the project.

## Phase 1.2 - Environment & Dependency Strategy

### Why initialize the project?

Although Python can execute files without additional configuration, a professional project requires a standard way to describe its identity and environment.

Modern Python projects use `pyproject.toml` as the central configuration file.

This file serves as the single source of truth for:

- Project metadata
- Required Python version
- Runtime dependencies
- Development dependencies
- Tool configuration (Ruff, MyPy, Pytest, etc.)

Using a single configuration file improves maintainability, reduces duplicated configuration, and follows modern Python packaging standards.

### Software Engineering Principles Applied

- DRY (Don't Repeat Yourself)
- Separation of Concerns
- Principle of Least Surprise
- Modern Python Project Standards

## UV Project Initialization

The project was initialized using:

```powershell
uv init . --app --vcs git
```

This transforms a directory containing Python files into a recognized Python project.

The initialization creates the foundational project configuration and establishes a standard structure that modern Python development tools can understand.

At this point, the project has an identity, version control support, and a central configuration file (`pyproject.toml`) that will become the source of truth for dependencies and tool configuration throughout the project.

### Software Engineering Principles Applied

- Modern Python Project Standards
- Separation of Concerns
- DRY (centralized configuration)
- Professional Development Workflow

## Phase 1.2 - Project Initialization and `pyproject.toml`

The project was initialized using UV, creating a modern Python project structure centered around the `pyproject.toml` file.

### Why `pyproject.toml`?

`pyproject.toml` is the standard configuration file for modern Python projects. It acts as the single source of truth for project metadata, dependency management, Python version requirements, and tool configuration.

As the project evolves, this file will also contain the configuration for development tools such as Ruff, MyPy, Pytest, and pre-commit.

### Initial Project Metadata

The generated file defines:

- Project name
- Initial semantic version (`0.1.0`)
- Placeholder description
- README location
- Minimum supported Python version
- Runtime dependencies (currently empty)

At this stage, the empty dependency list is intentional because no external libraries have been introduced yet.

### Software Engineering Principles Applied

- KISS (start with the smallest valid configuration)
- YAGNI (do not add dependencies before they are needed)
- DRY (centralize project configuration)
- Separation of Concerns (configuration separated from application code)
- Modern Python Packaging Standards

## Phase 1.2 - Development Environment Initialization

The project now has a complete development foundation.

### Environment Layers

The architecture is organized into clearly separated responsibilities:

- Operating System
- Conda Environment
- Git Repository
- UV Project Management
- `pyproject.toml` as the project configuration
- `src/` as the application source directory

Each layer has a single responsibility and does not overlap with the others.

## Runtime Dependency Strategy

At this stage of the project, the runtime dependency list is intentionally empty.

The current Agent architecture has been designed using Python abstractions and dependency injection. The implementation intentionally avoids external frameworks and third-party AI services at this stage.

The project separates:

- Runtime dependencies: packages required by the application during execution.
- Development dependencies: packages required to maintain and validate the codebase.

Current development dependencies include:

- Ruff for code quality validation.
- MyPy for static type checking.
- Pytest for automated testing.
- Pre-commit for automated validation before Git commits.

External runtime dependencies will be introduced only when the architecture requires them.

Examples of future runtime dependencies may include:

- LLM providers.
- Agent frameworks.
- Vector databases.
- API integrations.

This follows the engineering principle:

> Introduce complexity only when it provides real value to the system.

### Version Control

Git was initialized during project creation with UV.

A `.gitignore` file was reviewed and adapted to the project's needs, ensuring that generated files, caches, virtual environments, coverage reports, and IDE-specific settings are excluded from version control.

This keeps the repository clean, portable, and focused on source code.

### Software Engineering Principles Applied

- Separation of Concerns
- Single Responsibility Principle
- KISS
- DRY
- Modern Python Development Workflow
- Clean Repository Practices

## Phase 1.3 - Development Environment and Toolchain

The development environment was configured to use the existing Conda environment (`agent_env`) instead of creating a project-local virtual environment.

### Environment Strategy

Responsibilities are clearly separated:

- Conda manages the Python interpreter and environment.
- UV manages the Python project and its dependencies.
- `pyproject.toml` is the single source of truth for project configuration.

### Development Dependencies

The first development tools were added using UV:

- Ruff (linting and formatting)
- MyPy (static type checking)

These tools are stored under the `dependency-groups.dev` section of `pyproject.toml`, keeping them separate from runtime dependencies.

### Engineering Lesson

Modern development tools often provide sensible defaults, but those defaults should always be evaluated against the project's architecture. In this case, UV's default behavior of creating a `.venv` was intentionally overridden to align with the project's Conda-based workflow.

### Software Engineering Principles Applied

- Separation of Concerns
- Single Source of Truth
- KISS
- Root Cause Analysis
- Verify Before Continuing

## Phase 1.3.1 - Code Quality with Ruff

The first automated engineering tool was integrated into the project.

### Purpose

Ruff is responsible for enforcing consistent code style and detecting common code quality issues before the software is executed.

Unlike Python itself, which validates syntax during execution, Ruff performs static analysis of the source code.

### Configuration

Ruff was configured directly inside `pyproject.toml`, reinforcing the project's philosophy of maintaining a single source of truth for configuration.

Only two configuration options were defined:

- Target Python version (`py312`)
- Maximum line length (88 characters)

The configuration intentionally remains minimal, following the KISS and YAGNI principles.

### Validation

The command

`ruff check .`

was executed successfully.

Result:

`All checks passed!`

This confirms that the current codebase satisfies the project's initial code quality standards.

### Software Engineering Principles Applied

- Automation over manual verification
- Single Source of Truth
- KISS
- YAGNI
- Separation of Concerns

## Phase 1.3.2 - Static Type Checking with MyPy

The project now includes static type checking using MyPy.

### Purpose

MyPy analyzes type annotations without executing the program. It verifies that software components interact according to their declared contracts.

Unlike runtime errors, type inconsistencies can be detected during development, reducing the probability of bugs reaching production.

### Configuration

MyPy was configured in `pyproject.toml`:

```toml
[tool.mypy]
mypy_path = ["src"]
```

The `mypy_path` setting informs MyPy where the project's source code resides, matching the selected `src` project layout.

### Practical Validation

A temporary demonstration file intentionally violated the `Agent` constructor contract:

```python
agent = Agent(42)
```

MyPy reported:

```
Argument 1 to "Agent" has incompatible type "int"; expected "LLM"
```

The error was detected before execution, illustrating the value of static analysis.

### Engineering Lessons

- Type hints serve as contracts between software components.
- Static analysis complements runtime testing.
- The `src` layout requires explicit tool configuration, leading to more robust and portable projects.
- Early error detection reduces debugging time and improves software reliability.

### Software Engineering Principles Applied

- Separation of Concerns
- Design by Contract
- Fail Early
- KISS
- Single Source of Truth

## Phase 1.3.3 - Foundations of Unit Testing

Before writing tests, the AAA (Arrange–Act–Assert) pattern was introduced as the standard structure for unit tests.

### The AAA Pattern

A well-designed unit test is divided into three distinct phases:

1. **Arrange**: Prepare the objects, inputs, and dependencies required for the test.
2. **Act**: Execute the single behavior being tested.
3. **Assert**: Verify that the observed result matches the expected outcome.

This structure improves readability, maintainability, and makes the purpose of each test immediately clear.

### Engineering Lessons

- Unit tests should verify one behavior at a time.
- Tests should isolate the component under test from its dependencies.
- Clear test structure is as important as clear production code.
- The AAA pattern naturally reinforces the Single Responsibility Principle and Separation of Concerns.

### Software Engineering Principles Applied

- Single Responsibility Principle (SRP)
- Separation of Concerns
- KISS
- Readability over cleverness

## Phase 1.3.3 - Unit Testing Foundation with Pytest

The project now includes automated unit testing using Pytest.

### Purpose

Pytest was integrated to verify that software components fulfill their defined responsibilities through automated tests.

The first unit test validates the behavior of the Agent component independently from external services.

### Testing Approach

The Agent dependency on an LLM was replaced with a FakeLLM implementation.

This allows the test to focus exclusively on Agent behavior without depending on:

- External APIs
- Network connections
- Real language models
- Non-deterministic responses

### Test Structure

The first test follows the AAA pattern:

- Arrange: Create the FakeLLM and Agent objects.
- Act: Execute the Agent behavior.
- Assert: Verify that the returned response matches expectations.

### Project Configuration

Pytest was configured in `pyproject.toml` using:

[tool.pytest.ini_options]
pythonpath = ["src"]

This configuration allows Pytest to correctly discover and import the application package using the project's `src` layout.

### Engineering Principles Applied

- Single Responsibility Principle
- Separation of Concerns
- Dependency Injection
- Test Isolation
- Convention over Configuration
- Fail Early

## Phase 1.3 - Engineering Toolchain

The project now includes a complete local software engineering workflow.

### Purpose

The objective of this milestone was to establish automated mechanisms that help maintain code quality, correctness, and reliability during development.

### Implemented Components

The project now integrates:

- Ruff for code quality validation.
- MyPy for static type checking.
- Pytest for automated behavior testing.
- Pre-commit for automatic validation before Git commits.

### Testing Foundation

The first unit test was created for the Agent component.

The test verifies that:

- The Agent receives a user request.
- The Agent delegates the request to an LLM dependency.
- The Agent returns the generated response.

A FakeLLM implementation was used to isolate the Agent behavior from external services.

### Development Workflow

The project now follows this workflow:

Developer changes code.

↓

Automated validation runs through pre-commit.

↓

Ruff, MyPy, and Pytest verify the changes.

↓

Only validated code is committed.

### Engineering Principles Applied

- Single Responsibility Principle
- Separation of Concerns
- Dependency Injection
- Test Isolation
- Fail Early
- Automation
- Reproducibility

### Result

The project has moved from a simple Python application structure into a maintainable software engineering foundation ready for future AI system development.

## Testing Foundation

The project now includes its first unit testing foundation.

The objective is to verify application behavior independently from external systems.

The Agent component is tested using a FakeLLM implementation instead of a real Language Model.

This allows the test to validate the Agent responsibility:

- Receive a user request.
- Delegate the request to an LLM dependency.
- Return the generated response.

The test does not validate external services, APIs, or model performance.

Those responsibilities belong to different layers of the system.

### Testing Principles Applied

- Unit testing.
- Dependency isolation.
- Fake objects (test doubles).
- Separation of concerns.
- Deterministic behavior.

The testing architecture follows the same dependency injection strategy used in the application design:

Agent → LLM Contract → FakeLLM (test)

This foundation allows future integration with real LLM providers while keeping the core system reliable and testable.
