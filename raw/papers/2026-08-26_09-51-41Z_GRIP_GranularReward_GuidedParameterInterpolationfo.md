---
title: GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning
published: 2026-08-26T09:51:41Z
authors: Lam So, Canhui Wu, Han Lin
url: http://arxiv.org/abs/2608.25583v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning

## Abstract
Reasoning-oriented large language models often achieve strong problem-solving performance by generating long chains of thought, but this behavior substantially increases inference cost and latency. In contrast, instruction-tuned models tend to answer more concisely, yet often lack comparable reasoning ability. This accuracy-efficiency mismatch motivates a lightweight approach that combines the strengths of both models without full model retraining. In this paper, we propose GRIP (Granular Reward-guided Interpolation of Parameters), a reward-guided parameter interpolation framework for efficient reasoning. Given a reasoning model and an instruction model with identical architectures, GRIP assigns learnable interpolation ratios to individual modules and optimizes only these ratios while keeping both source models frozen. The interpolation ratios are trained with a reward signal that favors responses that are both correct and concise. Experiments show that GRIP achieves a better accuracy-efficiency trade-off than fixed or search-based merging baselines and further reveals module-wise fusion patterns associated with efficient reasoning.

## Metadata
- **Published**: 2026-08-26T09:51:41Z
- **Authors**: Lam So, Canhui Wu, Han Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25583v1)