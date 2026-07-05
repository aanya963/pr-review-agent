from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class ReviewAggregator:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def aggregate_reviews(
        self,
        reviews
    ):

        all_reviews = ""

        for review in reviews:

            all_reviews += (
                f"\nFILE: {review['file']}\n"
                f"{review['review']}\n"
            )

        prompt = f"""
            You are a Principal Engineering Manager.

            You are given AI code reviews for multiple files.

            Reviews:

            {all_reviews}

            Generate the report in EXACTLY this format.

            # Executive Summary

            Summarize the PR in 2-3 lines.

            # Code Review Findings

            List all issues grouped by severity.

            ## High

            ...

            ## Medium

            ...

            ## Low

            ...

            # Final Recommendation

            One of:

            - Approve
            - Approve with minor changes
            - Request Changes

            IMPORTANT:

            Do NOT invent issues.

            Do NOT invent files.

            Only summarize what appears in the reviews.

            If every review says "No significant issues found"

            then simply output

            "No significant issues found."
            """

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content