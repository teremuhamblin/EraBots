import asyncio
from core.engine import EraEngine
from core.eventbus import EventBus
from core.session import SessionManager

from modules.echo_bot import EchoBot
from modules.sample_bot import SampleBot
from modules.openai_agent import OpenAIAgent
from modules.voice_agent import VoiceAgent
from modules.sandbox_agent import SandboxBot


async def main():

    # --- EraBots v2.0 Core Systems ---
    eventbus = EventBus()                    # Système d’événements interne
    sessions = SessionManager()              # Sessions persistantes
    engine = EraEngine(eventbus=eventbus, sessions=sessions)

    # --- Enregistrement des bots ---
    engine.register(EchoBot())
    engine.register(SampleBot())
    engine.register(OpenAIAgent())
    engine.register(VoiceAgent())
    engine.register(SandboxBot())

    # --- Message entrant ---
    incoming_message = "Explain recursion in one sentence."
    print(f"\n📩 Message reçu : {incoming_message}")

    # --- Session persistante ---
    session_id = sessions.start_session("default-user")

    # --- Dispatch multi-bots + handoff intelligent ---
    responses = await engine.dispatch(incoming_message, session_id=session_id)

    # --- Affichage ---
    print("\n🤖 Réponses générées :")
    for bot_name, result in responses.items():
        print(f"{bot_name} → {result}")

    # --- Logs EventBus ---
    print("\n📡 EventBus Logs :")
    for event in eventbus.history:
        print(f"- {event}")


if __name__ == "__main__":
    asyncio.run(main())
