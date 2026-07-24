---
title: Sample-Efficient Learning from Agent Experience
url: http://arxiv.org/abs/2607.21051v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_08-34-31Z_Sample_EfficientLearningfromAgentExperience.md
generated_at: 2026-07-23 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Experience Distillation to retain in‑context learning gains without requiring additional environment interactions. Experiments show it retains at least 64.8% of the benefits from in‑context learning while supervised fine‑tuning only recovers 3.8%, and matches RL baselines with roughly nine times fewer samples. The approach demonstrates that preserving contextual knowledge internally can reduce reliance on costly external feedback.

## Key Takeaways
- The method retains at least 64.8% of the gains from in‑context learning across software‑engineering tasks and text‑adventure games.
- Direct supervised fine‑tuning on collected experience recovers only 3.8%, highlighting inefficiency.
- Experience Distillation matches RL baselines with at least 9.6× fewer environment samples.
- The experiments were conducted on a curated set of 749 software‑engineering tasks and six text‑adventure games.

## Context
This work addresses the challenge of preserving contextual knowledge in agent learning when interactions cannot be repeated, aligning with trends toward sample‑efficient and context‑aware AI models. It contributes to the broader effort of minimizing costly simulation or human feedback loops while maintaining performance.

## Implications
For practitioners, the approach reduces expensive environment interaction cycles, enabling rapid deployment of learned policies from limited data. It also suggests that internalizing experience into model weights can outperform traditional fine‑tuning in resource‑constrained settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21051v1)
