import os
import time

from graphs.pr_review_graph import app
from utils.url_parser import parse_pr_url

start = time.time()

# Check if running inside GitHub Actions
if os.getenv("PR_NUMBER"):

    owner = os.getenv("OWNER")
    repo = os.getenv("REPO")
    pr_number = int(os.getenv("PR_NUMBER"))

else:

    # Local Development
    pr_url = "https://github.com/aanya963/ai-log-processing-system/pull/3"

    owner, repo, pr_number = parse_pr_url(pr_url)

result = app.invoke(
    {
        "owner": owner,
        "repo": repo,
        "pr_number": pr_number,
        "force_refresh": False,
        "repo_summary": "",
        "has_conflict": False,
        "conflict_report": "",
        "files": [],
        "reviews": [],
        "final_report": ""
    }
)

print("\n")
print("=" * 80)
print(result["final_report"])
print("=" * 80)

print(f"\nCompleted in {time.time()-start:.2f} seconds")