class EchoBot:
    name = "EchoBot"

    async def handle(self, message, context=None):
        return f"Echo: {message}"
