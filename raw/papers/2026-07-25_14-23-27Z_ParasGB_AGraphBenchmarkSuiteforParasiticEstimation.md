---
title: ParasGB: A Graph Benchmark Suite for Parasitic Estimation on AMS Circuits
published: 2026-07-25T14:23:27Z
authors: Jiajun Zou, Jiawei Liu, Ao Liu, Junnong Tian, Yibin Zhang, Chengjie Liu, Yuxi Wang, Shan Shen, Wenhua Gu, Jun Yang, Wenjian Yu
url: http://arxiv.org/abs/2607.23225v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ParasGB: A Graph Benchmark Suite for Parasitic Estimation on AMS Circuits

## Abstract
As chip manufacturing processes advance to deep submicron nodes, parasitic interconnect effects increasingly dominate the performance of analog and mixed-signal (AMS) circuits and often lead to costly layout iterations. This makes early-stage estimation of parasitic capacitance and resistance important for parasitic-aware design exploration before full physical implementation. However, progress on GNN-based parasitic modeling has been hindered by the lack of public, high-fidelity RC benchmarks that support reproducible evaluation. To address this gap, we introduce ParasGB, the first open-source benchmark suite for pre-layout parasitic parameter prediction on circuit graphs. ParasGB provides large-scale, heterogeneous RC networks extracted with commercial EDA tools from tape-out-proven designs, together with a unified evaluation protocol covering node-level ground capacitance, edge-level resistance, and edge-level coupling capacitance. Within this framework, we benchmark diverse GNN architectures using a standardized training pipeline and expose challenges such as extreme label imbalance, long-tailed parasitic distributions, and strong structural heterogeneity. By establishing a physically grounded and standardized benchmark for early-stage parasitic prediction, ParasGB provides an open platform for reproducible research on circuit graph learning and parasitic-aware model development. All datasets, preprocessing scripts, and configurations are publicly available in our code repository https://github.com/ShenShan123/ParasGB.git.

## Metadata
- **Published**: 2026-07-25T14:23:27Z
- **Authors**: Jiajun Zou, Jiawei Liu, Ao Liu, Junnong Tian, Yibin Zhang, Chengjie Liu, Yuxi Wang, Shan Shen, Wenhua Gu, Jun Yang, Wenjian Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23225v1)