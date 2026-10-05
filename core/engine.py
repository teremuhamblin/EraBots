import asyncio


class EraEngine:
    """
    EraEngine v2.0 — Quantum‑Era Multi‑Bot Engine
    ------------------------------------------------
    - Dispatch parallèle
    - Handoff intelligent
    - EventBus intégré
    - Sessions persistantes
    - Contexte utilisateur
    - Architecture modulaire
    """

    def __init__(self, eventbus=None, sessions=None):
        self.bots = []
        self.eventbus = eventbus
        self.sessions = sessions

        if self.eventbus:
            self.eventbus.emit("engine.initialized", {
                "version": "2.0",
                "status": "ready"
            })

    # ---------------------------------------------------------
    # 1. Enregistrement des bots
    # ---------------------------------------------------------
    def register(self, bot):
        self.bots.append(bot)

        if self.eventbus:
            self.eventbus.emit("bot.registered", {
                "bot": bot.name
            })

    # ---------------------------------------------------------
    # 2. Dispatch v2.0 — exécution parallèle + sessions
    # ---------------------------------------------------------
    async def dispatch(self, message, session_id=None):
        if self.eventbus:
            self.eventbus.emit("engine.dispatch.start", {
                "message": message
            })

        # Récupération du contexte de session
        context = None
        if self.sessions:
            context = self.sessions.get_context(session_id)
            self.sessions.add_message(session_id, message)

        # Exécution parallèle des bots
        tasks = [
            asyncio.create_task(bot.handle(message, context=context))
            for bot in self.bots
        ]

        results = await asyncio.gather(*tasks)

        responses = {}
        for bot, result in zip(self.bots, results):
            if result:
                responses[bot.name] = result

                if self.eventbus:
                    self.eventbus.emit("bot.response.generated", {
                        "bot": bot.name,
                        "response": result
                    })

        # -----------------------------------------------------
        # 3. Handoff intelligent (exemple simple)
        # -----------------------------------------------------
        if "OpenAIAgent" in responses and "VoiceAgent" in responses:
            if self.eventbus:
                self.eventbus.emit("handoff.triggered", {
                    "from": "OpenAIAgent",
                    "to": "VoiceAgent"
                })

        if self.eventbus:
            self.eventbus.emit("engine.dispatch.end", {
                "responses": list(responses.keys())
            })

        return responses
