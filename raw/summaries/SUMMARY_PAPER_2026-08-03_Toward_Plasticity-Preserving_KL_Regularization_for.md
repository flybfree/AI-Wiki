---
title: Toward Plasticity-Preserving KL Regularization for Capability Retention in LLM Reinforcement Learning
url: http://arxiv.org/abs/2608.01743v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_06-10-33Z_TowardPlasticity_PreservingKLRegularizationforCapa.md
generated_at: 2026-08-03 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CoKL, a conditional KL regularization method designed to preserve the capabilities of large language models during reinforcement learning fine‑tuning while minimizing interference with new task learning. By restricting the regularization constraint to response distributions that are conditioned on correctness rather than the full output distribution, CoKL achieves better balance between retaining prior knowledge and improving target performance.

## Key Takeaways
- The proposed CoKL narrows the KL regularization from the entire policy to only those responses that are correct under a reference model, reducing unnecessary restriction of exploration.  
- At the population level, CoKL decouples the total probability assigned to correct answers from their conditional distribution, allowing flexible allocation among reference‑supported correct responses without anchoring incorrect outputs or total correctness mass.  
- Experiments show that full‑policy KL regularization forces an optimal correctness gap even with imperfect references, whereas CoKL avoids this limitation and yields higher task improvement alongside better prior retention.

## Context
LLM post‑training fine‑tuning often suffers from catastrophic forgetting when new objectives are optimized, prompting the use of regularization techniques like KL divergence to keep models close to their original capabilities. Standard full‑policy KL constraints can overly limit learning dynamics, highlighting a need for more nuanced approaches that preserve both task performance and prior knowledge.

## Implications
For practitioners, CoKL offers a practical framework that can be integrated into RL pipelines without sacrificing exploration or causing excessive regularization pressure. This method supports continual deployment of LLMs across diverse tasks while maintaining robust capability retention, aligning with industry goals for reliable, adaptable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01743v1)
