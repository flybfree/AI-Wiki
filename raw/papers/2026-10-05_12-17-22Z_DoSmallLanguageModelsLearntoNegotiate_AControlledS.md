---
title: Do Small Language Models Learn to Negotiate? A Controlled Scaling Study of RL-Trained Sellers
published: 2026-10-05T12:17:22Z
authors: Pedro Tabacof, Sagar Joglekar
url: http://arxiv.org/abs/2610.06204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Small Language Models Learn to Negotiate? A Controlled Scaling Study of RL-Trained Sellers

## Abstract
LLM agents are starting to own the full customer experience. Soon, LLMs may be selling and buying on behalf of companies and customers respectively. Small models are more cost-efficient at scale, but can reinforcement learning train them into competent sellers? We train four Gemma 4 checkpoints (2.3B to 31B effective parameters) with GRPO on a programmatic utility reward for bilateral multi-issue bargaining, and evaluate every arm on the same 1,152 negotiations against two frontier buyers it never saw in training. With the same learning rate ($10^{-6}$) for every size, the gain of the RL model over its base rises from $+0.001$ at 2.3B to $+0.078$ at 31B. Each size was trained once and the two smallest checkpoints use a different architecture, so we fit no scaling law. Tripling the learning rate, with the same or fewer training steps, improves on the shared rate at every size by $+0.032$ (2.3B) to $+0.081$ (4.5B). In exploratory comparisons with two frontier models run as sellers, the 12B seller trained at the tripled rate scores above both, though its untrained base already scores as high as they do. The 4.5B seller at that rate shows no detectable difference from either and fits on one 48 GB GPU. A further 2.3B arm at ten times the shared rate raises pooled score, but its gain concentrates on the evaluation buyer that shares a model family with the training pool. These results suggest tuning the learning rate before concluding that a small model cannot learn to negotiate, and testing against buyers from more than one model family.

## Metadata
- **Published**: 2026-10-05T12:17:22Z
- **Authors**: Pedro Tabacof, Sagar Joglekar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06204v1)