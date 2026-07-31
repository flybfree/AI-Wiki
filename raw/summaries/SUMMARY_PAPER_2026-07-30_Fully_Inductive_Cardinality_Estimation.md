---
title: Fully Inductive Cardinality Estimation
url: http://arxiv.org/abs/2607.28311v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-46-43Z_FullyInductiveCardinalityEstimation.md
generated_at: 2026-07-30 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FICE, a fully inductive learned cardinality estimator for Basic Graph Patterns queries over Knowledge Graphs that works on unseen graphs without retraining. It achieves lower median q-error than previous methods and improves tail behavior.

## Key Takeaways
- The encoder GNN operates on a factor-graph view of the KG to produce entity and relation embeddings, proving BGP cardinality is a local function of the 2‑hop neighborhood around bound terms.
- A decoder GNN composes these embeddings along the query join topology to predict log‑cardinality, with encoder and decoder trained jointly for specialization.
- FICE scales to millions of triples using neighborhood sampling, decouples embedding generation from decoding, and delivers sub‑millisecond latency.

## Context
Learned cardinality estimators have dominated recent research but are limited by transductive nature requiring retraining. This work addresses the gap by providing a truly inductive model that generalizes to unseen graphs, aligning with the trend toward robust, deployment‑ready AI systems.

## Implications
For industry practitioners, FICE enables accurate query responses in real‑time triplestores without costly retraining pipelines, supporting large‑scale knowledge bases. Practitioners can rely on fast, low‑error estimates that improve user experience and reduce operational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28311v1)
