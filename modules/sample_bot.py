from core.utils import log

class SampleBot:
    name = "SampleBot"

    async def handle(self, message):
        if message.lower() == "ping":
            return "Pong!"
        return None
