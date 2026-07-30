---
title: Probing the Origins of Reasoning Performance: Representational Quality for Mathematical Problem-Solving in RL vs. SFT Fine-Tuned Models
url: http://arxiv.org/abs/2607.26119v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_17-42-42Z_ProbingtheOriginsofReasoningPerformance_Representa.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why reinforcement learning (RL)-trained models outperform supervised fine-tuned (SFT) models on mathematical reasoning tasks. It finds that RL models have more linearly separable representations and hierarchical layer importance, while SFT models are uniform. Additionally, token‑count variability across repeated sampling is higher in some RL models, suggesting adaptive compute allocation.

## Key Takeaways
- Linear probes show RL hidden states predict answer correctness better than SFT, indicating structured, linear representations.
- Ablation studies reveal RL models develop hierarchical architecture with deeper layers more critical, whereas SFT distributes importance uniformly.
- Token‑count variability across repeated sampling is higher in some RL models, suggesting adaptive compute allocation that may reflect stable vs under‑determined policies.

## Context
The field of large language model training has shifted toward RL for reasoning tasks, yet the internal mechanisms remain opaque. Understanding representational differences can guide more effective training pipelines and improve model reliability.

## Implications
These findings suggest that RL’s hierarchical representation design yields more robust reasoning but also introduces variability in compute allocation. Practitioners should monitor token usage patterns to assess policy stability when deploying models for critical tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26119v1)
