from fastapi import APIRouter, Request

from graphs.pr_review_graph import app
from services.github_comment_service import GitHubCommentService

router = APIRouter()
comment_service = GitHubCommentService()

@router.post("/webhook")
async def github_webhook(request: Request):

    payload = await request.json()

    # Only react when PR is opened or updated
    if payload.get("action") not in ["opened", "synchronize", "reopened"]:
        return {"message": "Ignored"}

    owner = payload["repository"]["owner"]["login"]
    repo = payload["repository"]["name"]
    pr_number = payload["pull_request"]["number"]

    print(f"\nNew PR Received #{pr_number}")

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

    # print(result["final_report"])
    comment_service.post_comment(
        owner,
        repo,
        pr_number,
        result["final_report"]
    )

    return {"status": "completed"}