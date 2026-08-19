---
title: DEPT: Document Embedding Preservation Tuning for Unified Query Expansion and Retrieval
url: http://arxiv.org/abs/2608.17632v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_10-52-08Z_DEPT_DocumentEmbeddingPreservationTuningforUnified.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Document Embedding Preservation Tuning (DEPT) to address the moving‑target problem in unified query expansion and retrieval using a single decoder‑only LLM. By preserving document embeddings while allowing the generator to adapt via straight‑through gradients, DEPT improves average retrieval quality over previous baselines.

## Key Takeaways
- The unified end‑to‑end training creates a moving‑target problem where retrieval supervision also shifts document embeddings.
- DEPT preserves cached document embeddings close to their initial values while letting the generator receive stable, whitened embeddings via straight‑through decoding.
- Experiments on Qwen3‑4B‑Instruct‑2507 and LLaMA‑3.2‑3B‑Instruct across five BEIR datasets show DEPT outperforms training‑free, independently trained, and staged unified baselines.

## Context
Current approaches to query expansion rely on separate modules or staged optimization, which limit integration with retrieval signals. A single model that generates both expanded queries and encodes documents would be ideal but suffers from instability due to moving targets in joint training.

## Implications
DEPT enables more efficient deployment of unified models by reusing cached document embeddings, reducing compute for online hard‑negative mining. Practitioners can adopt this technique to improve retrieval relevance without retraining large embedding indexes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17632v1)
