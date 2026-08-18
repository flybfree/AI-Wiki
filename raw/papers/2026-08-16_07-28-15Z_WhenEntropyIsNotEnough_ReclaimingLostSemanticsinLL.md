---
title: When Entropy Is Not Enough: Reclaiming Lost Semantics in LLM Output Length Prediction
published: 2026-08-16T07:28:15Z
authors: Feiyang Ren, Shengtao Wen, Lingbing Guo, Yu Tian, Yuanning Cui, Xiang Chen
url: http://arxiv.org/abs/2608.15592v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Entropy Is Not Enough: Reclaiming Lost Semantics in LLM Output Length Prediction

## Abstract
Efficient LLM serving is often bottlenecked by the need to pad sequences to a fixed maximum length, and this wastes compute and degrades throughput. Predicting output lengths in advance makes it possible to adopt length-aware scheduling, and this reduces the overhead. This advantage is especially pronounced in long-context reasoning and reinforcement learning applications. Existing approaches, such as entropy-guided token pooling, use token-wise entropy as their primary signal, but they tend to ignore differences in semantic content across tokens. So, important tokens are often underweighted, and tokens carrying little information receive disproportionate emphasis. This hurts the reliability of length prediction. We introduce ESTP (Entropy-and-Semantic Token Pooling), a lightweight framework that addresses this issue by combining entropy with attention-based importance scores. These scores are derived directly from the self-attention weights computed during the LLM prefill phase, and this allows ESTP to capture both uncertainty and semantic importance with minimal additional computation. Since the framework reuses prefill activations, it adds almost no extra memory overhead and introduces only minimal latency. On the ForeLen benchmark, ESTP outperforms baseline methods, achieves better prediction accuracy and lower error rates in most scenarios. When integrated with a length-aware scheduler in end-to-end system tests, it further helps improve overall throughput and reduce the padding ratio. Our results offer a practical and effective building block for length-aware LLM serving systems.

## Metadata
- **Published**: 2026-08-16T07:28:15Z
- **Authors**: Feiyang Ren, Shengtao Wen, Lingbing Guo, Yu Tian, Yuanning Cui, Xiang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15592v1)