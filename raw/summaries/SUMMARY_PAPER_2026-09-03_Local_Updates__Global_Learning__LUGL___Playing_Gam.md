---
title: Local Updates, Global Learning (LUGL): Playing Games with non-incremental Learners
url: http://arxiv.org/abs/2609.03660v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_10-58-09Z_LocalUpdates_GlobalLearning_LUGL__PlayingGameswith.md
generated_at: 2026-09-03 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LUGL, a framework that lets non‑incremental learners such as LightGBM operate effectively in reinforcement learning by separating data collection from model fitting. By alternating between local updates where the agent stores tabular game information and global learning where a function approximator is trained on those updates, LUGL achieves competitive or superior performance to DQN and DeepCFR across both perfect‑information and imperfect‑information games.

## Key Takeaways
- The framework decouples data accumulation from model training, allowing tree‑based models to handle distributional shift typical of self‑play.  
- Local updates store Q‑values, V‑values, policies or regret values in a finite table before each global learning phase.  
- Experiments show LightGBM agents match or exceed neural network baselines on all tested benchmarks.

## Context
Game states are naturally tabular, making tree‑based methods a strong candidate for reinforcement learning despite their limited capacity compared to deep nets. This work highlights that the community’s preference for NNs may stem more from ease of implementation than inherent superiority in this domain.

## Implications
LUGL suggests that non‑incremental learners can be viable alternatives to neural networks, reducing reliance on large models and computational resources. Practitioners may adopt tree‑based approaches for games or structured tabular problems where interpretability and efficiency matter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03660v1)
