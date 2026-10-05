import asyncio
from openai import OpenAI


class AgentsEngineV2:
    """
    Moteur OpenAI Agents pour EraBots v2.0
    - Compatible EventBus
    - Compatible SessionManager
    - Dispatch parallèle
    - Handoff intelligent
    - Gestion des sessions OpenAI
    """

    def __init__(self, eventbus=None, sessions=None):
        self.client = OpenAI()
        self.eventbus = eventbus
        self.sessions = sessions
        self.agents = {}

    # ---------------------------------------------------------
    # 1. Enregistrement des agents OpenAI
    # ---------------------------------------------------------
    def register(self, name, agent_id):
        self.agents[name] = agent_id
        if self.eventbus:
            self.eventbus.emit("agent.registered", {
                "agent": name,
                "agent_id": agent_id
            })

    # ---------------------------------------------------------
    # 2. Création d'une session OpenAI
    # ---------------------------------------------------------
    def create_session(self, agent_name):
        agent_id = self.agents.get(agent_name)
        if not agent_id:
            raise ValueError(f"Agent {agent_name} non enregistré.")

        session = self.client.agents.sessions.create(agent_id=agent_id)

        if self.eventbus:
            self.eventbus.emit("agent.session.created", {
                "agent": agent_name,
                "session_id": session.id
            })

        return session.id

    # ---------------------------------------------------------
    # 3. Envoi d'un message à un agent OpenAI
    # ---------------------------------------------------------
    async def send(self, agent_name, session_id, message):
        agent_id = self.agents.get(agent_name)
        if not agent_id:
            return None

        if self.eventbus:
            self.eventbus.emit("agent.message.sent", {
                "agent": agent_name,
                "session_id": session_id,
                "message": message
            })

        response = self.client.agents.messages.create(
            agent_id=agent_id,
            session_id=session_id,
            messages=[{"role": "user", "content": message}]
        )

        result = response.output[0].content[0].text

        if self.eventbus:
            self.eventbus.emit("agent.response.received", {
                "agent": agent_name,
                "response": result
            })

        return result

    # ---------------------------------------------------------
    # 4. Dispatch multi‑agents OpenAI (parallèle)
    # ---------------------------------------------------------
    async def dispatch(self, message, session_id=None):
        if self.eventbus:
            self.eventbus.emit("agent.dispatch.start", {
                "message": message
            })

        # Création de session si nécessaire
        if session_id is None:
            session_id = self.create_session("default")

        tasks = [
            asyncio.create_task(self.send(agent_name, session_id, message))
            for agent_name in self.agents
        ]

        results = await asyncio.gather(*tasks)

        responses = {
            agent_name: result
            for agent_name, result in zip(self.agents.keys(), results)
            if result
        }

        # Handoff intelligent
        if "text-agent" in responses and "voice-agent" in self.agents:
            if self.eventbus:
                self.eventbus.emit("agent.handoff.triggered", {
                    "from": "text-agent",
                    "to": "voice-agent"
                })

        return responses
