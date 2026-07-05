from agents.base_agent import BaseAgent
from services.conflict_resolver import ConflictResolver


class ConflictAgent(BaseAgent):

    def __init__(self):

        self.resolver = ConflictResolver()

    def analyze(
        self,
        filename,
        current_code,
        incoming_code
    ):

        self.log("Resolving Merge Conflict...")

        return self.resolver.resolve(
            filename,
            current_code,
            incoming_code
        )