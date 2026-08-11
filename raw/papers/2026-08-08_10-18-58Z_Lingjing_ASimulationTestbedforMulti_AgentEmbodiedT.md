---
title: Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities
published: 2026-08-08T10:18:58Z
authors: Xiaohe Li, Yiru Wang, Junhao Fan, Mingyuan Liu, Jie Huang, Kaixin Zhang, Jiahao Li, Chen Qian, Zide Fan
url: http://arxiv.org/abs/2608.08045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities

## Abstract
Urban embodied intelligence requires coordination among heterogeneous agents (e.g., UAVs, ground robots, and autonomous vehicles) in dynamic cities. Simulators therefore provide a scalable foundation for developing and evaluating such coordination. Existing platforms nevertheless isolate different embodiments and decouple them from task design and evaluation. We present \textbf{Lingjing}, a simulation platform for heterogeneous multi-agent embodied intelligence in open-ended urban environments. Lingjing reconstructs and renders evolving cities from geographic data, synchronizes multiple physics engines, and exposes shared physical and structured urban state to agents. Its Gym-like interface supports user-defined ReAct agents and single- or multi-agent natural-language missions with configurable star or broadcast communication and resource constraints. Each episode becomes an attribution-ready replay that links agent trajectories and communication to relation-graph changes, resource consumption, and engine-based evaluations for systematic diagnosis. We evaluate twelve vision-language models on nine urban tasks under a shared engine-in-the-loop protocol. Controlled studies further examine communication, scalability, robustness, and failure provenance. Results expose persistent bottlenecks in grounding and long-horizon execution. They also show task-dependent coordination trade-offs and diminishing returns from added capacity, while heavier workloads further reduce success. Lingjing provides a unified testbed that enables reproducible end-to-end evaluation and systematic failure diagnosis in urban multi-agent embodied intelligence.

## Metadata
- **Published**: 2026-08-08T10:18:58Z
- **Authors**: Xiaohe Li, Yiru Wang, Junhao Fan, Mingyuan Liu, Jie Huang, Kaixin Zhang, Jiahao Li, Chen Qian, Zide Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08045v1)