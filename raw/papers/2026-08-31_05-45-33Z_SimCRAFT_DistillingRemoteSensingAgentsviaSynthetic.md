---
title: SimCRAFT: Distilling Remote Sensing Agents via Synthetic Trajectories and Contextual Retrieval-Augmented Fine-Tuning
published: 2026-08-31T05:45:33Z
authors: Haoran Wang, Jing Yao, Xu Yang, Zeqing Wang, Yang Zhang, Pedram Ghamisi, Zhengchao Chen
url: http://arxiv.org/abs/2608.30277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SimCRAFT: Distilling Remote Sensing Agents via Synthetic Trajectories and Contextual Retrieval-Augmented Fine-Tuning

## Abstract
The unprecedented surge in Earth observation data volume and diversity has exposed a critical bottleneck for traditional manual workflows, catalyzing the emergence of Remote Sensing (RS) Agents. However, the practical deployment of these advanced agents is severely hindered by their heavy reliance on large-scale general-purpose LLMs, which lack deep domain expertise and impose prohibitive infrastructure demands. To resolve this, we propose SimCRAFT, a model-agnostic framework that distills sophisticated RS orchestration capabilities into a compact 7B-scale model. Addressing data scarcity, we first pair a multiagent synthesis engine with a Mock Execution Engine that checks schema correctness, inter-tool dependencies, and sensor/tool compatibility, producing SimRS-14k, a large-scale, constraint-validated workflow planning corpus. Second, we propose Contextual Retrieval-Augmented Fine-Tuning (CRAFT) that finetunes the model to reason analogically by adapting retrieved Standard Operating Procedures to novel queries under a noise-robust objective, generalizing RAFT to multi-step RS workflow planning without mechanical copying. Extensive experiments demonstrate that SimCRAFT-7B significantly outperforms openweights LLMs and rivals advanced closedsource models and specialized RS agents, while reproducing across three 7B backbones. This work contributes a competitive open-weights baseline for lightweight RS intelligence, enabling efficient autonomous deployment under resource-constrained or resource-conserving conditions.

## Metadata
- **Published**: 2026-08-31T05:45:33Z
- **Authors**: Haoran Wang, Jing Yao, Xu Yang, Zeqing Wang, Yang Zhang, Pedram Ghamisi, Zhengchao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30277v1)