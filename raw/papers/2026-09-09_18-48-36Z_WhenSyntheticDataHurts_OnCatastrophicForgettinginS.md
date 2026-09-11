---
title: When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents
published: 2026-09-09T18:48:36Z
authors: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund
url: http://arxiv.org/abs/2609.10750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents

## Abstract
LLM agents increasingly rely on external skills retrieved at runtime, making skill selection from large repositories a critical challenge. We present a production skill router over 34,396 skills and a large-scale study of skill retrieval using limited real supervision and synthetic data. We found that the synthetic-data fine-tuning improves in-distribution retrieval but it causes catastrophic forgetting on real and out-of-distribution (OOD) data. We evaluate several forgetting mitigation fine-tuning approaches inspired by continual learning, including embedding-anchor regularization, Learning without Forgetting (LwF), Elastic Weight Consolidation (EWC), and L2-initialization. The results show that these approaches not only retain the performance on OOD skills retrieval but also improve the retrieval on synthetic in-distribution skills by 13.98\% for 0.6B Qwen retriever and reranker. Our results provide a practical benchmark and a robust fine-tuning recipe for scarce, multi-positive supervision.

## Metadata
- **Published**: 2026-09-09T18:48:36Z
- **Authors**: Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.10750v1)