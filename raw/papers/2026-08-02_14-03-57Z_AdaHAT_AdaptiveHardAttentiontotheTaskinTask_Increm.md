---
title: AdaHAT: Adaptive Hard Attention to the Task in Task-Incremental Learning
published: 2026-08-02T14:03:57Z
authors: Pengxiang Wang, Hongbo Bo, Jun Hong, Weiru Liu, Kedian Mu
url: http://arxiv.org/abs/2608.01252v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdaHAT: Adaptive Hard Attention to the Task in Task-Incremental Learning

## Abstract
Catastrophic forgetting is a major problem in task-incremental learning, where neural networks tend to overwrite previously learned knowledge when trained on new tasks. A number of architecture-based approaches have been proposed to address this problem. However, the architecture-based approaches suffer from another problem related to network capacity when the networks learn long task sequences: As a network is trained on an increasing number of new tasks in a long task sequence, a growing proportion of active parameters becomes static to prevent forgetting of previously learned knowledge. In this paper, we propose Adaptive Hard Attention to the Task (AdaHAT) with an adaptive attention mechanism which allows adaptive updates to static parameters by taking into account the information about previous tasks on both the importance of these parameters to previous tasks and the current network capacity. Based on this idea, we develop a new neural network architecture incorporating our proposed AdaHAT mechanism. AdaHAT extends an existing architecture-based approach, Hard Attention to the Task (HAT), to better support task-incremental learning over long task sequences. We conduct experiments on a number of datasets and compare AdaHAT with task-incremental learning baselines including HAT. Our experimental results show that AdaHAT achieves better average performance across tasks than these baselines, especially on long task sequences, demonstrating the benefits from balancing the trade-off between stability and plasticity of a network when learning such sequences of tasks, alleviating the network capacity problem. Our code is available at pengxiang-wang.com/projects/continual-learning-arena.

## Metadata
- **Published**: 2026-08-02T14:03:57Z
- **Authors**: Pengxiang Wang, Hongbo Bo, Jun Hong, Weiru Liu, Kedian Mu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01252v1)