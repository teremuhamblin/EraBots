class EraEngine:
    def __init__(self):
        self.bots = []

    def register(self, bot):
        self.bots.append(bot)

    async def dispatch(self, message):
        for bot in self.bots:
            await bot.handle(message)
