---
title: IDEEA: training-free Input-Dependent stEEring via Activation cluster matching
url: http://arxiv.org/abs/2609.02089v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_04-28-39Z_IDEEA_training_freeInput_DependentstEEringviaActiv.md
generated_at: 2026-09-02 20:52
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IDEEA, a training‑free steering method that makes the alignment of large language models input‑dependent. By clustering activation supports per attention head and solving an optimal matching problem, IDEEA creates cluster‑conditional directions for each concept while keeping the original input representation unchanged. On TruthfulQA it boosts the truth × info rate by up to 23.5% over the best input‑independent baseline.

## Key Takeaways
- IDEEA clusters positive and negative activation supports per attention head, enabling input‑specific steering directions that match the model’s own activations for a given concept.  
- The framework solves an optimal‑matching problem to generate a set of cluster‑conditional directions, preserving the original representation while aligning toward the target concept.  
- IDEEA improves the truth × info rate in TruthfulQA by an average of 9.9% and can reach as high as 23.5%, outperforming all input‑independent baselines.

## Context
Current steering methods rely on a single global bias, which cannot adapt to different inputs occupying distinct activation regions. This limitation hampers the ability to steer models accurately across varied queries without retraining or weight updates. IDEEA addresses this by leveraging local representation clusters within each attention head.

## Implications
For practitioners, IDEEA offers a lightweight, inference‑only solution that can be deployed immediately after model deployment. It reduces reliance on costly fine‑tuning pipelines and enables more nuanced alignment across diverse user inputs, fostering trustworthy AI systems in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02089v1)
