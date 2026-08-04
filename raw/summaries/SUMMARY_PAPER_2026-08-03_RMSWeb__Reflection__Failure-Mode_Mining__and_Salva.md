---
title: RMSWeb: Reflection, Failure-Mode Mining, and Salvage-DS for Web Agent Reinforcement Learning
url: http://arxiv.org/abs/2608.00335v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_22-57-16Z_RMSWeb_Reflection_Failure_ModeMining_andSalvage_DS.md
generated_at: 2026-08-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces RMSWeb, a three‑stage framework that improves the training of compact web agents by enhancing data collection, focusing offline reinforcement learning on failure modes, and providing a salvage mechanism for rejected groups. The method combines reflection‑conditioned retries to gather more successful trajectories, failure‑mode mining to concentrate learning on critical states, and Salvage‑DS to handle group‑relative reward issues. Experiments show that RMSWeb reduces action steps by up to 19.7% and lifts SFT scores by 2.4–7.0 points at the 8B model and 1.2–7.7 points at the 32B model.

## Key Takeaways
- Reflection‑conditioned retries increase collection yield and shorten successful trajectories, leading to fewer action steps on solved tasks.
- Failure‑mode mining concentrates offline RL on critical states exposed by the SFT policy, improving efficiency of reward updates.
- Salvage‑DS introduces an action‑semantic polarized reward, contrast‑and‑competence‑gated dynamic sampling, and an action‑only anchor to salvage rejected groups from learning.

## Context
Compact web agents are valuable for reducing deployment cost, yet their training is hampered by limited data and inefficient trajectories. This work addresses those challenges with a novel three‑part recipe that integrates offline reinforcement learning techniques tailored to the unique dynamics of web interactions.

## Implications
The results demonstrate measurable gains in both performance and efficiency, offering practitioners a practical path to train smaller models on complex web tasks without sacrificing quality. These improvements could lower costs for deployment while maintaining high accuracy across standard benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00335v1)
