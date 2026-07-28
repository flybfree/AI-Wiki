---
title: In-Context Learning as Implicit Policy Gradient
published: 2026-07-25T11:13:52Z
authors: Masahiro Kaneko, Timothy Baldwin
url: http://arxiv.org/abs/2607.23153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Learning as Implicit Policy Gradient

## Abstract
Recent work has shown that large language models (LLMs) can iteratively improve their outputs by incorporating generated samples and their corresponding evaluation scores as in-context examples. Despite these empirical findings, the theoretical foundations underlying this phenomenon remain poorly understood. In this paper, we show that score-conditioned In-Context Learning (ICL) admits a structural correspondence to policy gradient optimization. We first provide a constructive proof that self-attention mechanisms can implement reward-weighted aggregation analogous to the REINFORCE algorithm under specific weight matrix configurations, and discuss the relationship between this construction and the behavior of pretrained transformers. The correspondence is directional in hidden-state space and holds exactly only under the stated simplifying conditions; we quantify its strength empirically. Within our simplified hidden-state model, we furthermore derive an exact upper bound on the distribution shift induced by a bounded attention update, yielding a trust-region-like analogy to KL-constrained policy optimization. We validate our theory through extensive experiments across multiple LLMs, demonstrating that LLMs effectively utilize score information to shift output distributions toward high-scoring exemplars, and that attention weights exhibit a strong correlation with example scores.

## Metadata
- **Published**: 2026-07-25T11:13:52Z
- **Authors**: Masahiro Kaneko, Timothy Baldwin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23153v1)