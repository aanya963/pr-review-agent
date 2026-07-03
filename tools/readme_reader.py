from pathlib import Path


class ReadmeReader:

    @staticmethod
    def read(repo_path):

        readme_path = Path(repo_path) / "README.md"

        if not readme_path.exists():
            return ""

        content = readme_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return content[:2000]