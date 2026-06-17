# Interview Questions and Answers

## Explain your project.

I built an AI-powered Pull Request Review Agent using LangGraph, Groq LLMs, and GitHub APIs.

The system first analyzes a repository to understand its architecture and tech stack.

It then fetches Pull Request changes from GitHub, reviews modified files using an LLM, and generates a consolidated review report.

---

## Why did you build this?

I wanted a practical project to learn:

* Agentic AI
* Tool Calling
* LangGraph
* AI workflow orchestration

while solving a real engineering problem.

---

## Why use LangGraph?

LangGraph provides:

* State management
* Workflow orchestration
* Multi-step execution

It is better suited than simple scripts for agent workflows.

---

## What is the state in your graph?

The state contains:

* owner
* repo
* pr_number
* repo_summary
* files
* reviews
* final_report

Each node reads and updates state.

---

## What tools did you create?

Git Tool

Clones repositories.

GitHub Tool

Fetches PR information.

Repo Scanner

Scans repository structure.

README Reader

Reads repository documentation.

Code Explorer

Extracts code samples.

---

## Why not review code directly?

Reviewing code without repository context often produces generic reviews.

Repository understanding improves review quality.

---

## Biggest challenge?

Generating useful repository context.

Initially, reviews were generic.

Adding repository analysis significantly improved results.

---

## How did you optimize performance?

I implemented caching.

Repository analysis results are stored locally.

Subsequent executions reuse cached summaries.

---

## What would you improve?

* Parallel file reviews
* GitHub comment posting
* Security review agent
* Automated approvals
* CI/CD integration

---

## What did you learn?

I learned that AI systems are more than prompts.

Production AI systems require:

* APIs
* Context engineering
* Tool calling
* Workflow orchestration
* State management
* Performance optimization

This project gave me hands-on experience with all of them.
