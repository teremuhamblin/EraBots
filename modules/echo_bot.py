from core.utils import log

class EchoBot:
    name = "EchoBot"

    async def handle(self, message):
        log(f"{self.name} a reçu : {message}")
        return f"Echo: {message}"
