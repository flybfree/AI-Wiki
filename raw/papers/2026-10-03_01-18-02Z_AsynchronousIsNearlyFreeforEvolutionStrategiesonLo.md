---
title: Asynchronous Is Nearly Free for Evolution Strategies on Long-Horizon Agentic Tasks
published: 2026-10-03T01:18:02Z
authors: William Hoy, Jingxuan Fan, Nurcin Celik, Xu Pan
url: http://arxiv.org/abs/2610.04196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asynchronous Is Nearly Free for Evolution Strategies on Long-Horizon Agentic Tasks

## Abstract
LLM-based long-horizon agentic post-training is often bottlenecked by rollout generation: trajectories span many interaction turns, completion times vary substantially, and synchronous update barriers leave faster workers waiting for stragglers. Asynchronous reinforcement learning which has been adopted in LLM post-training addresses this inefficiency by consuming trajectories as they arrive, but introduces policy lag and off-policy optimization. Evolution strategies (ES) offer a backpropagation-free alternative for LLM post-training, yet it relies on a larger number of rollouts and existing practices have remained largely synchronous. In this short-form paper, we introduce bounded-staleness asynchronous ES and demonstrate it on Endless Terminals benchmark using Qwen2.5-7B-Instruct. Across three evaluation seeds, natural Async-1 matches synchronous ES, achieving 25.9\% versus 25.4\% held-out success. Controlled schedules that delay 10\% of each update cohort by four or eight policy updates reduce success by only 1.6 and 3.1 percentage points, respectively, without explicit off-policy correction. GRPO performs better overall, reaching 29.0\% held-out success, but importantly our results show that ES tolerates moderate policy staleness with limited degradation, opening possibilities for future improvement of ES-based post-training with asynchronous algorithms. To the best of our knowledge, we are the first to demonstrate the effectiveness of sync and async ES on a multi-turn terminal style agentic coding task.

## Metadata
- **Published**: 2026-10-03T01:18:02Z
- **Authors**: William Hoy, Jingxuan Fan, Nurcin Celik, Xu Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04196v1)