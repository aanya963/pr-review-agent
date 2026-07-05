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
        You are a Senior .NET Architect.

        A Pull Request cannot be merged because of a merge conflict.

        File:

        {filename}

        ==========================
        Current Branch
        ==========================

        {current_code}

        ==========================
        Incoming Branch
        ==========================

        {incoming_code}

        Tasks

        1. Explain why this conflict happened.

        2. Explain which code should be kept.

        3. Generate the merged code.

        4. Mention any risks.

        Respond in GitHub Markdown.

        Keep the response under 250 words.

        Do not explain Git.

        Focus only on this file.
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