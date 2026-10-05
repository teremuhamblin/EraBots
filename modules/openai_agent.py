class OpenAIAgent:
    name = "OpenAIAgent"

    async def handle(self, message, context=None):
        return "Recursion is a function calling itself."
