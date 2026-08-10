---
title: Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference
published: 2026-08-07T03:18:13Z
authors: Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku, Yung-Chun Chang
url: http://arxiv.org/abs/2608.06752v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference

## Abstract
This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propagation or retrieval methods that ignore structural relationships in domain knowledge. To address these limitations, we introduce an inference-only knowledge augmentation framework that dynamically constructs a User-Specific Intent Knowledge Graph from each review and aligns it with a Global Hotel Knowledge Graph through structure-aware semantic smoothing. The aligned knowledge is combined with the original review and processed by a large language model to simultaneously predict aspect ratings and generate reverse user intent statements. Experiments on TripAdvisor reviews show that DKG-MTI consistently outperforms strong LLM and retrieval-based baselines in both classification and intent generation tasks, demonstrating the effectiveness of structure-aware knowledge alignment for scalable and explainable intent inference.

## Metadata
- **Published**: 2026-08-07T03:18:13Z
- **Authors**: Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku, Yung-Chun Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06752v1)