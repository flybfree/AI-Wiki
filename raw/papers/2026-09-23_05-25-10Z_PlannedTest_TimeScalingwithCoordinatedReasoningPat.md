---
title: Planned Test-Time Scaling with Coordinated Reasoning Paths
published: 2026-09-23T05:25:10Z
authors: Xueqing Wu, Langxing Bai, Hritik Bansal, Po-Nien Kung, Shuo Li, Hao Liu, Nanyun Peng, Kai-Wei Chang
url: http://arxiv.org/abs/2609.27374v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Planned Test-Time Scaling with Coordinated Reasoning Paths

## Abstract
Test-time scaling with parallel branches is widely adopted to improve performance on challenging reasoning tasks. The predominant approach, repeated sampling, draws branches independently from a single policy, which can produce redundant attempts and thereby limit the gains from additional inference compute. To address this limitation, we propose Planned Test-Time Scaling (PTTS), which replaces independent sampling with a coordinated joint policy: a planner generates a solution outline for each branch, steering the branches toward distinct reasoning paths, and an executor produces a full solution conditioned on each outline. Formally, we show that PTTS strictly generalizes repeated sampling and, in a stylized setting, provably promotes coverage of complementary reasoning modes and yields better pass@k scaling. We instantiate PTTS on top of strong reasoning models, keeping them fixed as executors while replacing repeated sampling with PTTS inference to further enhance test-time scaling. Concretely, we develop two variants: PTTS-ZS prompts a model to jointly generate outlines for all branches in a single autoregressive pass, while PTTS-RL directly optimizes the planner against the pass@k reward using truncated execution rollouts for efficient training and a sharper reward signal. Across five mathematical reasoning benchmarks with Qwen3-1.7B and 4B, PTTS-ZS improves pass@64 over repeated sampling by up to 6.7 points, while PTTS-RL further increases the gain to up to 13.4 points. Further analysis indicates that broader coverage of distinct reasoning paths contributes to these gains. Overall, PTTS provides a general framework for improving test-time scaling by coordinating reasoning branches, with zero-shot and trainable instantiations that yield substantial performance gains.

## Metadata
- **Published**: 2026-09-23T05:25:10Z
- **Authors**: Xueqing Wu, Langxing Bai, Hritik Bansal, Po-Nien Kung, Shuo Li, Hao Liu, Nanyun Peng, Kai-Wei Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27374v1)