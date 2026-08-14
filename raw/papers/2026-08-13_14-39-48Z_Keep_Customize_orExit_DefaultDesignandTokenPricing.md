---
title: Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services
published: 2026-08-13T14:39:48Z
authors: Ahmet Bugra Gundogan, Yigit Turkmen, Melih Bastopcu
url: http://arxiv.org/abs/2608.13315v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Keep, Customize, or Exit: Default Design and Token Pricing in LLM Reasoning Services

## Abstract
We study a large language model (LLM) service in which a provider chooses a per-token price and a default reasoning-token allocation, while a user may accept the default, customize the allocation, or exit. Larger allocations can improve accuracy but increase token cost and latency. We model this interaction as a Stackelberg game and derive the user's unique optimal customized allocation in closed form. For any price, the acceptable defaults form either an empty set or a compact interval. We characterize the provider's optimal default through a three-regime rule, reduce equilibrium computation to a one-dimensional price optimization, and prove the existence of the equilibrium. We further show that defaults affect the implemented reasoning allocation only when users value the convenience of avoiding customization; otherwise, every service-providing outcome implements the user's optimal customized allocation. Experiments with two compact open-weight reasoning models on five mathematics and science benchmarks support the accuracy-token model and show how model and task characteristics determine equilibrium prices, defaults, and reasoning allocations.

## Metadata
- **Published**: 2026-08-13T14:39:48Z
- **Authors**: Ahmet Bugra Gundogan, Yigit Turkmen, Melih Bastopcu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13315v1)