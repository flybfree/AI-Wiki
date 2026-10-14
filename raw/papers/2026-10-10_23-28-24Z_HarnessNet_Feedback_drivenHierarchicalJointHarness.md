---
title: HarnessNet: Feedback-driven Hierarchical Joint Harness Evolution for Multi-agent Systems
published: 2026-10-10T23:28:24Z
authors: Zhaoyuan Qiu, Sachith Seneviratne, Yu Xia, Saman Halgamuge
url: http://arxiv.org/abs/2610.15221v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HarnessNet: Feedback-driven Hierarchical Joint Harness Evolution for Multi-agent Systems

## Abstract
AI agents can evolve by using environment feedback to revise their harnesses, the software managing model inputs, tool use, memory, and execution, while keeping foundation models frozen. Existing studies focus on single agents, leaving joint harness evolution in multi-agent systems (MAS) underexplored. A single global optimizer faces growing context and workload as the system scales, while access restrictions may prevent sharing agent internals or system-wide feedback. We propose HarnessNet, a framework for hierarchical harness evolution in MAS. Its basic unit, Agentron, comprises an evolvable forward harness, a foundation model, and a local optimizer that can observe and modify only that harness. Agentrons form a layered graph through which environment feedback propagates backward, with upstream optimizers receiving node-specific feedback from the downstream layer. This decomposes joint harness evolution into smaller, coordinated tasks with separate contexts, reducing individual optimizers' context and workload while keeping access local. Optimizers need not access all agent trajectories or raw environment feedback. Experiments on AgentBench with multiple foundation models demonstrate the feasibility of training HarnessNet. Compared with a single global optimizer, HarnessNet achieves comparable performance gains while respecting local privacy and requiring fewer tokens and less time per optimizer call. A migration study shows that the evolved harnesses remain jointly effective after replacing the foundation models, suggesting transferability across models.

## Metadata
- **Published**: 2026-10-10T23:28:24Z
- **Authors**: Zhaoyuan Qiu, Sachith Seneviratne, Yu Xia, Saman Halgamuge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15221v1)