# services/architecture_analyzer.py

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ArchitectureAnalyzer:

    @staticmethod
    def analyze(
    scan_result,
        readme,
        solution,
        projects,
        program,
        dotnet_summary
    ):

        prompt = f"""
        You are a Staff Software Engineer specializing in ASP.NET Core applications.

        Analyze the following .NET repository.

            Repository Metadata:
            {scan_result}

            README Summary:
            {readme}

            Projects:
            {solution}

            NuGet & Frameworks:
            {projects}

            Startup Configuration:
            {program}

            Detected Components:
            {dotnet_summary}

        Generate a detailed report containing:

        1. Project Purpose
        2. Tech Stack (.NET version, NuGet packages, database, messaging, etc.)
        3. High-Level Architecture
        4. Project Layers (API, Application, Domain, Infrastructure, Tests)
        5. Dependency Injection setup
        6. Main Components (Controllers, Services, Repositories, DbContext)
        7. Design Patterns used (Clean Architecture, Repository, CQRS, Dependency Injection, etc.)
        8. External Integrations (Redis, RabbitMQ, Azure, SQL Server, etc. if detected)
        9. Potential Challenges
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content