---
title: TALSC: Timeliness-Aware Large-Small VLM Collaboration for Infrastructure-Assisted Autonomous Driving
published: 2026-08-03T09:58:20Z
authors: Mengmeng Zhu, Yuxuan Sun, Wei Chen, Bo Ai
url: http://arxiv.org/abs/2608.01998v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TALSC: Timeliness-Aware Large-Small VLM Collaboration for Infrastructure-Assisted Autonomous Driving

## Abstract
The deployment of Vision-Language Models (VLMs) in autonomous driving (AD) systems is constrained by on-board computing power, restricting vehicles to small VLMs (SVLMs) with limited perception and reasoning capabilities. Infrastructure-assisted AD alleviates this resource constraint by enabling collaboration with large VLMs (LVLMs) at edge servers. However, in dynamic vehicular environments, the utility of sensory data for downstream tasks decays rapidly, making timeliness of information a critical concern. To balance the accuracy gains of LVLMs with their latency-induced timeliness degradation, we develop a Timeliness-Aware Large-Small VLM Collaboration (TALSC) framework. Specifically, we first model the Age of Information (AoI) evolution for VLM inference and characterize the coupling among AoI, token length, and task performance to formulate a general timeliness metric. Building on this, we propose the TALSC online scheduling algorithm. Since scheduling decisions have a delayed impact on future timeliness metric and the output token number is unknown at scheduling time, we design a Lyapunov drift-plus-estimated-penalty algorithm and provides a guaranteed performance. In simulation, we first conduct a case study to derive a fitted timeliness metric based on nuScenes dataset, and further show that TALSC outperforms baselines under various communication and computing settings, achieving up to a 12.6\% normalized improvement in Micro-F1 score compared with the best-performing baseline.

## Metadata
- **Published**: 2026-08-03T09:58:20Z
- **Authors**: Mengmeng Zhu, Yuxuan Sun, Wei Chen, Bo Ai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01998v1)