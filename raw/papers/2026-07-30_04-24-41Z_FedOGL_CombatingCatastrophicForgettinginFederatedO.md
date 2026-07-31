---
title: FedOGL: Combating Catastrophic Forgetting in Federated Open-World Multimodal Graph Learning
published: 2026-07-30T04:24:41Z
authors: Zekai Chen, Haodong Lu, Shihao Li, Weiwei Ji, Xunkai Li, Xun Wu, Yinlin Zhu, Rong-Hua Li
url: http://arxiv.org/abs/2607.27665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FedOGL: Combating Catastrophic Forgetting in Federated Open-World Multimodal Graph Learning

## Abstract
Federated graph learning enables collaborative training over decentralized graph data without sharing raw graph information. As such risks evolve, clients must learn emerging classes from private multimodal graph streams, retain historical categories, and reject samples outside the known class space. In this setting, clients must learn emerging classes from private multimodal graph streams while preserving historical categories and rejecting samples outside the current known class space. The core challenge is catastrophic forgetting, which in federated multimodal graphs is not merely a classifier-level failure: old knowledge can be erased through modality-semantic overwriting, topology-induced structural erosion, and federated memory fragmentation. To address this challenge, we propose \textbf{FedOGL}, a semantic-structural memory preservation framework. On the client side, FedOGL preserves historical decision behavior through replay and task-start distillation, while protecting graph-propagation memory via projection onto a globally shared structure basis. On the server side, FedOGL maintains and transfers compact category prototypes to facilitate cross-client knowledge sharing without exposing raw graph data. Extensive experiments demonstrate that, compared with the best-performing baselines, FedOGL reduces performance degradation caused by catastrophic forgetting by \textbf{42.67\%}, while maintaining or improving performance on downstream tasks.

## Metadata
- **Published**: 2026-07-30T04:24:41Z
- **Authors**: Zekai Chen, Haodong Lu, Shihao Li, Weiwei Ji, Xunkai Li, Xun Wu, Yinlin Zhu, Rong-Hua Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27665v1)