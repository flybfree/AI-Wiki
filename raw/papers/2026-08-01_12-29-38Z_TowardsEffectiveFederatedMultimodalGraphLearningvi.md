---
title: Towards Effective Federated Multimodal Graph Learning via Navigating Multifaceted Heterogeneity
published: 2026-08-01T12:29:38Z
authors: Yinlin Zhu, Di Wu, Yi Zhang, Xunkai Li, Wang Luo, Wei-Jin Huang, Miao Hu, Guocong Quan
url: http://arxiv.org/abs/2608.00623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Effective Federated Multimodal Graph Learning via Navigating Multifaceted Heterogeneity

## Abstract
Multimodal-attributed graphs (MAGs), where nodes carry heterogeneous semantic content across multiple modalities while edges encode relational dependencies, have been widely adopted across diverse domains. Federated multimodal graph learning (FMGL) extends federated graph learning (FGL) to MAGs, enabling collaborative optimization across decentralized MAGs without exposing raw data. However, naively applying existing FGL methods to FMGL is insufficient, as they fail to navigate the multifaceted heterogeneity inherent in decentralized MAGs, including task heterogeneity across diverse client objectives, modality heterogeneity from discrepant modality quality and semantic domains, and topology heterogeneity arising from divergent topological patterns with low cross-modality correlation. To address these challenges, we propose Federated multimodal graph learning with Topology-aware Cross-modal Routing (FedTCR), the first systematic algorithm designed for FMGL. To handle task heterogeneity, FedTCR employs a two-stage paradigm that comprises federated task-agnostic pre-training followed by isolated task-oriented fine-tuning. To jointly address modality and topology heterogeneity, FedTCR introduces a topology-aware cross-modal routing mechanism. Concretely, each client distills modality-specific knowledge into compact prototypes via topology-aware importance-weighted aggregation informed by graph structure; the server then evaluates cross-client cross-modal relationships among these structure-informed prototypes and routes informative ones as contrastive references, driving a tri-level cross-modal contrastive learning scheme that jointly aligns cross-client modalities while preserving discrimination. Experiments across 7 domains demonstrate that FedTCR outperforms state-of-the-art baselines on both graph-centric and modality-centric tasks.

## Metadata
- **Published**: 2026-08-01T12:29:38Z
- **Authors**: Yinlin Zhu, Di Wu, Yi Zhang, Xunkai Li, Wang Luo, Wei-Jin Huang, Miao Hu, Guocong Quan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00623v1)