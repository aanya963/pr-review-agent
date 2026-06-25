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
            You are a Principal Software Engineer.

            Below are code review findings for individual files.

            Create ONE concise PR review.

            Include:

            1. Executive Summary
            2. Top Issues
            3. Risk Level (Low/Medium/High)
            4. Recommendation

            Reviews:

            {all_reviews}
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