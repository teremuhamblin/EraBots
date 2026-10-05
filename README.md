# 📄⚡ EraBots

[![Dependency Graph](https://github.com/teremuhamblin/EraBots/actions/workflows/dependabot/update-graph/badge.svg)](https://github.com/teremuhamblin/EraBots/actions/workflows/dependabot/update-graph)

- Multi‑Bot Quantum‑Era Framework

>EraBots est un framework léger permettant de créer, assembler et exécuter plusieurs bots simultanément.  
- Il s’agit d’un projet modulaire, extensible, et conçu pour l’ère moderne des systèmes distribués.

### 🚀 Fonctionnalités principales

```text
- Architecture multi‑bots  
- Moteur central EraEngine  
- Modules bots indépendants  
- Extensible (IA, NLP, Web3, automatisation)  
- Structure professionnelle pour GitHub
```

### 📁 Structure du projet

```text
EraBots/
│
├── core/
│   ├── engine.py               # Moteur multi-bots
│   ├── agents_engine.py        # Nouveau moteur OpenAI Agents
│   └── utils.py
│
├── modules/
│   ├── echo_bot.py
│   ├── sample_bot.py
│   ├── openai_agent.py         # Agent text complet
│   ├── voice_agent.py          # Agent voix
│   └── sandbox_agent.py        # Agent sandbox
│
├── assets/
│
├── main.py
├── requirements.txt
└── README.md
```

### 🛠️ Installation

```bash
pip install -r requirements.txt
```

### ▶️ Exécution

```bash
python main.py
```

### ⚡ EraBots Agents Integration

- EraBots v1.5 intègre désormais le SDK **OpenAI Agents**, permettant :

```text
- Agents textuels
- Agents sandbox
- Agents voix
- Agents realtime
- Handoffs entre bots
- Guardrails
- Sessions persistantes
- Tracing complet
```

### Modules disponibles

```text
- `openai_agent.py` → Agent textuel OpenAI
- `voice_agent.py` → Agent voix
- `sandbox_agent.py` → Agent workspace
- `agents_engine.py` → Moteur OpenAI Agents
```

### Exécution

```bash
python main.py
```

### 🧩 Ajouter un nouveau bot

- Créer un fichier dans modules/ :

```python
class MyBot:
    name = "MyBot"

    async def handle(self, message):
        if message == "hello":
            return "Bonjour !"
        return None
```

- Puis l’enregistrer dans main.py :

```python
engine.register(MyBot())
```

### 🎯 Objectif

- EraBots est conçu pour :

```text
- apprendre la structure d’un framework Python  
- créer plusieurs bots modulaires  
- développer des systèmes automatisés  
- servir de base à des projets IA / Web3 / Automation
```

### 📜 Licence
- Projet personnel
- Intégré à l’écosystème PYTHON

---
