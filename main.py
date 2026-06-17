from graphs.pr_review_graph import app

from utils.url_parser import parse_pr_url

pr_url = "https://github.com/langchain-ai/langgraph/pull/8093"

owner, repo, pr_number = parse_pr_url(pr_url)

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