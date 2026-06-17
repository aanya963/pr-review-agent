# STACKS:
AI Concepts

✅ Agent workflow
✅ Tool calling
✅ GitHub integration
✅ LLM orchestration
✅ Context-aware review generation

Engineering Concepts

✅ Caching
✅ Repository scanning
✅ API integration
✅ State management

Frameworks

✅ LangGraph
✅ Groq/OpenAI style APIs

# Technical Deep Dive - AI PR Review Agent

## High-Level Architecture

User Input

↓

Repository Analysis

↓

Repository Summary

↓

PR File Extraction

↓

File Reviews

↓

Review Aggregation

↓

Final Report

---

## Components

### 1. Repository Agent

Purpose:

Understand repository architecture before PR review.

Responsibilities:

* Clone repository
* Scan repository structure
* Read README
* Extract code samples
* Generate architecture summary

Files:

agents/repository_agent.py

tools/git_tool.py

tools/repo_scanner.py

tools/readme_reader.py

tools/code_explorer.py

services/architecture_analyzer.py

---

### 2. GitHub Tool

Purpose:

Interact with GitHub APIs.

Responsibilities:

* Fetch PR metadata
* Fetch changed files
* Extract patches

Files:

tools/github_tool.py

Methods:

get_pull_request()

get_pr_files()

---

### 3. PR Reviewer

Purpose:

Review code changes using LLM.

File:

services/pr_reviewer.py

Input:

* filename
* patch
* repository summary

Output:

* review comments

Model:

llama-3.3-70b-versatile

Provider:

Groq

---

### 4. Review Aggregator

Purpose:

Combine individual file reviews into a final report.

File:

services/review_aggregator.py

Output:

* Executive Summary
* Risks
* Recommendations

---

### 5. Cache Service

Purpose:

Avoid repeated repository analysis.

File:

services/cache_service.py

Problem Solved:

Repository analysis takes time.

Without cache:

Clone Repo
→ Scan
→ Analyze

every run.

With cache:

Load existing summary.

Benefits:

* Faster execution
* Lower LLM cost

---

## LangGraph Workflow

State:

owner

repo

pr_number

repo_summary

files

reviews

final_report

---

Node 1

repository_analysis_node

Generates repository context.

---

Node 2

fetch_pr_node

Fetches changed files.

---

Node 3

review_files_node

Reviews each modified file.

---

Node 4

aggregate_node

Creates final report.

---

Execution Flow

START

↓

repository_analysis

↓

fetch_pr

↓

review_files

↓

aggregate

↓

END

---

## Design Decisions

### Why LangGraph?

Instead of writing:

step1()

step2()

step3()

I wanted a framework designed for AI workflows.

LangGraph provides:

* State management
* Workflow orchestration
* Extensibility

### Why Repository Context?

Without repository understanding:

Reviews become generic.

Repository summary improves:

* Accuracy
* Relevance
* Architectural awareness

### Why Cache?

Repository architecture changes infrequently.

Caching avoids unnecessary analysis.
