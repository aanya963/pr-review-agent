import os


class DotNetExplorer:

    @staticmethod
    def scan(repo_path):

        result = {
            "controllers": [],
            "services": [],
            "repositories": [],
            "entities": [],
            "dbcontexts": []
        }

        for root, _, files in os.walk(repo_path):

            folder = root.lower()

            for file in files:

                if not file.endswith(".cs"):
                    continue

                full_path = os.path.join(root, file)

                if "controller" in file.lower():
                    result["controllers"].append(full_path)

                elif "service" in file.lower():
                    result["services"].append(full_path)

                elif "repository" in file.lower():
                    result["repositories"].append(full_path)

                elif "entity" in folder:
                    result["entities"].append(full_path)

                elif "dbcontext" in file.lower():
                    result["dbcontexts"].append(full_path)

        return result