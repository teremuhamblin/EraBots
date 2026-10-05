from core.agents_engine import EraAgentsEngine
from core.utils import log

class OpenAIAgent:
    name = "OpenAIAgent"

    def __init__(self):
        self.engine = EraAgentsEngine()
        self.agent = self.engine.create_text_agent(
            instructions="You are a helpful assistant. Keep answers short."
        )

    async def handle(self, message):
        log(f"{self.name} reçoit : {message}")
        response = self.engine.run_text(self.agent, message)
        return response
