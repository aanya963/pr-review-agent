from agents.base_agent import BaseAgent
from services.conflict_resolver import ConflictResolver


class ConflictAgent(BaseAgent):

    def __init__(self):

        self.resolver = ConflictResolver()

    def analyze(
        self,
        filename,
        current_branch,
        incoming_branch
    ):

        self.log(
            "Resolving merge conflict..."
        )

        return self.resolver.resolve(
            filename,
            current_branch,
            incoming_branch
        )