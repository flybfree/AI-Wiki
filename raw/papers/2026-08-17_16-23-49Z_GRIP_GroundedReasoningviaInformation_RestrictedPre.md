---
title: GRIP: Grounded Reasoning via Information-Restricted Premises
published: 2026-08-17T16:23:49Z
authors: Lirui Teng
url: http://arxiv.org/abs/2608.16776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GRIP: Grounded Reasoning via Information-Restricted Premises

## Abstract
High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we introduce \textbf{GRIP} (Grounded Reasoning via Information-Restricted Premises), which imposes capacity asymmetry: the decoder keeps full-dimensional access to the query, while retrieved evidence passes through a severe stochastic bottleneck. This forces the evidence channel to encode only the residual information unavailable from the query. Across five reasoning benchmarks, GRIP outperforms strong iterative baselines, cuts a query--latent mutual-information diagnostic by roughly 30$\times$ (14.8 $\to$ 0.47 bits), and reduces hallucination by 73\%. Residual-alignment analysis further shows that the bottleneck output occupies subspaces less aligned with the query than baseline representations.

## Metadata
- **Published**: 2026-08-17T16:23:49Z
- **Authors**: Lirui Teng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16776v1)