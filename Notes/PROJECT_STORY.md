# AI PR Review Agent - Project Story

## Why I Built This

While learning AI Agents, Tool Calling, and LangGraph, I wanted to build a project that solves a real engineering problem instead of a simple chatbot.

In software development, Pull Requests are reviewed manually by engineers. For large repositories, understanding repository architecture before reviewing code changes can be time-consuming.

I wanted to build an AI-powered system that:

* Understands a repository
* Reads Pull Request changes
* Reviews modified files
* Generates meaningful review feedback

This project helped me learn:

* Agentic AI systems
* LangGraph orchestration
* Tool Calling
* GitHub API integration
* Repository analysis
* Multi-step AI workflows

---

## Problem Statement

Most AI code review tools only look at changed code.

Without repository context, the AI may generate generic or incorrect reviews.

For example:

A change might look risky in isolation but may actually be valid based on repository architecture.

I wanted the AI to understand:

* Repository purpose
* Tech stack
* Architecture
* Design patterns

before reviewing code.

---

## My Solution

I built an AI PR Review Agent.

The workflow:

1. Analyze repository
2. Understand architecture
3. Fetch Pull Request changes
4. Review modified files
5. Generate final review report

This makes reviews more contextual and useful.

---

## Key Learnings

### Agent Design

I learned how to separate responsibilities between:

* Repository Agent
* PR Review Agent

instead of creating one giant script.

### Tool Calling

I learned how agents use tools:

* GitHub Tool
* Git Tool
* Repo Scanner
* README Reader

to gather information before reasoning.

### Workflow Orchestration

I learned LangGraph concepts:

* State
* Nodes
* Edges
* Execution flow

### AI Engineering

I learned that building AI systems is not only about prompts.

Real AI systems require:

* APIs
* Data collection
* Context generation
* State management
* Caching

---

## Future Improvements

* Parallel review execution
* GitHub PR comments
* Security review agent
* Test coverage analysis
* CI/CD integration
