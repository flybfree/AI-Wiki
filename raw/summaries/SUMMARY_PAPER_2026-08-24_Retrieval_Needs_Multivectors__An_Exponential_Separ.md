---
title: Retrieval Needs Multivectors: An Exponential Separation
url: http://arxiv.org/abs/2608.21494v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_13-26-44Z_RetrievalNeedsMultivectors_AnExponentialSeparation.md
generated_at: 2026-08-24 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper establishes an exponential separation between single-vector and multi-vector embeddings for document ranking tasks, demonstrating that single‑vector models can rank all relevant documents above irrelevant ones only with exponentially large query sets. It introduces ANDOR, a benchmark that realizes these hard examples, showing state‑of‑the‑art single‑vector models fail in zero‑shot settings while multi‑vector models improve substantially after fine‑tuning.

## Key Takeaways
- Single‑vector embeddings require exponential size to achieve perfect ranking on the constructed query and document sets.  
- Multi‑vector embeddings can solve the same problem with polynomial‑size representations, confirming an exponential gap in expressive power.  
- The ANDOR benchmark reveals that fine‑tuning yields only marginal gains for single‑vector models but substantial improvements for multi‑vector models.

## Context
The paper builds on Jayaram’s theoretical work to move beyond score approximation toward ranking challenges, where representation capacity is critical. It contributes a concrete family of datasets that expose the limitations of current embedding approaches in retrieval systems.

## Implications
For practitioners, this highlights that single‑vector embeddings may be insufficient for high‑quality ranking without massive data or model size, encouraging adoption of multi‑vector techniques. Industry research should prioritize models that can handle such exponential separation to maintain competitive performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21494v1)
