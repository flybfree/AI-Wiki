---
title: CoRL: Co-Evolutionary Reinforcement Learning for Adaptive Indirect Prompt-Injection Attacks and Defenses
url: http://arxiv.org/abs/2609.07529v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_14-09-11Z_CoRL_Co_EvolutionaryReinforcementLearningforAdapti.md
generated_at: 2026-09-08 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoRL, a co-evolutionary reinforcement learning framework for adaptive indirect prompt injection (IPI) attacks and defenses in tool‑augmented language agents. By modeling the interaction as an asymmetric Markov game, CoRL enables attackers to evolve multi‑turn payloads while defenders learn to block them without sacrificing task utility.

## Key Takeaways
- The adversarial IPI is treated as a partially observable general‑sum Markov game where the attacker adapts payloads at tool‑return sites and the defender must preserve both safety and task completion.  
- CoRL’s bilateral Co‑PPO jointly trains attacker and defender agents using role‑specific rewards, allowing online adaptation of strategies across many execution runs.  
- Verifier‑grounded repair is mined from population failures to produce safe teacher repairs that are integrated into the defender’s SFT loop.

## Context
Tool‑augmented language agents face a growing threat of indirect prompt injection where malicious instructions hide in tool outputs, complicating static defenses. Traditional approaches assume fixed attack patterns, which often fail as attackers evolve. CoRL addresses this by treating IPI as an evolving game and using co‑evolution to keep both sides competitive.

## Implications
For practitioners, CoRL provides a scalable method to continuously adapt defenses without retraining from scratch, preserving user task utility. The framework also yields attack candidates for red‑team testing, offering a feedback loop that improves both safety and robustness in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07529v1)
