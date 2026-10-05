# Copilot Instructions — EraBots v2.0
# Doctrine Quantum‑Era / Militaire‑Tech

## Mission
Copilot doit assister le développement du framework EraBots v2.0 sans modifier l’architecture
ni les composants critiques du moteur.

## Zones interdites
- Ne pas modifier core/engine.py
- Ne pas modifier core/eventbus.py
- Ne pas modifier core/session.py
- Ne pas supprimer ou fusionner des modules
- Ne pas inventer de dépendances dans requirements.txt
- Ne pas créer de fichiers hors architecture officielle

## Zones autorisées
- Création de bots dans modules/
- Création d’agents dans agents/
- Documentation, optimisation, refactor non destructif
- Ajout de tests unitaires
- Amélioration de la lisibilité et robustesse

## Style obligatoire
- PEP8 strict
- Fonctions ≤ 40 lignes
- Pas de logique cachée
- Logs structurés
- Exceptions explicites
- Commentaires doctrinaux (# [ERA], # [SEC], # [FLOW])

## Sécurité BlueSecurity v1.0
- Lecture autorisée
- Écriture dans modules/ et agents/ autorisée
- Modification core/ interdite sauf ordre humain
- Aucune commande système

## Communication
- Expliquer chaque modification
- Justifier les décisions techniques
- Proposer des alternatives
- Ne jamais modifier silencieusement

## Clause finale
Toute modification du cœur du framework nécessite un ordre explicite du Major Hamblin (Teremu).
