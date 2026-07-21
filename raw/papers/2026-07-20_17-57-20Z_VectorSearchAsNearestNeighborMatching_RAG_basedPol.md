---
title: Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal Inference
published: 2026-07-20T17:57:20Z
authors: Masahiro Kato, Taka Kato
url: http://arxiv.org/abs/2607.18225v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vector Search As Nearest Neighbor Matching: RAG-based Policy Learning in Causal Inference

## Abstract
We propose one-step and two-step methods for policy learning with retrieval-augmented generation (RAG). We formulate RAG-based action selection under the potential outcome framework. In the two-step method, vector search retrieves action-specific neighboring evidence in an embedding space, the generator estimates conditional expected outcomes or their contrasts, and a plug-in rule selects an action. This formulation connects action-specific vector search with nearest-neighbor matching in causal inference. We decompose the regret of the two-step method into candidate-generation regret and within-candidate choice regret, and we bound the latter using prediction-error guarantees for nearest-neighbor estimators and transformers. We evaluate the one-step method directly as a policy because its intermediate computation is unobserved.

## Metadata
- **Published**: 2026-07-20T17:57:20Z
- **Authors**: Masahiro Kato, Taka Kato
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18225v1)