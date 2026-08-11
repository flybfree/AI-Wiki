---
title: ML-Based Hierarchical Prediction for Practical Energy Scheduling in Dynamic NTN-WPT Systems
published: 2026-08-09T16:41:13Z
authors: Zhanyu Ju, Wenchi Cheng
url: http://arxiv.org/abs/2608.08804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ML-Based Hierarchical Prediction for Practical Energy Scheduling in Dynamic NTN-WPT Systems

## Abstract
With advancements in long-distance wireless power transfer (WPT) and space-based energy technologies, integrating WPT into non-terrestrial networks (NTNs), referred to as NTN-WPT, is emerging as a promising approach for next-generation wireless networks. This paper proposes an energy-scheduling approach that jointly optimizes energy efficiency, task completion rate, and task waiting time for power transfer from low Earth orbit satellites to terrestrial mobile user devices (UDs). To address scheduling challenges caused by satellite and UD mobility and channel uncertainty from stochastic propagation effects, we decompose the problem into three subproblems within a three-layer predictive framework: 1) a state prediction layer forecasts UD and satellite states; 2) an interaction mapping layer uses a graph neural network (GNN) to model energy transfer efficiency; and 3) a decision-making layer determines the energy allocation plan. Distinct machine learning (ML) methods are tailored to each layer. To balance the competing objectives, we adopt a multi-objective reinforcement learning (MORL) technique that scalarizes them into a weighted-sum reward, transforming the multi-objective problem into a tractable single-objective problem. We further introduce a multi-agent deep learning model integrating self-attention with multi-agent proximal policy optimization (MAPPO) to improve objective balancing. Simulation results show that the proposed approach achieves a better overall trade-off than baseline methods, maintaining competitive task completion rates and energy efficiency while reducing task waiting times, and remains robust under highly variable conditions.

## Metadata
- **Published**: 2026-08-09T16:41:13Z
- **Authors**: Zhanyu Ju, Wenchi Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08804v1)