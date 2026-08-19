---
title: Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents
url: http://arxiv.org/abs/2608.18008v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-55-46Z_Policy_InvariantRewardShapingfromLLMFeedback_AFram.md
generated_at: 2026-08-18 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a framework for combining large language models with reinforcement learning by treating the LLM’s per‑state progress score as a bounded potential function within a Goal‑Augmented Markov Decision Process. It proves that using this shaping term preserves the optimal policy set even when the LLM scores are inaccurate, offering a stronger guarantee than typical LLM‑as‑reward methods.

## Key Takeaways
- The hybrid architecture is modeled as a Goal‑Augmented MDP where the LLM score acts as a bounded potential function that shapes the reward without altering the optimal policy set.  
- Accuracy of the LLM’s progress scores does not affect the preservation of optimality, because the shaping term is mathematically independent of score magnitude or error.  
- Numerical experiments on four MDPs, including an adversarial case scaled tenfold, confirm the theoretical guarantee across diverse reward configurations.

## Context
The integration of language models into reinforcement learning remains largely unexplored in terms of formal guarantees, leaving practitioners to rely on heuristic or empirical methods. This work provides a rigorous analysis that bridges theory and practice, offering a clear path for safe deployment of LLM‑driven agents.

## Implications
For industry, the framework enables developers to embed LLMs into control systems with confidence that policy optimality is maintained despite imperfect model outputs. Practitioners can adopt this approach to improve robustness in autonomous decision‑making tasks without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.18008v1)
