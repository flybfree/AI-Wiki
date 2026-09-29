---
title: CUA-Sandbox: Efficient Environments for Computer-Use Agent Reinforcement Learning
published: 2026-09-26T16:16:08Z
authors: Xin Yan, Zhengbo Jiao, Jiaqi Liu, Zhenglin Wan, SiYuan Ma, Xuliang Yu, Tianyi Jiang, Chubin Zhang, Pengfei Zhou, Wangbo Zhao, Xingrui Yu, Bo An, Yang You, Ivor Tsang
url: http://arxiv.org/abs/2609.32750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUA-Sandbox: Efficient Environments for Computer-Use Agent Reinforcement Learning

## Abstract
Reinforcement learning enables computer-use agents to improve through interaction with real software environments, including websites and desktop applications. However, conventional deployments replicate an initialized runtime for each independent rollout, even when trajectories use the same software, incurring repeated memory and initialization costs as the number of parallel environments grows. Does an independent computer-use environment require an independent execution runtime? Our key observation is that trajectories require independent mutable state, while initialized application runtimes can be reused across concurrently evolving environments, making state the natural unit of environment independence. Guided by this observation, we introduce CUA-Sandbox, which separates private state capsules from shared runtimes through state-scoped execution and transactional lifecycle operations, including resets and branches, while retaining the original software interfaces and task evaluators. Experiments show comparable or improved task success relative to Docker, while substantially reducing rollout and resource costs. CUA-Sandbox achieves up to a 6.20x increase in rollout throughput, a 9.2x reduction in per-environment memory, and a 504x reduction in incremental storage.

## Metadata
- **Published**: 2026-09-26T16:16:08Z
- **Authors**: Xin Yan, Zhengbo Jiao, Jiaqi Liu, Zhenglin Wan, SiYuan Ma, Xuliang Yu, Tianyi Jiang, Chubin Zhang, Pengfei Zhou, Wangbo Zhao, Xingrui Yu, Bo An, Yang You, Ivor Tsang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32750v1)