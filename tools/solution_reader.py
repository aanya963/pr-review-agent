import os
import re

class SolutionReader:

    @staticmethod
    def read(repo_path):

        for root, _, files in os.walk(repo_path):

            for file in files:

                if file.endswith(".sln"):

                    path = os.path.join(root, file)

                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    projects = re.findall(
                        r'Project\(.*?\)\s*=\s*".*?",\s*"(.*?)"',
                        content
                    )

                    return "\n".join(projects)

        return "No solution found."