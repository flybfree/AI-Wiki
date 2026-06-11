---
title: Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in Sparse Autoencoders
url: http://arxiv.org/abs/2606.12138v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_14-32-57Z_UnstableFeatures_ReproducibleSubspaces_Understandi.md
generated_at: 2026-06-11 10:56
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how seed dependence affects sparse autoencoder (SAE) feature stability, defining a per‑feature signal that measures the likelihood of similar features reappearing in independent training runs. The study reveals that stable features dominate reconstruction and prediction signals while unstable ones are weak and driven by low‑frequency activation patterns.

## Key Takeaways
- Stable features carry most of the reconstruction‑ and prediction‑relevant signal, whereas unstable features have only marginal impact and are dominated by surface‑form triggers in both activation statistics and automatic explanations.  
- Geometrically, unstable features are individually non‑reproducible but concentrate within reproducible lower‑rank subspaces, indicating seed dependence reflects basis ambiguity rather than pure noise.  
- Pooling unique cross‑seed features yields more stable SAEs while preserving explained variance, showing that low‑rank ground‑truth features can be recovered at the subspace level even when individual latents differ across seeds.

## Context
Understanding feature stability is crucial for reproducible AI research and practical deployment where consistent model behavior across runs matters. This work bridges interpretability theory with large‑scale empirical analysis of neural network representations.

## Implications
For practitioners, identifying stable features can guide regularization strategies that improve consistency without sacrificing performance. Researchers should consider subspace‑level explanations when evaluating SAE outputs to avoid misinterpreting seed‑dependent noise as instability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12138v1)
