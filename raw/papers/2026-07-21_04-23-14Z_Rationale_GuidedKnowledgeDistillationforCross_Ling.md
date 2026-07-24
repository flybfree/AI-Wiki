---
title: Rationale-Guided Knowledge Distillation for Cross-Lingual Stance Detection
published: 2026-07-21T04:23:14Z
authors: Qiuli Zhou, Jingyuan Yao, Shengeng Tang, Hongzhi Chen, Jun Tang, Richang Hong
url: http://arxiv.org/abs/2607.18693v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rationale-Guided Knowledge Distillation for Cross-Lingual Stance Detection

## Abstract
Stance detection aims to identify whether a text expresses a favorable or opposing attitude toward a given target, and serves as an important task for various downstream applications. Although existing studies have achieved strong performance in monolingual settings, especially in English, many low-resource languages such as Catalan still lack sufficient annotated data for training effective models. Cross-lingual stance detection alleviates this problem by transferring stance knowledge from resource-rich languages to low-resource languages. However, most existing methods mainly rely on semantic alignment between texts and targets, while ignoring the reasoning process required for reliable stance inference. Although Large Language Models provide strong reasoning ability, their high computational cost and inference latency limit practical deployment. To address these limitations, we propose a rationale-guided knowledge distillation framework for cross-lingual stance detection. Specifically, we use Chain-of-Thought prompting to guide Large Language Models in generating informative rationales, and distill the resulting reasoning knowledge into a compact student model. We further design a dual-path distillation mechanism to align rationale-enhanced and rationale-free representations, together with their prediction distributions. In addition, two contrastive learning strategies are introduced to improve stance discrimination. Experiments on multilingual benchmarks demonstrate that our method consistently outperforms competitive baselines.

## Metadata
- **Published**: 2026-07-21T04:23:14Z
- **Authors**: Qiuli Zhou, Jingyuan Yao, Shengeng Tang, Hongzhi Chen, Jun Tang, Richang Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18693v1)