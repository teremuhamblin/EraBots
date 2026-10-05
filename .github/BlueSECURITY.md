`
SECURITY.md
`

---

🛡️ SECURITY.md — EraBots v2.0 / BlueSecurity v1.0
> Doctrine de sécurité, protocoles de durcissement et procédures de réponse pour le framework EraBots v2.0.  
> Version : BlueSecurity v1.0 — Quantum‑Era Defense Protocol

---

🧩 1. Présentation

EraBots v2.0 intègre un système de sécurité interne nommé BlueSecurity v1.0, conçu pour :

- protéger l’architecture multi‑bots,  
- sécuriser les communications EventBus,  
- garantir l’intégrité des sessions,  
- prévenir les comportements IA non conformes,  
- assurer la résilience du framework dans un environnement hostile.

Ce document définit les protocoles de sécurité, les bonnes pratiques, les procédures de signalement, et les règles de durcissement applicables à tout contributeur ou utilisateur du framework.

---

🛡️ 2. Principes fondamentaux BlueSecurity v1.0

🔒 2.1 Confidentialité
- Aucun secret ne doit être stocké dans le code.  
- Utilisation obligatoire de variables d’environnement.  
- Interdiction de commit de clés API, tokens, credentials.

🧬 2.2 Intégrité
- Toute modification du moteur (Engine v2.0) doit être revue.  
- Les bots IA doivent respecter les règles AGENTS.md.  
- Les modules critiques doivent être couverts par des tests.

🛡️ 2.3 Résilience
- Le système doit continuer à fonctionner même en cas de défaillance d’un bot.  
- EventBus v2.0 doit isoler les erreurs et empêcher la propagation.  
- SessionManager v2.0 doit protéger les sessions contre les corruptions.

---

🔧 3. Modules critiques à surveiller

Les composants suivants sont considérés comme sensibles :

- Engine v2.0 — cœur du framework  
- EventBus v2.0 — communication interne  
- SessionManager v2.0 — gestion des sessions  
- AgentsEngineV2 — intégration OpenAI Agents SDK  
- Bots IA — text, voice, sandbox, realtime  
- security_bot.py — BlueSecurity B1 → B9  
- Config.yaml — configuration globale

Toute anomalie dans ces modules doit être traitée comme potentiellement critique.

---

🧨 4. Types de vulnérabilités surveillées

🔥 4.1 Vulnérabilités IA
- réponses non conformes,  
- hallucinations dangereuses,  
- exécution sandbox non contrôlée,  
- escalade de permissions entre bots.

🔥 4.2 Vulnérabilités système
- injection dans EventBus,  
- corruption de session,  
- accès non autorisé à des modules internes,  
- contournement des règles BlueSecurity.

🔥 4.3 Vulnérabilités code
- absence de validation d’entrée,  
- mauvaise gestion des exceptions,  
- dépendances obsolètes ou vulnérables,  
- absence de tests sur les modules critiques.

---

🛠️ 5. Procédure de signalement

Pour signaler une faille de sécurité :

1. Ne pas créer d’issue publique.  
2. Utiliser le template dédié :  
   `
   .github/ISSUETEMPLATE/securityreport.yml
   `
3. Fournir :
   - description détaillée,  
   - étapes de reproduction,  
   - logs, captures, preuves,  
   - impact potentiel,  
   - proposition de mitigation.

4. Le rapport sera traité selon le protocole BlueSecurity v1.0.

---

🧪 6. Tests de sécurité obligatoires

Chaque PR modifiant un module critique doit inclure :

- tests unitaires,  
- tests d’intégration multi‑bots,  
- tests EventBus (routing, broadcast, isolation),  
- tests de sessions persistantes,  
- tests AgentsEngineV2 (OpenAI Agents SDK),  
- tests de résistance (erreurs, timeouts, exceptions).

---

🧱 7. Durcissement du framework (Hardening)

🔐 7.1 Engine v2.0
- validation stricte des messages,  
- isolation des erreurs,  
- logs structurés.

📡 7.2 EventBus v2.0
- interdiction des messages non typés,  
- contrôle des topics,  
- protection contre les injections.

🧬 7.3 SessionManager v2.0
- expiration automatique,  
- protection contre les collisions,  
- isolation des contextes.

🤖 7.4 Bots IA
- sandbox obligatoire pour les bots sensibles,  
- interdiction d’accès direct aux modules internes,  
- respect strict des règles AGENTS.md.

---

🛡️ 8. Politique de divulgation

EraBots suit une politique de divulgation responsable :

- les failles ne doivent pas être rendues publiques avant correction,  
- les contributeurs doivent utiliser le canal sécurisé,  
- les correctifs doivent être testés et validés avant publication.

---

🧠 9. Contact sécurité

Pour toute question ou rapport confidentiel :

`
Maintainer : Teremu
Canal : Issue Template Security Report
Protocole : BlueSecurity v1.0
`

---

🟦 10. Version

- BlueSecurity v1.0 — Quantum‑Era Defense Protocol  
- Compatible EraBots v2.0  
- Mise à jour : 05/10/2026

---
