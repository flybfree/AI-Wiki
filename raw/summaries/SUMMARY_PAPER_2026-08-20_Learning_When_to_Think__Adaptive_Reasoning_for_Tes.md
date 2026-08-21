---
title: Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation
url: http://arxiv.org/abs/2608.20256v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_16-54-08Z_LearningWhentoThink_AdaptiveReasoningforTest_TimeC.md
generated_at: 2026-08-20 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a method that lets reasoning language models allocate their own computing effort per problem by selecting one of three response modes at the start of each answer: NoThink, Short, or Long. Trained with Group Relative Policy Optimization and reinforced by shaped rewards, the model learns to use less tokens for easy problems while still handling hard ones effectively.

## Key Takeaways
- The adaptive policy chooses among NoThink, Short, and Long modes based on problem difficulty rather than randomly assigning them.
- Brief reasoning (Short mode) yields higher accuracy than extended reasoning (Long mode), showing the router correctly sorts easier tasks to shorter responses.
- Mean response length dropped from 4,796 tokens to 2,811 tokens—a 41% reduction—while average MATH500 accuracy remained close to the baseline.

## Context
Fixed token budgets in reasoning models often cause over‑computation on simple questions and under‑computation on complex ones. This work demonstrates that allowing a model to self‑regulate its reasoning effort can improve both efficiency and performance without retraining, offering a scalable alternative for deploying large language models.

## Implications
For researchers, the approach shows that adaptive compute allocation is feasible within standard RL frameworks, encouraging further study of dynamic resource management in AI systems. For industry practitioners, it means lower inference costs and the ability to serve diverse workloads on limited hardware without sacrificing quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20256v1)
