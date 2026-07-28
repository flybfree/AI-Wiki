---
title: The Entropic Bound for Transformers: Why Static Rank Fails and Attention-Native Rank Recovers
published: 2026-07-25T05:27:52Z
authors: Byeong Hoon Yoon
url: http://arxiv.org/abs/2607.23050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Entropic Bound for Transformers: Why Static Rank Fails and Attention-Native Rank Recovers

## Abstract
Neural scaling laws describe how loss decreases as models, data, and compute grow, but they do not answer a prior question: for a fixed task, what is the minimum model capacity required to solve it? We study this through the Entropic Bound, a spectral notion of task-intrinsic capacity for Transformers. We first prove that, in a linear attention surrogate, the intrinsic rank $r^*$ of the token-mixing operator is a tight lower bound: any rank-deficient model incurs unavoidable excess risk, and the bound is achievable at $r^*$. We further show that gradient descent recovers this rank under standard low-rank implicit-bias assumptions, confirm all three properties empirically, and show $r^*$ is recoverable from data before training. We then ask whether this transfers to real attention. A naive transfer fails, and a controlled interpolation ladder localizes the cause precisely: it is not softmax and not a rank constraint, but the input-conditioned nature of attention's mixing operator, which a static weight kernel cannot summarize. Motivated by this, we introduce an attention-native intrinsic rank -- the minimum query-key kernel rank realizing the task within the attention class -- and show that under this definition the full Entropic Bound structure (deficiency, achievability, recovery) is restored for both linear and softmax attention, with the energy effective rank as the estimator robust to softmax distortion. Finally, we map the boundary of data-only predictability: $r^*$ is exactly recoverable for linear QK attention, even without the value map at scale, while softmax attention admits only partial pre-training recovery due to nonlinear inversion and kernel-value identifiability effects. Our results reframe the Entropic Bound from a post-hoc descriptor into an attention-native capacity measure with a precisely characterized predictability frontier.

## Metadata
- **Published**: 2026-07-25T05:27:52Z
- **Authors**: Byeong Hoon Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23050v1)