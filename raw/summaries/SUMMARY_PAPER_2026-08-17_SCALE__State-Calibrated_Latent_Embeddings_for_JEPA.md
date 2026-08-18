---
title: SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry
url: http://arxiv.org/abs/2608.16287v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_08-58-55Z_SCALE_State_CalibratedLatentEmbeddingsforJEPAPlann.md
generated_at: 2026-08-17 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SCALE, a lightweight regularization technique that aligns the latent geometry of end‑to‑end learned world models with task‑relevant state space distances without altering the model’s encoder. Experiments across five tasks, three planners and varying compute budgets show SCALE consistently outperforms LeWM, while maintaining comparable or better decodability of states.

## Key Takeaways
- SCALE correlates sampled latent pairwise distances with standardized task‑relevant state distances to create a favorable geometric structure for Euclidean planning.
- The regularizer is applied only during training and adds no overhead at inference time, preserving the original LeWM encoder.
- Although full‑embedding decodability remains high, SCALE’s alignment yields more consistent planning gains across all evaluated scenarios.

## Context
The field of joint‑embedding predictive world models seeks representations that balance state fidelity with low variance for efficient planning. Recent work shows that geometric properties can be as important as raw content, yet few methods systematically adjust the latent space to match task needs without full retraining.

## Implications
Practitioners can adopt SCALE to improve planner performance on existing models with minimal effort, highlighting geometry‑aware training as a practical lever for better planning outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16287v1)
