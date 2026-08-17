---
title: Local and Global Regimes of Geometric Complexity in Language Model Representations
url: http://arxiv.org/abs/2608.14361v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-01-24Z_LocalandGlobalRegimesofGeometricComplexityinLangua.md
generated_at: 2026-08-16 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how lexical diversity, measured by the number of unique last tokens in a language model dataset, influences intrinsic dimensionality estimates. It discovers that at low lexical diversity fewer unique final words lead to higher ID, whereas at high lexical diversity more unique words yield higher ID, revealing a scale-dependent transition between two regimes. The authors provide an exact parameter-free formula for the reversal point.

## Key Takeaways
- At low lexical diversity conditions with fewer unique final words produce higher intrinsic dimensionality estimates than expected.
- At high lexical diversity the ordering reverses and more unique words correspond to higher ID, indicating a non‑monotonic relationship.
- The paper derives an exact parameter-free formula that predicts the reversal point across all tested scales.

## Context
Understanding intrinsic dimensionality is crucial for assessing the efficiency of language model representations. This study shows that dataset construction artifacts can obscure true complexity signals, prompting researchers to reconsider how ID is interpreted in linguistic AI systems.

## Implications
Practitioners must be cautious when using ID as a sole metric of representation quality, especially across varying data scales. The identified regimes suggest that the internal organization of LLMs may follow distinct patterns depending on lexical richness, offering new avenues for probing model manifold structures and improving interpretability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14361v1)
