---
title: ReCo: Reweighting GRPO Against Distributional Concentration
published: 2026-07-29T12:45:55Z
authors: Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim
url: http://arxiv.org/abs/2607.26862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReCo: Reweighting GRPO Against Distributional Concentration

## Abstract
Group Relative Policy Optimization (GRPO) has become a standard reinforcement learning method for post-training language models. Recent work shows that GRPO can reduce the base model's reasoning capacity and underperform it in Pass@k when k is large, indicating reduced coverage of reasoning paths. We find that this reduction is associated with GRPO concentrating on responses that the base model already generates with high probability. We trace this concentration to two mechanisms in the GRPO update. At the response level, high-probability responses dominate the group gradient through repeated occurrence. At the token level, GRPO's importance ratio scales gradients, further reinforcing tokens that become more likely under the current policy. We propose ReCo, a reweighting method that addresses both effects. Response contributions are normalized by their expected occurrence within the rollout group, and the token-level importance ratio is replaced with a variance-based ratio that gives larger update scale to non-saturated decision points where alternative token choices remain plausible. Across Qwen2.5-Math-1.5B/7B and Llama-3.1-8B-Instruct on five mathematical reasoning benchmarks, ReCo improves Pass@k for large values of k and is comparable to GRPO for small values of k.

## Metadata
- **Published**: 2026-07-29T12:45:55Z
- **Authors**: Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26862v1)