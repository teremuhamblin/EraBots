import asyncio
from core.engine import EraEngine
from modules.echo_bot import EchoBot
from modules.sample_bot import SampleBot
from modules.openai_agent import OpenAIAgent
from modules.voice_agent import VoiceAgent
from modules.sandbox_agent import SandboxBot

async def main():
    engine = EraEngine()

    engine.register(EchoBot())
    engine.register(SampleBot())
    engine.register(OpenAIAgent())
    engine.register(VoiceAgent())
    engine.register(SandboxBot())

    incoming_message = "Explain recursion in one sentence."
    print(f"Message reçu : {incoming_message}")

    responses = []
    for bot in engine.bots:
        result = await bot.handle(incoming_message)
        if result:
            responses.append(f"{bot.name} → {result}")

    print("\nRéponses générées :")
    for r in responses:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
