---
title: Compositional RL: Evaluating and Training LLMs for Collaborative Reasoning
url: http://arxiv.org/abs/2610.17456v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_22-16-45Z_CompositionalRL_EvaluatingandTrainingLLMsforCollab.md
generated_at: 2026-10-14 00:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the concept of "compositional strength" to evaluate how much a language model contributes to a multi-model collaborative system, rather than how well it performs in isolation. The authors formalize this using Shapley values from cooperative game theory and demonstrate that standalone benchmark performance is largely uncorrelated with a model's value inside collaborative systems. They then propose Compositional Reinforcement Learning (C-RL), a training method that optimizes a model's contribution to a live multi-model system's overall outcome, achieving substantial performance gains across reasoning, coding, and scientific discovery tasks.

## Key Takeaways
- Individual model strength and compositional strength are largely uncorrelated: across five model pools, twelve collaboration methods, and twelve datasets, the authors find that in 12 of 15 (pool, method-family) settings, a model's standalone performance does not translate into advantages when placed inside a collaborative system. The coupling is weakest among general-purpose models, which are the ones practitioners most commonly deploy, meaning current evaluation practices systematically mislead practitioners about which models will be most valuable in multi-model pipelines.
- The authors formalize compositional strength using the Shapley value of a cooperative game over coalitions of a model pool, and introduce a tractable leave-one-out proxy that requires only n+1 system evaluations instead of the exponential 2^n evaluations needed for full Shapley computation, making the evaluation framework practical for real-world model pools.
- C-RL trains a policy inside a live multi-model system and rewards the collaborative system's outcome rather than the policy's isolated correctness. The leave-one-out baseline in Shapley values cancels under a group policy gradient, eliminating additional rollout costs and never requiring running a coalition without the policy. Across three collaboration protocols and eight tasks, C-RL produces the strongest collaborator in 21 of 24 settings, lifting collaborative performance by +4.0 to +5.4 points on average (roughly 3x the gain of baselines), with peaks up to +13.1 points.

## Context
As LLM deployment increasingly involves routing, debate, ensembling, and multi-agent collaboration, the field lacks principled methods for evaluating and training models specifically for their contribution within these systems. This paper bridges a critical gap between single-model evaluation culture and the reality of multi-model deployment, providing both a diagnostic framework (compositional strength via Shapley values) and a prescriptive training method (C-RL) that directly optimizes for collaborative contribution. It challenges the foundational assumption in AI evaluation that standalone benchmarks are sufficient proxies for real-world utility.

## Implications
For practitioners building multi-model pipelines, this work warns that selecting models based on leaderboard rankings may systematically underperform compared to selecting models optimized for compositional contribution, potentially wasting significant engineering effort and compute. For the research community, C-RL offers a practical training paradigm that requires no additional rollout overhead beyond standard RL on the collaborative system, making it feasible to integrate into existing RLHF or RL pipelines. Industry teams deploying model routing, debate-based reasoning, or ensemble systems should reconsider their model selection and fine-tuning strategies to explicitly target collaborative value rather than isolated accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17456v1)
