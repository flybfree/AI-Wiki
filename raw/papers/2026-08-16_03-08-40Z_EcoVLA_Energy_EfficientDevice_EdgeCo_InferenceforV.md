---
title: EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints
published: 2026-08-16T03:08:40Z
authors: Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao, Lingkun Long, Chunming Hu, Jianlei Yang
url: http://arxiv.org/abs/2608.15502v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints

## Abstract
Vision-Language-Action (VLA) models have emerged as a promising foundation for Embodied AI, but their high inference cost poses significant challenges for deployment in robotic systems. In practice, on-device inference is constrained by limited compute capacity and energy budgets, struggling to simultaneously satisfy real-time control and energy efficiency requirements. Alternatively, offloading the inference workload to an edge server is susceptible to fluctuations in system conditions, introducing unpredictable latency risks. Device-edge co-inference offers a promising solution, but systematic research tailored to VLA models remains scarce, particularly a unified co-inference framework that jointly addresses real-time constraints and system-level energy efficiency. Thus, we propose EcoVLA, an adaptive device-edge co-inference framework for VLA models that maximizes system energy efficiency under real-time constraints. EcoVLA first introduces a unified stage-level abstraction over different VLA paradigms, establishing an architecture-agnostic co-inference design space. It then formulates a joint device-edge-network latency and energy prediction model to enable rapid runtime evaluation of candidate co-inference schemes. Building on this, EcoVLA continuously selects the energy-optimal scheme satisfying real-time constraints with millisecond-level overhead, adapting to runtime variations in network and system states. Furthermore, EcoVLA incorporates a lightweight transmission mechanism for inter-stage intermediate tensors to reduce the communication overhead incurred by cross-device collaboration. Experimental results across VLA models show that EcoVLA improves system energy efficiency by up to 236% over existing co-inference approaches under a 20 Hz action output frequency constraint, while consistently maintaining SLO satisfaction under dynamic network and edge workload conditions.

## Metadata
- **Published**: 2026-08-16T03:08:40Z
- **Authors**: Ao Zhou, Bo Dai, Le Yu, Xingyu Liu, Zeyu Hao, Lingkun Long, Chunming Hu, Jianlei Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15502v1)