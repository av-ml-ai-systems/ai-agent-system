🟢 Pre-Phase (Phase 0) — Project Foundation ✅ Completed

🟢 Defined the philosophy of the project.
🟢 Defined the educational objectives.
🟢 Established the "understand before coding" workflow.
🟢 Defined the project scope (simple, educational, not production).
🟢 Selected LangChain as the future orchestration framework.
🟢 Decided to postpone unnecessary complexity (memory, tools, FastAPI, Docker, React, Streamlit, etc.).
🟢 Defined the software engineering philosophy (KISS, YAGNI, DRY, SRP, Separation of Concerns, Clean Code).
🟢 Defined the environment strategy (Conda + UV, one interpreter only, no .venv).
🟢 Created and documented the Phase 0 Markdown file.

🟢 Phase 1.1 — Project Structure Design ✅ Completed

🟢 Created the project folder.
🟢 Opened the project in VS Code.
🟢 Activated agent_env.
🟢 Created the docs/ folder.
🟢 Created the src/ folder.
🟢 Created the tests/ folder.
🟢 Learned why professional Python projects use the src layout.
🟢 Created the ai_agent_system package.
🟢 Created __init__.py.
🟢 Designed the responsibilities of the Agent.
🟢 Designed the LLM collaboration model.
🟢 Introduced Dependency Injection.
🟢 Introduced Programming to a Contract using a Protocol.
🟢 Created llm.py.
🟢 Created agent.py.
🟢 Performed the first architectural validation using a conceptual FakeLLM.
🟢 Documented all important architectural decisions.

🟢 Phase 1.2 — Environment & Dependency Strategy

✅ Initialize the project with UV.
✅ Create pyproject.toml.
✅ Explain every section of pyproject.toml.
✅ Configure the project to use the external agent_env.
✅ Initialize the Git repository.
✅ Create .gitignore.
✅ Verify that everything uses the same Python interpreter.
✅ Document the environment strategy.

🟢 Phase 1.3 — Engineering Toolchain

✅ Install Ruff.
✅ Install MyPy.
✅ Install Pytest.
✅ Install pre-commit.
✅ Configure each tool.
✅ Learn why each tool exists.
✅ Run the first validation commands.

Completed quality pipeline:

Ruff
 ↓
MyPy
 ↓
Pytest
 ↓
Pre-commit

🟢 Phase 1.4 — Configuration Foundation (Completed)

🟢 Introduce pyproject.toml as the source of truth.
🟢 Add project metadata.
🟢 Learn how professional Python projects manage configuration.
🟢 Understand dependency groups and project configuration strategy.
🟢 Review the role of uv.lock.
🟢 Prepare the project for future dependencies.

🟢 Phase 1.5 — Testing Foundation

🟢 Learn the philosophy of unit testing.
🟢 Create the first real unit test.
🟢 Test the Agent using a FakeLLM.
🟢 Understand mocking and test doubles.
🟢 Build confidence before integrating a real LLM.

🟡 Phase 2 — First Real LLM Integration
2.1 — LLM Integration Foundations

⬜ Review the current LLM abstraction.
⬜ Understand LLM interfaces, implementations, and providers.
⬜ Identify where the real LLM enters the architecture.
⬜ Apply dependency inversion principles.
⬜ Preserve separation between Agent logic and infrastructure.

2.2 — Introduce Ollama

⬜ Understand Ollama architecture.
⬜ Install and configure Ollama.
⬜ Download and manage a local LLM model.
⬜ Execute the first local inference.
⬜ Understand local model resource requirements.

2.3 — Create the First Real LLM Adapter

⬜ Create an Ollama-based LLM implementation.
⬜ Connect Ollama to the existing LLM abstraction.
⬜ Apply the Adapter Pattern.
⬜ Use dependency injection with the new implementation.
⬜ Keep the Agent independent from Ollama.

2.4 — Introduce LangChain

⬜ Understand why LangChain exists.
⬜ Introduce LangChain models.
⬜ Introduce LangChain message handling.
⬜ Connect LangChain with Ollama.
⬜ Understand LangChain responsibilities and limitations.

2.5 — Refactor the LLM Layer

⬜ Integrate LangChain without changing the Agent interface.
⬜ Separate application logic from LLM infrastructure.
⬜ Maintain interchangeable LLM implementations.
⬜ Update the architecture documentation.

2.6 — First Real Conversation

⬜ Connect the Agent to a real local LLM.
⬜ Execute the first real conversation.
⬜ Observe the complete request-response flow.
⬜ Document the new architecture milestone.

2.7 — Phase 2 Validation

⬜ Validate with Ruff.
⬜ Validate with MyPy.
⬜ Validate with Pytest.
⬜ Keep FakeLLM tests working.
⬜ Add integration testing strategy.

2.8 — Phase 2 Architectural Checkpoint

⬜ Document the real LLM integration.
⬜ Document Ollama integration.
⬜ Document LangChain integration.
⬜ Review architectural decisions.
⬜ Prepare for prompt engineering phase.

⬜ Phase 2 — First Real LLM Integration

⬜ Introduce Ollama.
⬜ Introduce LangChain.
⬜ Connect the Agent to a real LLM.
⬜ Execute the first real conversation.

⬜ Phase 3 — Prompts

⬜ Learn prompt engineering fundamentals.
⬜ Create prompt templates.
⬜ Separate prompts from business logic.

⬜ Phase 4 — Memory

⬜ Introduce conversational memory.
⬜ Understand why memory is a separate responsibility.

⬜ Phase 5 — Tool Calling

⬜ Create the first tool.
⬜ Add two or three simple tools.
⬜ Learn how the Agent decides when to use them.

⬜ Phase 6 — Multi-step Reasoning

⬜ Planning.
⬜ Reasoning loop.
⬜ Execution loop.
⬜ Feedback loop.

⬜ Phase 7 — User Interfaces

⬜ Streamlit interface.
⬜ FastAPI integration.
⬜ React frontend (later in the phase).

⬜ Phase 8 — Final Refactoring

⬜ Improve the architecture.
⬜ Refactor where necessary.
⬜ Apply everything learned throughout the project.

⬜ Phase 9 — Portfolio Preparation

⬜ Clean the repository.
⬜ Improve the README.
⬜ Review the architecture.
⬜ Prepare the project for GitHub.