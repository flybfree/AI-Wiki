---
title: From Attention Masks to Inert Zero-Vector Tokens: OAttention and O-Closure for Token Dynamics
published: 2026-08-21T14:43:45Z
authors: Heyang Gong
url: http://arxiv.org/abs/2608.21174v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Attention Masks to Inert Zero-Vector Tokens: OAttention and O-Closure for Token Dynamics

## Abstract
Attention masks are relation-level controls: they specify which query--source pairs may interact. They do not provide a representation-carried token state that is non-participating at the attention boundary. We assign each token hidden carrier \(h_i\) an active-presence coefficient \(p_i=\lVert h_i\rVert^2/(τ+\lVert h_i\rVert^2)\). The same coefficient has two roles: it gates information emitted by token \(i\), and it determines the mass with which token \(i\) enters computations shared with other tokens.   OAttention is the support-coupled attention realization of this rule. It gates the receiver output by \(p_i\) and weights source \(j\) by \(p_j\) in both the attention numerator and partition, while retaining the standard score, visibility relation, exponential competition, and value aggregation. This makes the zero-vector token a zero element and yields exact null-receiver, null-source insertion, self-attention insertion, and empty-support properties. The same token-level presence gives local O-components (OFFN, ONorm, and OInject), presence-weighted OStandardize, the O-Closure law \(M(H\oplus0)=M(H)\oplus0\), and an OTransformer by residual and compositional closure.   The canonical operator is checked by contract tests and a GPU evaluation. In a zero-fine-tuning retrofit of a cloned pretrained TabPFN v3 regressor, calibrated hidden-carrier OAttention and Full-O variants change mean RMSE by $+0.088\%$ and $+0.177\%$, respectively, over 18 matched dataset--seed cases. A two-block ablation shows that OAttention alone does not preserve a NULL state through ordinary host components, whereas the OTransformer path does. These are scoped tests of exactness, active-path compatibility, and compositional necessity; they do not establish universal no-loss, arbitrary-host closure, learned attraction to the origin, or a general semantics for missing values.

## Metadata
- **Published**: 2026-08-21T14:43:45Z
- **Authors**: Heyang Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21174v1)