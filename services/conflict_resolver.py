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
        current_branch,
        incoming_branch
    ):

        prompt = f"""
You are a Senior .NET Software Engineer.

A merge conflict occurred.

File:
{filename}

Current Branch Code:

{current_branch}

Incoming Branch Code:

{incoming_branch}

Explain:

1. Why the conflict happened.

2. Which code should be preserved.

3. Suggest the final merged code.

4. Mention possible risks.

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