---
title: PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning
published: 2026-09-28T13:35:47Z
authors: Jiaan Zhu, Wei Gao, Youhui Bai, Zewen Jin, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Cheng Li
url: http://arxiv.org/abs/2609.35158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning

## Abstract
Multi-turn rollout dominates the cost of agentic reinforcement learning (RL). Asynchronous execution and elastic GPU resources can accelerate this stage, but adding rollout replicas yields diminishing returns while training GPUs remain idle between updates. We observe that effective resource use also depends on the prefill--decode (PD) configuration. Both the choice between colocation and disaggregation and the optimal PD ratio vary with the workload, making resource scaling and PD configuration interdependent. Exploiting this opportunity requires selecting effective configurations and realizing their benefits within transient resource-availability windows despite reconfiguration costs.   We present PEARL, an asynchronous agentic RL system that coordinates external resource elasticity, temporary reuse of idle training GPUs, and adaptive PD execution. PEARL maintains a unified GPU--worker--role state and uses runtime profiles to predict rollout batch completion time, accounting for environment-induced reductions in decode concurrency. It selects the PD mode and ratio under the current GPU budget and translates each decision into an incremental transition plan that minimizes worker and role changes. Cost-aware switching and borrowing policies suppress transitions with insufficient expected benefit while ensuring timely return of training GPUs. Our evaluation show that PEARL achieves $2.17$--$2.79\times$ the throughput of fixed-resource ROLL across different LLMs. Compared with RLBoost+, throughput improves by up to approximately 26.9\% for Qwen3-8B and 36.3\% for Qwen3-30B-A3B.

## Metadata
- **Published**: 2026-09-28T13:35:47Z
- **Authors**: Jiaan Zhu, Wei Gao, Youhui Bai, Zewen Jin, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Cheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35158v1)