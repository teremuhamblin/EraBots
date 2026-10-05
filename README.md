# 📄⚡ EraBots

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
├── core/ # Moteur interne EraBots
│   ├── engine.py # Gestion des bots, événements, pipeline
│   └── utils.py # Fonctions utilitaires
│
├── modules/ # Bots individuels
│   ├── echo_bot.py # Bot de démonstration
│   └── sample_bot.py # Exemple de bot
│
├── assets/ # Logos, images, icônes
│
├── main.py # Point d'entrée principal
├── requirements.txt # Dépendances
└── README.md # Documentation du projet
```

### 🛠️ Installation

```bash
pip install -r requirements.txt
```

### ▶️ Exécution

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
