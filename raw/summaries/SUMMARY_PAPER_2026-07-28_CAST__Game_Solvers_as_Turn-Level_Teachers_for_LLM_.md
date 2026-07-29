---
title: CAST: Game Solvers as Turn-Level Teachers for LLM Agents
url: http://arxiv.org/abs/2607.25308v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_05-39-01Z_CAST_GameSolversasTurn_LevelTeachersforLLMAgents.md
generated_at: 2026-07-28 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAST, a method that uses game solvers to generate turn‑level credit signals for reinforcement learning with verifiable rewards in long‑horizon games. Experiments on Sokoban, Minesweeper and Rush Hour show that CAST outperforms all trained baselines both in‑domain and zero‑shot across diverse test suites.

## Key Takeaways
- CAST converts changes in a solver’s state value into scalar advantages that serve as turn‑level credit signals for RLVR.  
- Under a soft‑optimal solver assumption, maximizing these advantages is equivalent to on‑policy distillation from the solver without needing teacher logits.  
- The approach achieves the highest average zero‑shot performance across ALFWorld and WebShop compared with other methods.

## Context
Long‑horizon reinforcement learning struggles because rewards are sparse, obscuring which actions matter. Game solvers provide dense state information that can be leveraged to improve credit assignment, a challenge central to building generalist decision‑making agents.

## Implications
CAST offers a scalable way to enrich RLVR with interpretable turn‑level signals, potentially boosting performance on unseen games and reducing reliance on high‑quality teacher models. Practitioners may adopt this technique to develop more robust AI agents for complex interactive environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25308v1)
