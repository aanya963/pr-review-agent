from tools.github_tool import GitHubTool

github = GitHubTool()

pr = github.get_pull_request_object(
    "langchain-ai",
    "langgraph",
    8093
)

print("PR Title:", pr.title)
print("Mergeable:", pr.mergeable)
print("Merged:", pr.merged)
print("Base Branch:", pr.base.ref)
print("Head Branch:", pr.head.ref)