---
title: PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs
url: http://arxiv.org/abs/2608.30528v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_09-59-07Z_PAC_Progress_AugmentedAdvantageCurriculumforMulti_.md
generated_at: 2026-08-31 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PAC, a Progress-Augmented Advantage Curriculum for multi-task reinforcement learning of large language models. It combines advantage-derived learnability signals with recent reward gains to guide rollout allocation during GRPO training. Experiments show PAC achieves comparable validation scores with fewer steps and higher final averages than random sampling or advantage-only baselines.

## Key Takeaways
- Advantage-driven learnability measures how much a task can improve the policy, providing an objective for task selection.
- Recent reward gains track actual performance improvements, ensuring updates are both large and effective.
- A Bayesian Thompson Sampling controller uses these dual signals to allocate rollouts efficiently across tasks during training.

## Context
Current RL methods often treat task mixtures as static or manually designed, ignoring how usefulness evolves over time. This limits sample efficiency for LLM post-training optimization in complex reasoning scenarios.

## Implications
PAC offers a principled way to adapt curriculum online, reducing wasted rollouts and accelerating convergence. Practitioners can implement similar signal fusion strategies to improve LLM fine‑tuning outcomes across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30528v1)
