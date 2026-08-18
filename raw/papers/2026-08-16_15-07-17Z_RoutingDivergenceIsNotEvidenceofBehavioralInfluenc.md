---
title: Routing Divergence Is Not Evidence of Behavioral Influence in Same-Weight MoE Self-Distillation
published: 2026-08-16T15:07:17Z
authors: Cedric Caruzzo, Donggeun Yoo, Tae Soo Kim
url: http://arxiv.org/abs/2608.15787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Routing Divergence Is Not Evidence of Behavioral Influence in Same-Weight MoE Self-Distillation

## Abstract
Two Mixture-of-Experts (MoE) forward passes can share every weight yet route the same token through different experts. This creates a possible blind spot in same-weight self-distillation, where a demonstration-conditioned teacher supervises a query-only student. We study this mismatch in its single-step form, with frozen weights rather than as a proxy for a full training trajectory. An exact blockwise decomposition separates a routing term, which changes gates at fixed content, from a dense-like content term. Across seven open-weight checkpoints and two domains, the routing term spans only $1.6\times$ as a fraction of block output, while its residual-stream exposure spans $3.2\times$. Exposure is ordered by the routed block's share of the residual. Scaling the always-on backbone in two confirmatory models moves exposure monotonically; common-mode controls support a mass-and-coherence mechanism rather than denominator dilution alone. Preregistered PubMedQA patches on three models show that the full routing term moves outputs by less than half the natural context effect and is largely reproduced by matched-norm noise, whereas the content term is strongly direction-specific. Scale and merged-expert probes show that the narrow block-level range is not universal, although exposure remains small at the tested boundaries. Router movement alone is therefore not evidence of behavioral influence: measure exposure first, and use a behavioral intervention when the decision matters.

## Metadata
- **Published**: 2026-08-16T15:07:17Z
- **Authors**: Cedric Caruzzo, Donggeun Yoo, Tae Soo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15787v1)