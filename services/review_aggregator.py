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
            You are a Principal .NET Engineering Manager.

            You are reviewing a Pull Request.

            Below are AI reviews generated for each changed file.

            {all_reviews}

            Generate a concise GitHub PR review.

            Maximum 350 words.

            Output EXACTLY in this format.

            # 🤖 AI Code Review

            ## Overall Decision

            Choose one:
            - ✅ Approve
            - 🟡 Approve with Minor Changes
            - ❌ Request Changes

            ---

            ## Summary

            - Files Reviewed:
            - High:
            - Medium:
            - Low:

            ---

            ## Must Fix

            List ONLY High and Medium issues.

            For each issue:

            ### filename

            Issue:
            Why:
            Recommendation:

            Maximum 5 issues.

            ---

            ## Improvements

            Maximum 5 bullet points.

            ---

            ## Positive Findings

            Maximum 5 bullet points.

            ---

            Keep the review concise.

            Do NOT include merge conflict analysis.

            Do NOT repeat issues.

            Do NOT write long explanations.
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