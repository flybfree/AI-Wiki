---
title: IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment
url: http://arxiv.org/abs/2607.25579v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-05-46Z_IRIS_ReusableIdentityRepresentationsfromFrozenLLMs.md
generated_at: 2026-07-28 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces IRIS, a training‑free framework that creates stable internal representations for entities using frozen large language models. By extracting identity‑oriented contextual embeddings, IRIS builds iris‑like signatures that enable direct similarity comparison across knowledge graphs without relying on pair‑specific processing or candidate inference.

## Key Takeaways
- IRIS leverages the latent state of a frozen LLM to produce reusable entity signatures rather than generating new text each time.  
- The framework constructs a shared identity space, allowing entities from different KGs to be aligned via simple similarity metrics.  
- Experiments on four benchmark datasets show Hits@1 scores ranging from 97.99 to 100.00 with two frozen LLM backbones.

## Context
Entity alignment remains challenging because textual descriptions vary across knowledge graphs, and most LLM‑based methods treat each pair or candidate set separately. This work highlights the potential of static model representations to reduce computational overhead while improving semantic robustness in EA tasks.

## Implications
For industry practitioners, IRIS offers a scalable solution that can be deployed once per entity type, lowering latency for large‑scale KG integration. Researchers gain a template for extracting reusable embeddings from frozen models, encouraging further work on stable, pair‑independent alignment methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25579v1)
