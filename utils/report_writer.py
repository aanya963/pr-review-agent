from pathlib import Path


class ReportWriter:

    @staticmethod
    def save(report):

        Path("reports").mkdir(exist_ok=True)

        with open(
            "reports/pr_review.md",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(report)