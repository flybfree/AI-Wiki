---
title: OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization
published: 2026-07-22T06:39:03Z
authors: Kavin Aravindan, Arihant Rastogi, Krishak Aneja, Aadi Prasad, Saiyam Jain, Vaishnavi Shivkumar, Ponnurangam Kumaraguru
url: http://arxiv.org/abs/2607.19806v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization

## Abstract
Activation steering provides a lightweight mechanism for controlling large language models at inference time, but steering vectors can have unintended externalities: utility vectors may weaken safety behavior, while refusal vectors may induce over-refusal on benign prompts. We introduce OPIUM (Optimizing Protected Injections via Utility Manifolds), a training-free method for sanitizing steering vectors through representation matching. Given reference behaviors on two prompt sets, OPIUM optimizes a new steering vector that preserves the downstream representations induced by the desired intervention while matching a safer reference behavior on prompts where the original vector fails. Across steering-externality and over-refusal settings, OPIUM improves the safety--utility tradeoff relative to vanilla steering and directional ablation, suggesting that harmful side effects of activation steering can often be mitigated directly in activation space.

## Metadata
- **Published**: 2026-07-22T06:39:03Z
- **Authors**: Kavin Aravindan, Arihant Rastogi, Krishak Aneja, Aadi Prasad, Saiyam Jain, Vaishnavi Shivkumar, Ponnurangam Kumaraguru
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19806v2)