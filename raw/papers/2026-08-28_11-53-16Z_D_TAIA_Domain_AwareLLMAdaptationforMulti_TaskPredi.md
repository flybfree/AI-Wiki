---
title: D-TAIA: Domain-Aware LLM Adaptation for Multi-Task Predictive Process Monitoring
published: 2026-08-28T11:53:16Z
authors: Sjoerd van Straten, Christine Jacob, Marwan Hassani
url: http://arxiv.org/abs/2608.28236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D-TAIA: Domain-Aware LLM Adaptation for Multi-Task Predictive Process Monitoring

## Abstract
Predictive Process Monitoring (PPM) enables organizations to forecast future process behavior, such as the next activity and remaining time of ongoing cases. In practice, three conditions cause existing methods to degrade, namely data scarcity, high process entropy and distributional shift. While Foundation Models (FMs), especially Large Language Models (LLMs), offer a new paradigm through broad sequential reasoning, adapting them to multi-task PPM under these conditions remains an open challenge. Existing FM-based approaches either lack mechanisms for handling distributional shift or rely on direct regression heads that can be structurally misaligned with continuous time prediction tasks. This paper introduces D-TAIA (Domain-aware Training and Attention-based Inference Architecture), a framework for a joint next activity and remaining time prediction task via parameter-efficient fine-tuning of an FM backbone. Our approach combines domain-aware triplet loss (DATL) pre-training with FAISS-based nearest neighbor retrieval for remaining time prediction, and adopts the TAIA inference strategy to preserve pre-trained sequential reasoning during fine-tuning. Evaluated across four real-world event logs, D-TAIA consistently shows SOTA or competitive performance compared to a fine-tuned LLM and a recurrent neural network baseline. Ablation studies confirm that techniques from NLP and computer vision can be transferred effectively to PPM with only a 10M-parameter backbone, though component contributions vary by dataset entropy.

## Metadata
- **Published**: 2026-08-28T11:53:16Z
- **Authors**: Sjoerd van Straten, Christine Jacob, Marwan Hassani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28236v1)