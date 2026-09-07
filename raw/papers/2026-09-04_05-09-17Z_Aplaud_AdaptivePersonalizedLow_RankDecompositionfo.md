---
title: Aplaud: Adaptive Personalized Low-Rank Decomposition for User-Specific LLM
published: 2026-09-04T05:09:17Z
authors: Xinyu Li, Ruoming Jin, Jianfeng Zhu, Ruixin Guo, Zhi Liu
url: http://arxiv.org/abs/2609.04738v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aplaud: Adaptive Personalized Low-Rank Decomposition for User-Specific LLM

## Abstract
In this paper, we study the problem of personalized survey response prediction using fine-tuned large language models (LLMs). This task poses unique challenges: limited per-user training data, scalability of model storage, and the need to exploit shared structure across survey questions. To address these issues, we propose Aplaud (Adaptive Personalized Low-rank and User-specific Nested Decomposition), a lightweight and scalable framework for LLM personalization. Aplaud extends the LoRA paradigm by separating adaptation into a frozen, shared low-rank basis and a compact user-specific correction, augmented with a rank-one residual for finer personalization. To further reduce per-user parameter cost and mitigate overfitting, the correction matrix can be factorized into an even lower-rank form. Empirical results demonstrate that Aplaud achieves efficient, scalable personalization across users while outperforming state-of-the-art LoRA-based personalized LLM approaches in both generalization and inference efficiency.

## Metadata
- **Published**: 2026-09-04T05:09:17Z
- **Authors**: Xinyu Li, Ruoming Jin, Jianfeng Zhu, Ruixin Guo, Zhi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04738v1)