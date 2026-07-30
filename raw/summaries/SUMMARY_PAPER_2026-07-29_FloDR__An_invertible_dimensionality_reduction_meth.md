---
title: FloDR: An invertible dimensionality reduction method based on a normalising flow
url: http://arxiv.org/abs/2607.26278v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_21-20-52Z_FloDR_Aninvertibledimensionalityreductionmethodbas.md
generated_at: 2026-07-29 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
FloDR introduces an invertible normalising flow that creates two-dimensional embeddings while preserving the full data manifold. The method retains unused coordinates, providing exact inverse and density for diagnostics.

## Key Takeaways
- FloDR uses only the first two output coordinates to create a 2D embedding but stores all remaining coordinates, avoiding loss of information that t-SNE and UMAP discard. This preserves distances and cluster structure beyond visual density.
- The exact inverse mapping allows diagnostic visualisations computed from the true pre-image rather than approximations, enabling measurement of how much original data remains undetermined at each point.
- Two fields are evaluated: conditional spread quantifies remaining uncertainty in input units, and hidden contrast measures discarded information about labelled contrasts; both are compared to held-out data with bootstrap confidence.

## Context
In AI, dimensionality reduction often sacrifices interpretability for efficiency. FloDR addresses this by offering a lossless mapping that retains full manifold structure, making it valuable for research requiring transparent visual analysis.

## Implications
Practitioners can now assess the fidelity of embeddings and improve downstream tasks without retraining models. The method supports transparent evaluation of clustering and contrast detection in 2D visualisations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26278v1)
