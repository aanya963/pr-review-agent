from github import Github
from dotenv import load_dotenv
import os

load_dotenv()


class GitHubTool:

    def __init__(self):
        self.github = Github(
            os.getenv("GITHUB_TOKEN")
        )

    def get_pr_details(
        self,
        owner,
        repo,
        pr_number
    ):
        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        return {
            "title": pr.title,
            "body": pr.body,
            "state": pr.state,
            "author": pr.user.login
        }
    

    def get_pr_files(self,
        owner,
        repo,
        pr_number
    ):

        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        pr = repository.get_pull(pr_number)

        files = []
        
        for file in pr.get_files():

            files.append({
                "filename": file.filename,
                "status": file.status,
                "changes": file.changes,
                "patch": file.patch
            })

        return files
    

    def get_pull_request_object(
        self,
        owner,
        repo,
        pr_number
    ):

        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        return repository.get_pull(pr_number)
    
    def get_pull_request_object(
        self,
        owner,
        repo,
        pr_number
    ):
        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        return repository.get_pull(pr_number)


    def get_file_content(
        self,
        owner,
        repo,
        path,
        ref
    ):

        repository = self.github.get_repo(
            f"{owner}/{repo}"
        )

        try:
            file = repository.get_contents(
                path,
                ref=ref
            )

            return file.decoded_content.decode("utf-8")

        except Exception:
            return ""
        