---
title: Training-Free Universal Approximation by Prompting Random Transformers
published: 2026-08-10T12:57:22Z
authors: Alexander Hsu, Rongjie Lai
url: http://arxiv.org/abs/2608.09558v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-Free Universal Approximation by Prompting Random Transformers

## Abstract
How expressive is prompting a transformer? Answering this question is important for separating the roles of prompting, architecture, and pretraining in transformer models, and for determining whether task-specific behavior must be stored in model weights or can instead be induced at inference time through the prompt. We show, in an approximation-theoretic sense, that pretraining is optional: a single-layer softmax attention network with random, untrained weights can approximate any Hölder function on a compact manifold when steered by an appropriate soft prompt. Guided by the connection between softmax attention and kernel methods, we construct explicit soft prompts (a prompt per target function, independent of the query) as solutions to linear systems matching attention logits to Gaussian kernel exponents, under which the frozen transformer emulates the classical Nadaraya-Watson kernel estimator. The construction requires only a mild rank condition on the weights, which we show holds almost surely under Gaussian initialization. The prompted network inherits the theoretical guarantees of kernel regression, leading to universal approximation theorems with minimax-optimal rates that depend on the intrinsic dimension. We further quantify the cost of prompting, exposing a tradeoff between the norm of the constructed soft prompt tokens, prompt length, and hidden dimension. Numerical experiments corroborate the constructions and predicted rates.

## Metadata
- **Published**: 2026-08-10T12:57:22Z
- **Authors**: Alexander Hsu, Rongjie Lai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09558v1)