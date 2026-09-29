---
title: CUA-Sandbox: Efficient Environments for Computer-Use Agent Reinforcement Learning
url: http://arxiv.org/abs/2609.32750v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_16-16-08Z_CUA_Sandbox_EfficientEnvironmentsforComputer_UseAg.md
generated_at: 2026-09-28 20:38
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces CUA-Sandbox, a novel framework designed to optimize reinforcement learning for computer-use agents by decoupling private mutable state from shared application runtimes. By leveraging state-scoped execution and transactional lifecycle operations, the system enables multiple concurrent environments to reuse initialized software instances while maintaining independent trajectories. Experimental results demonstrate that CUA-Sandbox achieves significant efficiency gains, including a 6.20x increase in rollout throughput and up to a 504x reduction in incremental storage, without compromising task success rates compared to traditional Docker-based deployments.

## Key Takeaways
- CUA-Sandbox addresses the inefficiency of replicating initialized runtimes for every rollout by observing that only mutable state requires independence; it separates private state capsules from shared runtimes, allowing multiple environments to execute concurrently on a single runtime instance while preserving trajectory isolation through state-scoped execution and transactional resets or branches.
- The framework delivers substantial resource optimizations, achieving up to a 6.20x increase in rollout throughput, reducing per-environment memory consumption by 9.2 times, and cutting incremental

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32750v1)
