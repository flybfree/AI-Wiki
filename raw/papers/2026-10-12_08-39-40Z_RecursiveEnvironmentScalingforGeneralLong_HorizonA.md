---
title: Recursive Environment Scaling for General Long-Horizon Agents
published: 2026-10-12T08:39:40Z
authors: Lingxiao Jing, Zhengbo Jiao, Yichen Xiang, Bofan Zhu, Lingbei Meng, Yan Ni, Haorui Chen, Ran Ran, Zhirong Shen, Yuheng Yang, Chenhang Cui, Yaosong Du, Rui Huang
url: http://arxiv.org/abs/2610.16397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recursive Environment Scaling for General Long-Horizon Agents

## Abstract
We study environment scaling as a way to increase agent-benchmark difficulty while holding core task objectives fixed. Our framework, Recursive Environment Scaling (RES), transforms existing benchmark environments while preserving their objectives and completion requirements. A proposer changes information access, resource relations, and execution dependencies; execution-grounded checks validate the resulting candidate, and accepted changes are inherited across rounds. This produces related environments for paired evaluation and training-trajectory collection. Experiments on 294 initial tasks from three benchmarks show lower task success for all six evaluation models, with decreases of 57.14--77.14 percentage points on Claw-Eval-Live. With equal trajectory counts and identical optimization settings, fine-tuning on RES trajectories outperforms original-trajectory SFT in all nine model--benchmark comparisons by 7.00--14.61 percentage points. Ablations identify recursive inheritance and dependency composition as important contributors to increased difficulty. Together, these results support environment scaling for both agent evaluation and training.

## Metadata
- **Published**: 2026-10-12T08:39:40Z
- **Authors**: Lingxiao Jing, Zhengbo Jiao, Yichen Xiang, Bofan Zhu, Lingbei Meng, Yan Ni, Haorui Chen, Ran Ran, Zhirong Shen, Yuheng Yang, Chenhang Cui, Yaosong Du, Rui Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16397v1)