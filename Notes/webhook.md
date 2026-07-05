api/
    webhook.py

services/
    github_comment_service.py

main_api.py

run.py


GitHub
    │
    ▼
Webhook
    │
    ▼
FastAPI
    │
    ▼
LangGraph
    │
    ├── Repository Analysis
    ├── PR Review
    ├── Merge Conflict Analysis
    └── Final Report
    │
    ▼
Comment automatically appears on GitHub PR