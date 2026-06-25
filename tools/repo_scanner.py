from pathlib import Path


class RepoScanner:

    IMPORTANT_FILES = [
        "README.md",
        "requirements.txt",
        "pyproject.toml",
        # "package.json",
        "Dockerfile",
        "pom.xml"
    ]

    @staticmethod
    def scan_repository(repo_path: str):

        repo = Path(repo_path)

        result = {
            "repository_name": repo.name,
            "important_files": [],
            "important_folders": [],
            "detected_tech": []
        }

        for item in repo.iterdir():

            if item.name.startswith("."):
                continue

            if item.is_dir():
                result["important_folders"].append(item.name)

            if item.name in RepoScanner.IMPORTANT_FILES:
                result["important_files"].append(item.name)

        # Technology Detection

        if (repo / "requirements.txt").exists():
            result["detected_tech"].append("Python")

        if (repo / "pyproject.toml").exists():
            result["detected_tech"].append("Python")

        if (repo / "package.json").exists():
            result["detected_tech"].append("Node.js")

        if (repo / "pom.xml").exists():
            result["detected_tech"].append("Java")

        if (repo / "Dockerfile").exists():
            result["detected_tech"].append("Docker")

        return result