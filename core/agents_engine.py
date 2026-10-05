from agents import Agent, Runner
from core.utils import log

class EraAgentsEngine:
    def __init__(self, name="EraAgentsEngine"):
        self.name = name
        log(f"{self.name} initialisé")

    def create_text_agent(self, instructions="You are a helpful assistant"):
        return Agent(name="EraTextAgent", instructions=instructions)

    def run_text(self, agent, message):
        log(f"Execution OpenAI Agent → {message}")
        result = Runner.run_sync(agent, message)
        return result.final_output
