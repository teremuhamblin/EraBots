###### ~/README.md >> markdown 

# ⚡ EraBots

- v2.0

   - **Quantum‑Era Multi‑Bot Framework**

---

>⚡📄⚡ EraBots v2.0 est une refonte majeure du framework multi‑bots conçu pour l’ère moderne des systèmes distribués, IA et automatisation.  
Cette version introduit un moteur entièrement reconstruit, un EventBus interne, des sessions persistantes, un dispatch intelligent et une architecture prête pour le realtime.

---

### 🚀 Nouveautés v2.0

#### 🧠 Moteur EraEngine v2.0

```text
- Dispatch parallèle des bots  
- Handoff intelligent entre agents  
- Intégration du EventBus  
- Intégration du SessionManager  
- Architecture modulaire et extensible  
- Compatibilité OpenAI Agents
``` 

#### 📡 EventBus

- Réseau interne d’événements

```text
- Historique complet des événements  
- Émission d’événements système, bots, sessions, handoff  
- Base pour le futur Dashboard Web (v2.1)
```

### 🧬 SessionManager

- Sessions persistantes

```text
- Contexte utilisateur  
- Historique des messages  
- Mémoire courte IA  
- Préparation pour les sessions enrichies v2.1  
```

#### 🤖 Bots compatibles v2.0

>Tous les bots ont été mis à jour pour supporter :

- handle(message, context)  
- exécution parallèle  
- compatibilité EventBus  
- compatibilité sessions  

> Bots inclus :

- EchoBot  
- SampleBot  
- OpenAIAgent  
- VoiceAgent  
- SandboxBot  

#### 🧩 main.py v2.0
```text
- Intégration du moteur v2.0  
- Intégration EventBus  
- Intégration SessionManager  
- Dispatch intelligent  
- Affichage des logs EventBus  
```

### 📁 Structure du projet

```text
EraBots/
│
├── core/
│   ├── engine.py          # Moteur EraEngine v2.0
│   ├── eventbus.py        # Réseau interne d’événements
│   └── session.py         # Sessions persistantes
│
├── modules/
│   ├── echo_bot.py
│   ├── sample_bot.py
│   ├── openai_agent.py
│   ├── voice_agent.py
│   └── sandbox_agent.py
│
├── assets/
│
├── main.py
├── requirements.txt
└── README.md
```

### ▶️ Exécution

```bash
python main.py
```

### 🧩 Ajouter un bot (v2.0)

```python
class MyBot:
    name = "MyBot"

    async def handle(self, message, context=None):
        if "hello" in message.lower():
            return "Bonjour, je suis MyBot."
        return None
```

### Enregistrement dans main.py :

```python
engine.register(MyBot())
```

### ⚡ Fonctionnalités principales

```text
- Architecture multi‑bots
- Moteur EraEngine v2.0
- EventBus interne
- Sessions persistantes
- Dispatch parallèle
- Handoff intelligent
- Compatibilité OpenAI Agents
- Structure professionnelle pour GitHub
```

### 🧠 Vision EraBots

>EraBots est conçu pour :

```text
- apprendre la structure d’un framework Python
- créer plusieurs bots modulaires
- développer des systèmes automatisés
- servir de base à des projets IA / Web3 / Automation
- évoluer vers un système distribué (EraBots v3.0)
```

### 🛡️ Sécurité

```text
- Aucun accès réseau externe par défaut
- Isolation des modules bots
- Sessions sandboxées
- Logs internes non exposés
- Aucun stockage permanent
```

### 📜 Licence

>Projet personnel

- Écosystème PYTHON‑Learning

### 🟪 Roadmap

>v2.1 — Dashboard Web
- Interface web
- Monitoring en temps réel
- Logs EventBus
- Envoi de messages via navigateur

>v3.0 — Mesh Distributed Bots
- Multi‑nœuds EraBots
- Bots distribués
- Résilience automatique
- Synchronisation réseau

---

### 📜 CHANGELOG (Résumé)

>v2.0
- Nouveau moteur EraEngine v2.0  
- EventBus ajouté  
- Sessions persistantes  
- Dispatch parallèle  
- Handoff intelligent  
- Architecture Realtime‑Ready  
- Mise à jour complète des bots  
- Documentation v2.0 ajoutée  

---
