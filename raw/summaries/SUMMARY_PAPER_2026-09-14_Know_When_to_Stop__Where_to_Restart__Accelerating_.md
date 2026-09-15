---
title: Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation
url: http://arxiv.org/abs/2609.14636v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-13_16-17-35Z_KnowWhentoStop_WheretoRestart_AcceleratingMulti_Tu.md
generated_at: 2026-09-14 22:26
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces STRIDE, a novel acceleration framework for multi-turn agentic on-policy distillation that dynamically optimizes the trade-off between computational cost and model performance. By leveraging empirical findings that informative supervision is concentrated in early turn prefixes and error-related loss spikes at the first mistake, STRIDE employs adaptive early stopping and a prefix caching mechanism to efficiently truncate and restart student rollouts. The proposed method achieves significant speedups while matching or surpassing full-trajectory distillation baselines across agentic and mathematical reasoning benchmarks.

## Key Takeaways
- On-policy distillation in multi-turn settings suffers from high computational costs due to lengthy autoregressive rollouts, but existing fixed-budget truncation methods fail to account for trajectory-dependent variations in teacher signal reliability.
- Empirical analysis on the τ²-bench reveals that high-quality supervision is heavily concentrated in the initial prefix of each turn, and cross-turn performance degradation is temporally locked to a student's first erroneous action rather than accumulating gradually over multiple turns.
- STRIDE combines adaptive early stopping with a prefix buffer to dynamically terminate low-reliability rollouts and restart generation at optimal points, achieving up to 5.10x speedup on AIME benchmarks while outperforming fixed-budget baselines and matching full-trajectory distillation quality.

## Context
As large language models increasingly operate in multi-turn agentic workflows, the computational overhead of generating complete trajectories for teacher-student knowledge transfer has become a major bottleneck. Traditional distillation approaches rely on static truncation rules that ignore the dynamic reliability of model outputs across different turns and domains. This research addresses a critical gap in efficient AI training by introducing data-driven curriculum learning principles tailored to agentic reasoning tasks, shifting the paradigm from fixed computational budgets to adaptive signal quality thresholds.

## Implications
The STRIDE framework offers practitioners a scalable solution for reducing inference and training costs without sacrificing distillation quality, making large-model knowledge transfer more accessible for resource-constrained environments. By dynamically adapting to signal reliability, it enables more efficient multi-teacher and cross-domain training pipelines that can be deployed in real-world agentic applications. This approach also sets a new standard for evaluating acceleration techniques beyond simple latency metrics, emphasizing performance retention under aggressive computational constraints while providing actionable insights for future distillation research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14636v1)
