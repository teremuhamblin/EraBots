import numpy as np
from agents import Agent
from agents.voice import AudioInput, SingleAgentVoiceWorkflow, VoicePipeline
from core.utils import log

class VoiceAgent:
    name = "VoiceAgent"

    async def handle(self, message):
        log(f"{self.name} activation voix")

        agent = Agent(name="VoiceAssistant", instructions="You are a helpful voice assistant.")
        pipeline = VoicePipeline(workflow=SingleAgentVoiceWorkflow(agent))

        audio_input = AudioInput(buffer=np.zeros(24000 * 3, dtype=np.int16))
        result = await pipeline.run(audio_input)

        async for event in result.stream():
            if event.type == "voice_stream_event_audio":
                return "<Audio Stream>"
