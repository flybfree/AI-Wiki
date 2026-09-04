---
title: PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing
published: 2026-09-03T08:04:30Z
authors: Yangshuo Qi, Chenwei Wang, Zihan Shen, Songlin Sun
url: http://arxiv.org/abs/2609.03503v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing

## Abstract
With the rapid development of the Internet of Things, computation intensive directed acyclic graph (DAG) tasks have become increasingly common in cloud-edge-end collaborative environments. However, cloud, edge, and end nodes are highly heterogeneous in computing capacity, network bandwidth, and energy consumption, which makes the efficient scheduling of tasks with complex dependencies an NP-hard problem. Traditional heuristic algorithms and conventional reinforcement-learning methods often fail to capture the spatio-temporal dynamics of system resources. This paper proposes PPO-STGNN, a DAG task-scheduling algorithm that integrates proximal policy optimization (PPO) with spatio-temporal graph neural networks (STGNNs). The method uses an STGNN to extract features from both the DAG task topology and the physical cloud-edge-end resource graph, and then optimizes the scheduling policy through PPO to minimize makespan and schedule length ratio (SLR) while improving CPU and memory load balancing. To accelerate convergence, a multi-teacher behavior-cloning mechanism is introduced for pretraining. Experimental results show that PPO-STGNN significantly improves load balancing while maintaining a low completion time, making it suitable for dynamic and heterogeneous cloud-edge- end DAG scheduling scenarios.

## Metadata
- **Published**: 2026-09-03T08:04:30Z
- **Authors**: Yangshuo Qi, Chenwei Wang, Zihan Shen, Songlin Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03503v1)