from github import Github
import os


class GitHubCommenter:

    def __init__(self):

        self.github = Github(
            os.getenv("GITHUB_TOKEN")
        )

    def comment(
        self,
        owner,
        repo,
        pr_number,
        report
    ):

        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        pr.create_issue_comment(report)