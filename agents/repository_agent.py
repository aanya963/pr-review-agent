# agents/repository_agent.py

from agents.base_agent import BaseAgent
from services.architecture_analyzer import ArchitectureAnalyzer
from tools.code_explorer import CodeExplorer
from tools.git_tool import GitTool
from tools.repo_scanner import RepoScanner
from tools.readme_reader import ReadmeReader
# from services.repo_analyzer import RepoAnalyzer


class RepositoryAgent(BaseAgent):

    def analyze(self, repo_url: str):

        self.log("Step 1: Cloning Repository...")
        repo_path = GitTool.clone_repository(repo_url)

        self.log("Step 2: Scanning Repository...")
        scan_result = RepoScanner.scan_repository(repo_path)

        self.log("Step 3: Reading README...")
        readme_content = ReadmeReader.read(repo_path)

        self.log("Step 4: Generating Analysis...")
        code_samples = CodeExplorer.get_code_samples(
            repo_path
        )
        analysis = ArchitectureAnalyzer.analyze(
            scan_result,
            readme_content,
            code_samples
        )
        return analysis