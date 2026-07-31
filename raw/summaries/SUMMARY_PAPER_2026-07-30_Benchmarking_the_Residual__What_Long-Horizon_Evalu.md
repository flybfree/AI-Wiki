---
title: Benchmarking the Residual: What Long-Horizon Evaluations Add Beyond Matched Short-Task Performance
url: http://arxiv.org/abs/2607.27283v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_13-57-32Z_BenchmarkingtheResidual_WhatLong_HorizonEvaluation.md
generated_at: 2026-07-30 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces the concept of horizon residual to evaluate long‑horizon agent performance beyond matched short‑task results. It argues that failure in longer tasks may stem from compounding errors or increasing difficulty as context accumulates. The horizon residual is defined as the log‑ratio between a baseline prediction built from individual stages and actual full‑task success.

## Key Takeaways
- Long‑horizon failures are not explained by simple error accumulation but also by harder decisions emerging later in the task.
- Context rot, where earlier execution makes later work harder, can cause degradation that is not captured by short‑task benchmarks.
- The horizon residual quantifies the difference between a stage‑wise baseline prediction and actual success, highlighting that full rollouts differ from chosen baselines.

## Context
Current AI evaluation often relies on matching short‑task performance across tasks, overlooking how context evolves over time. This paper addresses the gap by proposing a metric that accounts for temporal dynamics in agent behavior.

## Implications
Practitioners should adopt horizon residual as a diagnostic tool to identify hidden degradation in long‑horizon deployments. It encourages more nuanced benchmarking and informs design of agents that maintain performance across extended interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27283v1)
