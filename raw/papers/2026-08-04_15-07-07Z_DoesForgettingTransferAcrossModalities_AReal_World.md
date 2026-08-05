---
title: Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation
published: 2026-08-04T15:07:07Z
authors: Chunlin Liu, Junnian Chen, Haitong Jiang, Jianyu Zhao, Yingsen Pang, Jingchen Li, Jiabiao He, Youming Lu, Jinhe Bi, Yuntao Du
url: http://arxiv.org/abs/2608.03791v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Forgetting Transfer Across Modalities? A Real-World Benchmark for Cross-Modal Knowledge Unlearning Evaluation

## Abstract
Vision-Language Models (VLMs), like Large Language Models (LLMs), may memorize sensitive, copyrighted, or harmful knowledge from their pretraining corpora. Removing such knowledge is essential for building trustworthy AI systems. However, existing studies primarily focus on forgetting within individual modalities. Although recent work has begun to explore cross-modal consistency in unlearning, the cross-modal transfer of real-world knowledge unlearning remains insufficiently studied. To address this gap, we introduce UNLINK-VL, a real-world benchmark for cross-modal knowledge unlearning in VLMs. Under a post-hoc unlearning setting in which the original forget and retain corpora are unavailable, UNLINK-VL selects visually identifiable real-world entities as unlearning targets and associates them with corresponding images and one-hop and multi-hop facts derived from Wikidata. The benchmark comprises four complementary subsets that evaluate direct forgetting of target knowledge, the propagation of forgetting through relational knowledge, the preservation of related non-target knowledge, and robustness to semantically equivalent queries. We train models under text-only and multimodal unlearning settings and evaluate forgetting effectiveness and retained utility across textual, visual, and cross-modal scenarios. Extensive experiments reveal a pronounced asymmetry in cross-modal transfer: multimodal unlearning remains effective under textual evaluation, whereas text-only unlearning transfers poorly to visual and cross-modal scenarios. Meanwhile, the evaluated methods largely preserve the models' general capabilities. These findings demonstrate that relying solely on intra-modal evaluation, particularly text-only evaluation, may substantially overestimate the effectiveness of knowledge unlearning in VLMs, underscoring the need for cross-modal unlearning and evaluation.

## Metadata
- **Published**: 2026-08-04T15:07:07Z
- **Authors**: Chunlin Liu, Junnian Chen, Haitong Jiang, Jianyu Zhao, Yingsen Pang, Jingchen Li, Jiabiao He, Youming Lu, Jinhe Bi, Yuntao Du
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03791v1)