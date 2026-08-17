---
title: AgentRewind: Recoverable Execution for Long-Horizon LLM Agents
published: 2026-08-14T15:20:35Z
authors: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
url: http://arxiv.org/abs/2608.14380v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

## Abstract
Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.

## Metadata
- **Published**: 2026-08-14T15:20:35Z
- **Authors**: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14380v1)