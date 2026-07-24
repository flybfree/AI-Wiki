---
title: TAPAS: Throughput-adaptive Perception for Autonomous Systems
published: 2026-07-19T16:01:11Z
authors: Aman Vyas, Vasista Kodumagulla, Zain Taufique, Pasi Liljeberg, Anil Kanduri
url: http://arxiv.org/abs/2607.17317v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TAPAS: Throughput-adaptive Perception for Autonomous Systems

## Abstract
Autonomous systems rely on a perception module to navigate through dynamic environments. In real-world scenarios, the perception module's throughput requirements vary at runtime due to changes in scene complexity. However, existing perception strategies assume a fixed FPS and static model-to-cluster mapping, resulting in either over/under provision of throughput requirements or unnecessary energy consumption across diverse scenes. Addressing this challenge requires tightly coupled \textit{scene complexity awareness} to estimate an appropriate FPS target and \textit{dynamic model-to-cluster mapping} to deliver the required throughput at minimum energy. We propose a throughput-adaptive perception strategy for mobile/edge platforms, enabling intelligent runtime resource allocation based on varying FPS targets. We use Reinforcement Learning (RL) with RRM (Reward Reasoning Model) and a GRU (Gated Recurrent Unit) agent to orchestrate perception tasks across heterogeneous mobile/edge platforms. We evaluate TAPAS on Jetson Orin NX across KITTI and unseen nuScenes. On the \textit{KITTI} dataset's test sequences, TAPAS achieves 93-100% throughput met rate while saving energy by 76%. On the unseen \textit{nuScenes} dataset, TAPAS maintains 97% throughput met rate with 64% lower energy compared to \textit{SOTA} approaches, proving its robustness.

## Metadata
- **Published**: 2026-07-19T16:01:11Z
- **Authors**: Aman Vyas, Vasista Kodumagulla, Zain Taufique, Pasi Liljeberg, Anil Kanduri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17317v1)