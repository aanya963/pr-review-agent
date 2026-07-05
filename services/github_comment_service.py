from tools.github_tool import GitHubTool


class GitHubCommentService:

    def __init__(self):
        self.github_tool = GitHubTool()

    def post_comment(
        self,
        owner,
        repo,
        pr_number,
        comment
    ):

        repository = self.github_tool.github.get_repo(
            f"{owner}/{repo}"
        )

        issue = repository.get_issue(pr_number)

        issue.create_comment(comment)

        print("✅ Comment posted to GitHub.")