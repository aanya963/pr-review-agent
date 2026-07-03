import os


class ProgramReader:

    @staticmethod
    def read(repo_path):

        keywords = (
            "builder.Services",
            "app.Use",
            "MapControllers",
            "AddAuthentication",
            "AddAuthorization",
            "AddDbContext"
        )

        for root, _, files in os.walk(repo_path):

            if "Program.cs" not in files:
                continue

            path = os.path.join(root, "Program.cs")

            important = []

            with open(path, "r", encoding="utf-8", errors="ignore") as f:

                for line in f:

                    if any(k in line for k in keywords):

                        important.append(line.strip())

            return "\n".join(important)

        return "Program.cs not found."