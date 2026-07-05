from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class PRReviewer:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def review_file(self, filename, patch, repo_summary):

        prompt = f"""
You are a Principal .NET Code Reviewer.

Repository Summary:
{repo_summary}

File:
{filename}

Git Diff:
{patch}

Review ONLY this file.

Focus on:

1. Bugs
2. .NET coding standards
3. SOLID violations
4. Dependency Injection issues
5. Entity Framework issues
6. Async/Await mistakes
7. Performance
8. Security
9. Regression risks

For every issue provide:

Severity:
High / Medium / Low

Issue:

Recommendation:

If there are no issues, say:

"No significant issues found."

Do NOT summarize the repository.
Review ONLY this file.
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