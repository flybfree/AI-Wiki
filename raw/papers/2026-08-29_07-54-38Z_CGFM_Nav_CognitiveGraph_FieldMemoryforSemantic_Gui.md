---
title: CGFM-Nav: Cognitive Graph-Field Memory for Semantic-Guided Lifelong Multimodal Embodied Navigation
published: 2026-08-29T07:54:38Z
authors: Yuxiang Xiao, Xibei Chen, Xin Zhou, Jie Chen, Yifeng Zhang, Guillaume Sartoretti
url: http://arxiv.org/abs/2608.29114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CGFM-Nav: Cognitive Graph-Field Memory for Semantic-Guided Lifelong Multimodal Embodied Navigation

## Abstract
Vision-and-Language Navigation (VLN) requires agents to reason over accumulated observations while continuously exploring unseen regions. However, existing environment representations often struggle to jointly support explicit semantic memory and continuous exploration guidance. To address this challenge, we propose Cognitive Graph-Field Memory (CGFM), a persistent multimodal scene representation that couples explicit relational memory with continuous spatial intuition. CGFM organizes objects, spatial relations, and visual observations into a multimodal scene graph, enabling target retrieval and long-horizon reasoning across navigation tasks. When no reliable target match is identified, graph-based evidence is projected into a goal-conditioned semantic-frontier field to guide exploration toward semantically promising frontiers and regions. Building upon CGFM, we introduce CGFM-Nav, a foundation-model-based framework for lifelong multimodal navigation that integrates task-relevant subgraph selection, VLM reasoning, and verification feedback into a closed decision loop. Preliminary experiments on GOAT-Bench show that, under the same Qwen3-VL-8B backbone, CGFM-Nav improves the overall success rate from 53.2% to 63.0% and SPL from 30.0% to 39.6%, demonstrating the effectiveness of combining explicit semantic memory with semantic-guided exploration.

## Metadata
- **Published**: 2026-08-29T07:54:38Z
- **Authors**: Yuxiang Xiao, Xibei Chen, Xin Zhou, Jie Chen, Yifeng Zhang, Guillaume Sartoretti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29114v1)