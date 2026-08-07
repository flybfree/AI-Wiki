---
title: Recursive Synthesis for Long-Horizon Terminal Tasks
url: http://arxiv.org/abs/2608.05466v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_23-24-26Z_RecursiveSynthesisforLong_HorizonTerminalTasks.md
generated_at: 2026-08-06 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RST, a recursive framework that creates long-horizon terminal tasks at low cost by extending verified seeds and revalidating them. Across fifteen rounds it produces 37,484 tasks with a median reference solution of 374 lines and DeepSeek-V4-Pro accuracy dropping to 2.5%. Fine‑tuning on rejection samples raises Qwen models’ scores by up to ten points.

## Key Takeaways
- RST achieves near‑zero per‑task cost (≈$0.05) while maintaining strict consistency between instruction, environment, solution and verifier.
- The difficulty of tasks grows dramatically: reference solutions increase from 67 to 374 lines and command counts rise from 40 to 244, yet synthesis yield stays stable.
- Model performance improves significantly after fine‑tuning on synthetic trajectories, with Qwen3.5‑27B gaining up to ten points across benchmarks.

## Context
Generating high‑quality terminal tasks remains a bottleneck for training long‑horizon agents because manual authoring is costly and fragile. RST’s automated synthesis addresses this scalability issue by reusing validated seeds and continuously increasing task complexity without human intervention.

## Implications
For researchers, RST offers a repeatable pipeline that can be extended indefinitely to produce ever harder tasks, supporting continual improvement of agentic models. For industry, the low cost enables rapid iteration in reinforcement‑learning pipelines without prohibitive human effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05466v1)
