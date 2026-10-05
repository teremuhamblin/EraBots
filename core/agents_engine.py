import asyncio

class EraEngine:
    def __init__(self, eventbus=None, sessions=None):
        self.bots = []
        self.eventbus = eventbus
        self.sessions = sessions

    def register(self, bot):
        self.bots.append(bot)
        if self.eventbus:
            self.eventbus.emit("bot.registered", {"bot": bot.name})

    async def dispatch(self, message, session_id=None):
        if self.eventbus:
            self.eventbus.emit("message.received", {"message": message})

        # Session context
        context = None
        if self.sessions:
            context = self.sessions.get_context(session_id)
            self.sessions.add_message(session_id, message)

        responses = {}

        # Parallel execution
        tasks = [
            asyncio.create_task(bot.handle(message, context=context))
            for bot in self.bots
        ]

        results = await asyncio.gather(*tasks)

        for bot, result in zip(self.bots, results):
            if result:
                responses[bot.name] = result
                if self.eventbus:
                    self.eventbus.emit("bot.response.generated", {
                        "bot": bot.name,
                        "response": result
                    })

        # Handoff intelligent
        if "OpenAIAgent" in responses:
            if self.eventbus:
                self.eventbus.emit("handoff.triggered", {
                    "from": "OpenAIAgent",
                    "to": "VoiceAgent"
                })

        return responses
