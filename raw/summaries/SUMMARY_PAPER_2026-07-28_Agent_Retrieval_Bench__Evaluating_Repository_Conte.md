---
title: Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents
url: http://arxiv.org/abs/2607.24882v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_09-39-09Z_AgentRetrievalBench_EvaluatingRepositoryContextRet.md
generated_at: 2026-07-28 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Agent Retrieval Bench, a file‑level benchmark that measures how coding agents locate repository files needed for their tasks. The evaluation compares multiple retrieval methods across 427 samples from 25 repositories and finds that no single approach dominates all metrics; instead, performance varies by model size, task type, and budget constraints.

## Key Takeaways
- Qwen3‑Embedding‑4B achieves the highest sample‑weighted MRR on positive retrieval tasks.  
- Qwen3‑Embedding‑8B leads in Recall@20, while RepoMap provides the best context yield within an 8K token budget.  
- Logged agent trajectories miss gold files on 27–35 % of samples, indicating a significant gap between recorded retrieval and actual file selection.

## Context
Retrieval is a critical upstream step for coding agents that determines whether they can generate correct patches. Recent work shows that model capacity and retrieval strategy heavily influence downstream success, yet few benchmarks quantify these trade‑offs across diverse tasks and repository snapshots.

## Implications
For practitioners, the benchmark reveals that selective thresholds based on counterfactual controls do not improve natural no‑gold performance, suggesting a calibration mismatch. Moreover, logged context selection often underperforms random non‑gold contexts, highlighting the need for more reliable retrieval pipelines to boost agent productivity in real coding workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24882v1)
