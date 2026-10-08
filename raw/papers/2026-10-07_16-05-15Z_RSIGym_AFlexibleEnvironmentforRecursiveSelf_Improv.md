---
title: RSIGym: A Flexible Environment for Recursive Self-Improvement
published: 2026-10-07T16:05:15Z
authors: Fanqing Meng, Lingxiao Du, Haocheng Lu, Qiguang Chen, Ziqi Zhao, Zijian Wu, Jiayuan Zhuo, Mengkang Hu, Michael Qizhe Shieh
url: http://arxiv.org/abs/2610.10310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RSIGym: A Flexible Environment for Recursive Self-Improvement

## Abstract
Recursive self-improvement requires carrying accepted changes into later improvement cycles, while studying agent-proposed changes also requires substantial research infrastructure. Existing settings often leave agents to rebuild routine infrastructure or restrict exploration to individual components. We introduce RSIGym, an agent-native research environment based on Everything as a Service (EaaS). RSIGym exposes training, inference, rollout, evaluation, and sandbox execution through reusable services, with shared budget and permission controls supporting Data, Harness, and Joint improvement tracks. This design enables agents to investigate individual interventions and jointly optimize data, training settings, and execution harnesses within the same environment. We define RSI-Index as the mean fraction of the remaining performance gap closed across five benchmarks covering software engineering, terminal interaction, mathematics, scientific reasoning, and skill-based tasks. Comparing six frontier research models in independent Joint runs, Opus 5 achieves the highest RSI-Index of 0.4809 under a $500 platform-service budget per benchmark run. Its selected systems improve all five benchmarks, raising SWE-bench Verified from 17.67% to 50.33% and AIME from 31.67% to 97.78%. Additional experiments examine DSH-harness refinement, budget variation, and restricted network access, while recorded trajectories reveal how agents diagnose failures and select candidates. We open-source the full RSIGym codebase and results to support reproducibility and further research.

## Metadata
- **Published**: 2026-10-07T16:05:15Z
- **Authors**: Fanqing Meng, Lingxiao Du, Haocheng Lu, Qiguang Chen, Ziqi Zhao, Zijian Wu, Jiayuan Zhuo, Mengkang Hu, Michael Qizhe Shieh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10310v1)