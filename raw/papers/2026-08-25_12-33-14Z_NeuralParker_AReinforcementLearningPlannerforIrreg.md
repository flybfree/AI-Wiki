---
title: NeuralParker: A Reinforcement Learning Planner for Irregular Parking Environments
published: 2026-08-25T12:33:14Z
authors: Zihan Wang, Bai Huang, Yang Guan, Xiao Li, Haoyu Xu, Naizheng Wang, Shengbo Eben Li
url: http://arxiv.org/abs/2608.24485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuralParker: A Reinforcement Learning Planner for Irregular Parking Environments

## Abstract
Automated parking commonly assumes marked slots and short approach maneuvers. Delivery and service vehicles, however, may need to reach an operator-specified pose in an irregular bounded environment from a distant start. Existing learning-based parking planners often rely on local observations, which can restrict long-range route reasoning. To address this problem, we present NeuralParker, a reinforcement learning-based hybrid planner for arbitrary-pose parking. NeuralParker encodes full-environment obstacle and boundary geometry in a target-relative vertex representation, allowing the policy to retain route-defining context throughout the approach. It further couples a learned curvature--length arc policy with an in-loop terminal ensemble that selects from diverse cubic Hermite connections using a curvature-regularized cost. We also establish factorial and long-range route-choice benchmarks to evaluate planning success and trajectory quality. Experiments on these benchmarks show that NeuralParker achieves higher planning success and better overall trajectory quality than the evaluated baselines, while ablation studies support the benefits of the target-relative global representation and terminal ensemble. Finally, a real-vehicle evaluation confirms that the planner transfers effectively to real delivery-vehicle perception at a working parking site, planning successfully at low computational cost.

## Metadata
- **Published**: 2026-08-25T12:33:14Z
- **Authors**: Zihan Wang, Bai Huang, Yang Guan, Xiao Li, Haoyu Xu, Naizheng Wang, Shengbo Eben Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24485v1)