from graphs.pr_review_graph import app 
# import LangGraph workflow, URL parser
from utils.url_parser import parse_pr_url

pr_url = "https://github.com/langchain-ai/langgraph/pull/8093"

#extract the owner, repo, pr_number
owner, repo, pr_number = parse_pr_url(pr_url)
# This starts the entire LangGraph workflow.
# it triggers a LangGraph workflow.
# the workflow orchestrates repository analysis, PR file retrieval, AI-powered review generation, and final review aggregation.
result = app.invoke(
    {
        "owner": owner,
        "repo": repo,
        "pr_number": pr_number,
        "force_refresh": False,
        "repo_summary": "",
        "files": [],
        "reviews": [],
        "final_report": ""
    }
)

print("\n")
print("=" * 80)

print(result["final_report"])