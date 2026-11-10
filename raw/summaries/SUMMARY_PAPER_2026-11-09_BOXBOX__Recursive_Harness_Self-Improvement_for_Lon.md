---
title: BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization
url: http://arxiv.org/abs/2611.09218v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_09-36-00Z_BOXBOX_RecursiveHarnessSelf_ImprovementforLong_Run.md
generated_at: 2026-11-09 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces BOXBOX, a system that enables agents to recursively improve their own harnesses during ongoing, long-running tasks rather than relying on offline pre-optimization using reference answers. The authors also introduce PerfRace, a benchmark designed to evaluate long-running performance optimization of software projects. Under matched test-time budgets, BOXBOX achieves a Speedup@4h of 1.70x, outperforming the strongest baseline at 1.54x, demonstrating that in-task harness revision leads to more efficient use of task time and model cost.

## Key Takeaways
- Existing offline harness optimization methods depend on reference answers and are designed for reuse on held-out tasks, making them poorly suited for open-ended, long-running real-world tasks where new difficulties emerge over time that a statically optimized harness cannot address.
- BOXBOX introduces two critical mechanisms: agent-triggered harness revision, where the agent itself decides when and how to modify its harness based on task-specific experience, and kernel-managed hot reloading, which swaps in updated harness components while preserving the agent's current execution context, avoiding costly restarts or context loss.
- The evaluation on PerfRace uses matched test-time budgets and compares BOXBOX against three baselines (Frozen Harness, offline Harness Evolution, and Harness Scaling), showing that recursive in-task self-improvement yields higher speedup and more efficient allocation of both wall-clock time and model inference cost than any offline or scaling-based alternative.

## Context
This work sits at the intersection of agent-based software engineering, automated program optimization, and self-improving AI systems. Most prior harness optimization research assumes a closed-world setting where ground-truth answers exist and tasks are finite, enabling offline tuning. As AI agents are increasingly deployed on open-ended, multi-hour software engineering tasks such as performance profiling and code optimization, the assumption that a harness can be fully optimized before execution breaks down. PerfRace and BOXBOX together provide the first structured study of harness self-improvement during live task execution, filling a gap in the literature on adaptive agent architectures.

## Implications
For practitioners building autonomous coding or optimization agents, BOXBOX suggests that embedding a lightweight self-modification loop into the agent's runtime can yield measurable performance gains without requiring additional model training or offline data collection. For the broader AI research community, the kernel-managed hot reloading mechanism offers a reusable infrastructure pattern for any agent system that needs to update its tooling or strategy mid-task without discarding accumulated state. As long-running agentic workflows become more common in software engineering and DevOps pipelines, techniques like recursive harness revision may become a standard component of agent orchestration frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.09218v1)
