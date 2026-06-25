from typing import TypedDict
from services.cache_service import CacheService
from langgraph.graph import StateGraph, START, END
from services.cache_service import CacheService
from tools.github_tool import GitHubTool
from services.pr_reviewer import PRReviewer
from services.review_aggregator import ReviewAggregator
from agents.repository_agent import RepositoryAgent

aggregator = ReviewAggregator()
repo_agent = RepositoryAgent()
github_tool = GitHubTool()
reviewer = PRReviewer()
# LangGraph passes this object between nodes.
# After Repository Analysis: "repo_summary": "...."
class PRReviewState(TypedDict):

    owner: str
    repo: str
    pr_number: int

    force_refresh: bool

    repo_summary: str 

    files: list
    reviews: list

    final_report: str

# A node is simply a function.
#input : state, output : updated state

# Repository
#     ↓
# Analyze Architecture
#     ↓
# Generate Repo Summary
def repository_analysis_node(state):

    owner = state["owner"]
    repo = state["repo"]

    force_refresh = state.get(
        "force_refresh",
        False
    )

    if (
        CacheService.exists(
            owner,
            repo
        )
        and not force_refresh
    ):

        print(
            "Using Cached Repository Analysis..."
        )

        state["repo_summary"] = (
            CacheService.load(
                owner,
                repo
            )
        )

        return state

    print(
        "Analyzing Repository..."
    )

    repo_url = (
        f"https://github.com/"
        f"{owner}/"
        f"{repo}.git"
    )

    analysis = repo_agent.analyze(
        repo_url
    )

    CacheService.save(
        owner,
        repo,
        analysis
    )

    state["repo_summary"] = analysis

    return state

# GitHub API
#      ↓
# Fetch PR Files
def fetch_pr_node(state):

    files = github_tool.get_pr_files(
        state["owner"],
        state["repo"],
        state["pr_number"]
    )

    print(f"Fetched {len(files)} files")

    state["files"] = files

    return state

# For each file
#       ↓
# Call LLM
#       ↓
# Generate Review
def review_files_node(state):

    reviews = []

    for file in state["files"]:

        print(f"Reviewing {file['filename']}")

        review = reviewer.review_file(
            file["filename"],
            file["patch"],
            state["repo_summary"]
        )

        reviews.append({
            "file": file["filename"],
            "review": review
        })

    state["reviews"] = reviews

    return state

def aggregate_node(state):

    report = aggregator.aggregate_reviews(
        state["reviews"]
    )

    state["final_report"] = report

    return state

# //creates the graph:
graph = StateGraph(PRReviewState)

# How LangGraph Knows Order?

graph.add_node(
    "repository_analysis",
    repository_analysis_node
)

graph.add_node(
    "fetch_pr",
    fetch_pr_node
)

graph.add_node(
    "review_files",
    review_files_node
)

graph.add_node(
    "aggregate",
    aggregate_node
)

graph.add_edge(
    START,
    "repository_analysis"
)

graph.add_edge(
    "repository_analysis",
    "fetch_pr"
)

graph.add_edge(
    "fetch_pr",
    "review_files"
)

graph.add_edge(
    "review_files",
    "aggregate"
)

graph.add_edge(
    "aggregate",
    END
)

app = graph.compile()



# What Happens When app.invoke() Runs?

# LangGraph:

# Step 1

# Calls

# repository_analysis_node()

# returns updated state.

# Step 2

# Passes state to

# fetch_pr_node()
# Step 3

# Passes state to

# review_files_node()
# Step 4

# Passes state to

# aggregate_node()
# Step 5

# Returns final state.