from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.entries import GitRepo
from agents.sandbox.sandboxes import UnixLocalSandboxClient
from core.utils import log

class SandboxBot:
    name = "SandboxBot"

    async def handle(self, message):
        log(f"{self.name} sandbox → {message}")

        agent = SandboxAgent(
            name="SandboxAssistant",
            instructions="Inspect the workspace before answering.",
            default_manifest=Manifest(
                entries={"repo": GitRepo(repo="openai/openai-agents-python", ref="main")}
            ),
        )

        result = Runner.run_sync(
            agent,
            message,
            run_config=RunConfig(sandbox=SandboxRunConfig(client=UnixLocalSandboxClient())),
        )

        return result.final_output
