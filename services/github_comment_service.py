from tools.github_tool import GitHubTool


class GitHubCommentService:

    def __init__(self):
        self.github_tool = GitHubTool()

    def post_review(
        self,
        owner,
        repo,
        pr_number,
        body,
        event="COMMENT"
    ):

        repository = self.github_tool.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        pr.create_review(
            body=body,
            event=event
        )

        print("✅ GitHub Review Posted")


    def post_conflict_review(
        self,
        owner,
        repo,
        pr_number,
        report
    ):

        repository = self.github_tool.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        pr.create_issue_comment(report)

        print("✅ Conflict Review Posted")