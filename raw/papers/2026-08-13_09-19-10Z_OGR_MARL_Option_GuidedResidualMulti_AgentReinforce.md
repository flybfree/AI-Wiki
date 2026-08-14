---
title: OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways
published: 2026-08-13T09:19:10Z
authors: Mao Jiayang, Wang Lanfeng, Peng Zhao-Han
url: http://arxiv.org/abs/2608.12995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways

## Abstract
Heterogeneous USV cooperative pursuit in constrained port waterways requires evader interception under navigation, traffic, and role constraints. This paper proposes OGR-MARL, an option-guided residual multi-agent reinforcement learning framework that is decoupled from a specific MARL algorithm. OGR-MARL integrates shared evader belief, role-conditioned option targets, adaptive rule penalties, and residual policy learning, allowing different MARL algorithms to learn corrective actions on top of rule-guided behaviors rather than exploring constrained port environments from scratch. We instantiate OGR-MARL with representative continuous-control MARL backbones, including MADDPG, MATD3, MAPPO, and MASAC, yielding OGR-MADDPG, OGR-MATD3, OGR-MAPPO, and OGR-MASAC. Experiments in an abstract Xiazhimen port-waterway scenario show that the OGR-MASAC instantiation achieves a 75.0% capture rate, promising mission-effective rule compliance, and the best heterogeneous coordination among the tested methods. Without retraining, zero-shot transfer to a QGIS/AIS-informed Xiazhimen map achieves promising results, demonstrating the generalization potential of OGR-MARL in more complex port scenarios.

## Metadata
- **Published**: 2026-08-13T09:19:10Z
- **Authors**: Mao Jiayang, Wang Lanfeng, Peng Zhao-Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12995v1)