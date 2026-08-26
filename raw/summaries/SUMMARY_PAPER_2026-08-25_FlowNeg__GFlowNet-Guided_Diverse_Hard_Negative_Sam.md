---
title: FlowNeg: GFlowNet-Guided Diverse Hard Negative Sampling for Knowledge Graph Embedding
url: http://arxiv.org/abs/2608.23849v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_21-38-34Z_FlowNeg_GFlowNet_GuidedDiverseHardNegativeSampling.md
generated_at: 2026-08-25 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FlowNeg, a hierarchical generative flow network that selects diverse hard negatives for knowledge graph embedding models. It improves mean MRR by 0.0172 over EMU and IF‑NS across benchmarks. The method balances model-based hardness with structural similarity without normalizing rewards.

## Key Takeaways
- FlowNeg generates negative triples using a type‑compatible support that amortizes reward proportionality, avoiding uniform sampling pitfalls.
- It combines bounded terminal reward with a training‑only structural score to penalize collisions between held‑out positives and generated negatives.
- Experiments show higher mean MRR (+0.0172) than EMU (+0.0160) on a five‑seed grid, confirming mode‑covering diversity.

## Context
Knowledge graph embeddings rely heavily on negative sampling to guide learning; poor negatives can degrade performance or waste compute. Traditional methods either produce uniform negatives that lack challenge or hard negatives that overfit to few entities, limiting scalability and robustness in large datasets.

## Implications
Practitioners can adopt FlowNeg’s hierarchical flow approach to generate richer counterexamples without sacrificing diversity, leading to more reliable embeddings for downstream tasks. The method also reduces reliance on external similarity oracles, simplifying deployment in resource‑constrained settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23849v1)
