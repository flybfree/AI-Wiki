---
title: FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels for Crowded and Chaotic Global South Urban Worlds
url: http://arxiv.org/abs/2608.01049v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_07-32-46Z_FactorJEPA_FactorizingMonolithicFuturesintoLayout_.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FactorJEPA, a new architecture for predicting urban dynamics in crowded Global South cities. It replaces monolithic latent representations with composable layout, entity and interaction factors using a visibility gate. Experiments show improved accuracy, causal sensitivity, robustness to occlusion across large models.

## Key Takeaways
- FactorJEPA decomposes world structure into separate subspaces for layout, entities, and interactions, preserving partially observed agents through a visibility gate.
- The method boosts future-latent L1 error reduction and maintains performance when visual evidence is masked, indicating strong robustness to occlusion.
- Results are consistent across 2B and 1B V-JEPA 2.1 backbones with high correlation (rho 0.895–0.978), showing scalable improvements.

## Context
Urban prediction models often assume clear spatial boundaries and homogeneous agents, which fail in dense environments where occlusion and social negotiation dominate. This work addresses that gap by treating world structure as a predictive primitive rather than a single latent vector.

## Implications
The factorized approach offers a more interpretable model for planners and traffic managers who need to understand specific interaction channels. Its robustness to missing data could enable real‑time deployment in chaotic urban settings where video streams are intermittently available.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01049v1)
