---
title: The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation
published: 2026-07-21T15:57:36Z
authors: Michael Jungo, Aixiu An
url: http://arxiv.org/abs/2607.19226v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation

## Abstract
Reinforcement learning with verifiable rewards (RLVR) has been established as a viable paradigm for the post-training of Large Language Models (LLMs), including downstream tasks, such as Neural Machine Translation (NMT). With the latest research indicating that RLVR could be the preferred training method for translating legal documents due to the induced reasoning capabilities, it raises the question whether it is really attributed to the reasoning or more generally to the training paradigm. We investigate the importance of including the model's reasoning trace in the generated responses during both training and inference by systematically omitting it from one of the phases. Our experiments show that including the reasoning, specifically during inference, has a positive effect on the overall translation quality. Furthermore, we recognise that the reasoning leads to an increase in output tokens, hence we study the cost-quality tradeoff between the increased computational demands and the improved translation quality.

## Metadata
- **Published**: 2026-07-21T15:57:36Z
- **Authors**: Michael Jungo, Aixiu An
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19226v1)