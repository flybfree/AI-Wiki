---
title: Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts
published: 2026-09-01T11:43:41Z
authors: Nikolaos Xiros, Dimitrios Damianos, Maria-Eleni Zoumpoulidi, Leon Voukoutis, Vassilis Katsouros, Georgios Paraskevopoulos
url: http://arxiv.org/abs/2609.01100v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts

## Abstract
In current Mixture-of-Experts architectures, routing is performed based on representations dominated by structure shared across all tokens, limiting expert specialization. We show that contrasting each token against an Exponential Moving Average of the layer's hidden states, rather than routing on absolute magnitude, concentrates the routing signal onto a low-dimensional, highly separable subspace. Building on this, we propose the Contrastive Routing Mechanism (CoRM), which scores each expert by the gap between its affinity for the incoming token and its affinity for this shared reference state, interpreted through a distinct per-expert projection. The resulting experts have routing boundaries that align with linguistic structure significantly more than the Top-k baseline. Our experiments show that CoRM improves average zero-shot accuracy by +0.67 to +1.69 points (Top-1) and +1.38 to +1.77 points (Top-2) over standard Top-k MoE baselines on nine zero-shot reasoning benchmarks, at the minimal cost of 2.9% added parameters and 2.6% added FLOPs per token.

## Metadata
- **Published**: 2026-09-01T11:43:41Z
- **Authors**: Nikolaos Xiros, Dimitrios Damianos, Maria-Eleni Zoumpoulidi, Leon Voukoutis, Vassilis Katsouros, Georgios Paraskevopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01100v1)