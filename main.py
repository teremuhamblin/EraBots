import asyncio
from core.engine import EraEngine
from modules.echo_bot import EchoBot
from modules.sample_bot import SampleBot

async def main():
    engine = EraEngine()

    # Enregistrement des bots
    engine.register(EchoBot())
    engine.register(SampleBot())

    # Simulation d'un message entrant
    incoming_message = "ping"
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
