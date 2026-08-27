---
title: Are LLM-Enhanced GNNs Privacy-Safe?
published: 2026-08-26T12:42:21Z
authors: Longzhu He, Zelang Wen, Chaozhuo Li, Sen Su
url: http://arxiv.org/abs/2608.25727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are LLM-Enhanced GNNs Privacy-Safe?

## Abstract
Large language models (LLMs) have recently advanced graph neural networks (GNNs) by enriching node representations with semantic information, giving rise to LLM-enhanced GNNs that achieve substantial performance gains. However, their vulnerability to privacy attacks, in which adversaries infer sensitive information from model outputs, remains largely underexplored. To bridge this gap, we present a systematic evaluation of privacy risks in LLM-enhanced GNNs through a unified framework consisting of five stages: (1) dataset preparation, (2) victim model training, (3) privacy attack, (4) risk assessment, and (5) defense analysis. Specifically, we conduct experiments on six real-world text-attributed graph datasets covering diverse domains. We consider six representative privacy attack methods targeting three fundamental threats, namely link, label, and membership inference, and construct 42 victim model configurations by combining multiple LLM-based feature enhancers with representative GNN backbones. Extensive experiments show that, despite their utility improvements, LLM-enhanced GNNs consistently exhibit increased vulnerability to privacy attacks compared to shallow text representation baselines. Further analysis reveals that semantic enrichment amplifies link-, label-, and membership-related signals in the embedding space, making them more exploitable by inference attacks. Finally, we evaluate differential privacy as a defense strategy and show that, while it can partially mitigate privacy risks, it introduces significant utility degradation, highlighting a fundamental privacy-utility trade-off in LLM-enhanced graph learning. Overall, this work provides a comprehensive understanding of privacy risks in LLM-enhanced GNNs and offers practical insights for developing more secure and trustworthy graph learning systems.

## Metadata
- **Published**: 2026-08-26T12:42:21Z
- **Authors**: Longzhu He, Zelang Wen, Chaozhuo Li, Sen Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25727v1)