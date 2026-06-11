---
title: Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients
url: http://arxiv.org/abs/2605.06650v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-07_17-55-21Z_BeyondNegativeRollouts_Positive_OnlyPolicyOptimiza.md
generated_at: 2026-06-11 10:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Positive-Only Policy Optimization (POPO), a reinforcement learning with verifiable rewards framework that learns exclusively from online positive rollouts, eliminating the need for explicit negative samples. The authors demonstrate that POPO can achieve performance comparable to or better than Group Relative Policy Optimization (GRPO) on standard mathematical benchmarks, including reaching 36.67% in AIME 2025 with Qwen‑Math‑7B versus GRPO’s 30.00%.  

## Key Takeaways
- POPO replaces negative rollouts with a bounded importance sampling over positive rollouts, allowing gradients to emerge implicitly through redistribution of positive probability mass.  
- The method employs a siamese policy network with momentum‑based adaptation and a bounded similarity penalty instead of KL divergence for stable policy evolution.  
- Experiments show POPO outperforms GRPO on multiple AIME‑style tasks, highlighting the effectiveness of positive‑only learning in sparse binary reward settings.  

## Context
Current RLVR research focuses on improving reasoning capabilities of large language models through deterministic verification, yet most approaches still rely on costly negative rollout sampling or complex advantage estimation. This work shifts attention to a simpler, sample‑efficient strategy that leverages only the positive outcomes observed during interaction.  

## Implications
POPO offers practitioners a more efficient way to train LLMs for reasoning tasks without generating large batches of negative samples, reducing computational overhead and enabling faster iteration cycles. The findings suggest that future LLM alignment and benchmarking can benefit from policies optimized purely on positive feedback, potentially lowering resource costs in real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.06650v1)
