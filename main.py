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
    eventbus = EventBus()
    sessions = SessionManager()
    engine = EraEngine(eventbus=eventbus, sessions=sessions)

    engine.register(EchoBot())
    engine.register(SampleBot())
    engine.register(OpenAIAgent())
    engine.register(VoiceAgent())
    engine.register(SandboxBot())

    incoming_message = "Explain recursion in one sentence."
    print(f"\n📩 Message reçu : {incoming_message}")

    session_id = sessions.start_session("default-user")

    responses = await engine.dispatch(incoming_message, session_id=session_id)

    print("\n🤖 Réponses générées :")
    for bot_name, result in responses.items():
        print(f"{bot_name} → {result}")

    print("\n📡 EventBus Logs :")
    for event in eventbus.history:
        print(f"- {event}")

if __name__ == "__main__":
    asyncio.run(main())
