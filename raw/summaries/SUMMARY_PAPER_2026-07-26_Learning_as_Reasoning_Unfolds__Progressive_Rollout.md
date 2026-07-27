---
title: Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning
url: http://arxiv.org/abs/2607.22002v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_06-04-04Z_LearningasReasoningUnfolds_ProgressiveRolloutAlloc.md
generated_at: 2026-07-26 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VIGOR, a variance‑guided rollout allocation method for reinforcement learning with verifiable rewards that reduces the number of generated chain‑of‑thought examples compared to GRPO. By allocating extra rolls only to high‑variance samples, VIGOR achieves up to 2.3× fewer rolls on math tasks and reaches GRPO’s final coding pass rate with 1.49× fewer rolls while improving test pass rates by 3.4 points.

## Key Takeaways
- VIGOR replaces a fixed rollout budget per example with an adaptive strategy that adds rolls to the most variance‑rich samples until the total budget is met, directly linking reward variance to gradient magnitude.
- Experiments show VIGOR reduces rollouts dramatically: 2.3× fewer on math reasoning and 1.49× fewer for coding full passes, while still attaining GRPO’s final pass rate.
- The method improves coding average test pass rates by 3.4 points, demonstrating that variance‑guided allocation yields both efficiency gains and higher performance.

## Context
RLVR methods like GRPO are central to improving large language model reasoning but suffer from high computational cost due to excessive rollout generation. Existing solutions either increase the pool size or rely on post‑hoc filtering, which slows training. VIGOR’s adaptive allocation offers a principled way to allocate compute where it matters most, aligning with trends toward efficient, scalable RL for LLMs.

## Implications
For practitioners, VIGOR provides a practical framework to cut training time without sacrificing accuracy, making large‑scale reasoning experiments feasible. In industry, this could accelerate model iteration cycles and reduce cloud costs, while the theoretical link between variance and gradient magnitude offers deeper insight into efficient RL design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22002v1)
