---
title: Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach
published: 2026-07-21T00:34:42Z
authors: Zijiang Yan, Hao Zhou, Wael Jaafar, Jianhua Pei, Ping Wang, Halim Yanikomeroglu, Hina Tabassum
url: http://arxiv.org/abs/2607.18604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach

## Abstract
The deployment of high-speed Uncrewed Aerial Vehicles (UAVs) in 3D aerial highways necessitates robust coordination of physical flight kinematics and multi-tier network handovers. While Deep Reinforcement Learning (DRL) offers rapid tactical control, it lacks the zero-shot strategic reasoning required to quickly adapt to dynamic Integrated Terrestrial and Non-Terrestrial Networks (ITNTNs). Conversely, Large Language Models (LLMs) excel at semantic reasoning but suffer from high inference latency, rendering them unsuitable for real-time aerodynamic control. To bridge this gap, we propose a novel Hierarchical LLM-driven control framework. A massive cloud-based LLM deployed on a High-Altitude Platform Station (HAPS) manages slow-timescale global load balancing, while lightweight edge-LLMs on individual UAVs translate local observations into tactical sub-goals. These sub-goals guide a fast-timescale physical DRL controller to execute collision-free, handover-aware trajectories. Simulation results demonstrate that our agentic architecture significantly reduces collision rates and improves aggregate system throughput compared to existing baselines.

## Metadata
- **Published**: 2026-07-21T00:34:42Z
- **Authors**: Zijiang Yan, Hao Zhou, Wael Jaafar, Jianhua Pei, Ping Wang, Halim Yanikomeroglu, Hina Tabassum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18604v1)