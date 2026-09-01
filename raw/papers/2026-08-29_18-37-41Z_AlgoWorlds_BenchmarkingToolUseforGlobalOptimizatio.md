---
title: AlgoWorlds: Benchmarking Tool Use for Global Optimization in Algorithmic Worlds
published: 2026-08-29T18:37:41Z
authors: Zixiang Xu, Jiaan Wang, Fandong Meng
url: http://arxiv.org/abs/2608.29397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlgoWorlds: Benchmarking Tool Use for Global Optimization in Algorithmic Worlds

## Abstract
Tool-use benchmarks generally evaluate whether an agent completes a workflow using appropriate tools and valid arguments. However, feasibility alone is insufficient in real-world decision settings such as route planning and fleet dispatch. Individual choices interact through shared constraints and costs, so a feasible solution may still be substantially suboptimal. This raises a harder question: can an agent turn information gathered through tools into a globally optimal decision? We introduce AlgoWorlds, a benchmark that transforms formally specified combinatorial optimization problems into partially observed decision environments with verifiable global optima. Each environment contains a hidden instance observed only through task-specific information tools, after which the agent commits to one structured decision evaluated for feasibility and optimality. AlgoWorlds contains 240 environments covering ten combinatorial optimization families and four workload levels. Family-specific deterministic programs generate the instances, exact algorithms certify their optima and determine workload levels, and two structurally different tool interfaces present each underlying instance. We evaluate seven leading LLMs, including Claude Opus 4.8 and GPT-5.6 Sol. Achieving global optimality remains highly challenging: although leading models produce feasible decisions in most cases, the best-performing model reaches exact optimality in only 38.61% of cases. Even when agents collect sufficient information to reconstruct the hidden instance, most failures end in feasible but suboptimal decisions. The challenge therefore extends beyond information acquisition to information integration, global constraint reasoning, and decision verification. The project homepage is available at https://xzx34.github.io/AlgoWorlds/, and the code is available at https://github.com/xzx34/AlgoWorlds.

## Metadata
- **Published**: 2026-08-29T18:37:41Z
- **Authors**: Zixiang Xu, Jiaan Wang, Fandong Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29397v1)