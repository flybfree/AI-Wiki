---
title: Beyond a Bag of Features: Set-Level Instability in Sparse Autoencoders
url: http://arxiv.org/abs/2608.11197v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_17-55-59Z_BeyondaBagofFeatures_Set_LevelInstabilityinSparseA.md
generated_at: 2026-08-11 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper revisits the analysis of LLM representations using sparse autoencoder latent sets to measure similarity, finding that these set-level measures do not align with human-perceived category boundaries or typicality. It shows SAE activation sets track internal model structure rather than semantic composition and mismatches human judgments under controlled modifications.

## Key Takeaways
- SAE latent sets can recover union-like compositional structure in toy models but fail to capture fine-grained typicality in natural text.
- Human category boundaries are not faithfully recovered by SAE active sets, unlike dense embeddings or residual-stream states.
- The mismatch between human conceptual change judgments and changes in SAE active sets indicates non‑bag‑of‑features composition.

## Context
LLM representations are often evaluated with dense cosine similarity, which obscures the underlying sparse feature space. Sparse autoencoders offer a more interpretable latent representation but their set-level semantics remain unclear. This work bridges that gap by comparing SAE active sets to human judgments in controlled settings.

## Implications
For practitioners relying on LLM embeddings, this suggests caution against assuming simple compositional semantics. It highlights the need for richer similarity metrics and deeper understanding of sparse feature spaces before deploying models where fine-grained typicality matters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11197v1)
