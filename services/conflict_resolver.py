from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class ConflictResolver:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def resolve(
        self,
        filename,
        current_code,
        incoming_code
    ):

        prompt = f"""
You are a Senior .NET Engineer.

A merge conflict occurred.

Filename:
{filename}

Current Branch Code:
{current_code}

Incoming Branch Code:
{incoming_code}

Your job:

1. Explain why the conflict occurred.
2. Identify risks.
3. Generate the best merged code.
4. Explain your decision.

Return Markdown.
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