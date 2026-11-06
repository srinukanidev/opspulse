# OpsPulse – AI-Powered Operations Copilot

OpsPulse is a hands-on Python and Applied AI engineering project focused on building an intelligent operations copilot for incident analysis, log diagnostics, and automated troubleshooting.

The project is being developed incrementally, starting with Python fundamentals and progressing towards production-grade AI systems using LLMs, Retrieval-Augmented Generation (RAG), AI agents, and secure backend services.

## Project Goals

- Build strong Python programming and software engineering fundamentals.
- Develop modular, maintainable Python applications.
- Build backend services using FastAPI.
- Integrate PostgreSQL and Redis.
- Implement LLM-powered incident analysis.
- Build secure RAG pipelines for operational knowledge.
- Develop AI agents for incident investigation and diagnostics.
- Implement evaluations, observability, security, and deployment practices.

## Current Implementation

The initial version focuses on Python-based log analysis.

Current capabilities:

- Read application log files.
- Process log entries line by line.
- Identify ERROR, WARNING, and INFO messages.
- Count log entries by severity.
- Display a log analysis summary.

## Project Structure

```text
opspulse/
│
├── data/
│   └── sample.log
│
├── src/
│   └── opspulse/
│       ├── __init__.py
│       ├── main.py
│       └── parse_log.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| uv | Python project and dependency management |
| Git | Version control |
| GitHub | Source code hosting |

Additional technologies will be introduced as the project evolves.

## Getting Started

### Prerequisites

- Python 3.12+
- uv
- Git

### 1. Clone the repository

```bash
git clone https://github.com/srinukanidev/opspulse.git
cd opspulse
```

### 2. Install dependencies

```bash
uv sync
```

This creates the virtual environment and installs the project dependencies using the lockfile.

### 3. Run the application

```bash
uv run python -m opspulse.main
```

## Development Workflow

This project follows a practical engineering workflow:

1. Learn the concept.
2. Implement the functionality.
3. Run and test the code.
4. Review and improve the implementation.
5. Commit changes to Git.
6. Push changes to GitHub.

### Git commands

```bash
git status
git add .
git commit -m "feat: describe your changes"
git push
```

## Planned Development Roadmap

| Phase | Focus Area |
|---|---|
| Phase 1 | Python fundamentals and systems scripting |
| Phase 2 | Backend engineering with FastAPI, PostgreSQL and Redis |
| Phase 3 | LLM integration and secure AI gateways |
| Phase 4 | Retrieval-Augmented Generation (RAG) |
| Phase 5 | AI agents and workflow orchestration |
| Phase 6 | Evaluation, observability, security and deployment |

## Learning Philosophy

OpsPulse is not just a sample application. It is an evolving engineering project designed to apply each newly learned concept to a realistic operational use case.

The focus is on writing understandable, testable, secure, maintainable, and production-ready code.

## Repository

GitHub: https://github.com/srinukanidev/opspulse

---

**Status:** Initial Python development

**Project:** OpsPulse – AI-Powered Operations Copilot