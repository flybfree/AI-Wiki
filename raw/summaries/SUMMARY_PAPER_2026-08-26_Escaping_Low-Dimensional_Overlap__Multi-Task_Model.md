---
title: Escaping Low-Dimensional Overlap: Multi-Task Model Merging via High-Dimensional Sparse Disentanglement
url: http://arxiv.org/abs/2608.25354v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_04-16-31Z_EscapingLow_DimensionalOverlap_Multi_TaskModelMerg.md
generated_at: 2026-08-26 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a sparse‑representation based merging framework that uses Sparse Autoencoders to project task vectors into a high‑dimensional sparse space, allowing feature‑level disentanglement before fusion. The method also employs a lightweight Group‑Ranked Zeroth‑Order Optimizer to select critical layers for selective merging. Experiments show consistent gains over multiple training‑free merging baselines on both Qwen2.5-1.5B and Qwen2.5-7B models, with a 2.78 % improvement in the most conflicting four‑task setting.

## Key Takeaways
- The framework leverages Sparse Autoencoders to map task vectors into a high‑dimensional sparse feature space, which isolates useful task directions from superposition induced entanglement.
- A lightweight Group‑Ranked Zeroth‑Order Optimizer (GR‑ZOO) is used to identify and merge only the most critical layers, reducing computational overhead while preserving performance.
- The method achieves superior results across mathematical reasoning, code generation, instruction following, and general knowledge tasks on both Qwen2.5 models, outperforming Task Arithmetic, TIES‑Merge, DARE, Fisher‑Merge, and recent training‑free merging approaches.

## Context
Model merging is a key technique for building generalist AI systems without retraining, yet severe task interference often degrades performance due to superposition of task‑specific features. Existing decomposition methods struggle to disentangle these entangled components, limiting the practicality of training‑free fusion strategies in large language models.

## Implications
This work demonstrates that sparse feature projection combined with selective layer merging can significantly boost the effectiveness of training‑free model fusion. Practitioners and researchers can adopt this approach to create more robust generalist agents, potentially reducing inference costs while maintaining high task performance across diverse applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25354v1)
