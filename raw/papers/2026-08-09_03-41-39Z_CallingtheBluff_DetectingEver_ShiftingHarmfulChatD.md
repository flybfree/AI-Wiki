---
title: Calling the Bluff: Detecting Ever-Shifting Harmful Chat Dialogue via Ordered Reasoning Chain Regularization
published: 2026-08-09T03:41:39Z
authors: Haojie Yu, Ziyou Jiang, Junjie Wang, Mingyang Li, Yuekai Huang, Jie Huang, Qing Wang
url: http://arxiv.org/abs/2608.08451v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Calling the Bluff: Detecting Ever-Shifting Harmful Chat Dialogue via Ordered Reasoning Chain Regularization

## Abstract
Harmful chat dialogues are ever-shifting through type-shifting and lexical evasion, yet we find they share invariant principles, i.e., an Ordered Reasoning Chain (ORC) of recurring topics, harm language indicators, severity hierarchies, and type characteristics, which can help us capture the key information in the frequently changing lexical expressions. We propose BRACE, which encodes the ORC as four differentiable stages (Topic -> Indicator -> Severity -> Type) with intermediate supervision, serving as a structured regularizer blended with direct heads, and supported by prototype-based feature augmentation and feature path disentanglement. The evaluation results show that, across 4 domains and 5 harm categories, BRACE achieves harm-type macro F1 of 0.934 (RoBERTa-wwm-ext, 3-seed mean), with decoder backbones (Qwen3-1.7B LoRA) reaching 0.949. Ablation studies show that all components contribute to BRACE, and the structural decomposition of ORC enables BRACE to distinguish harmful types with semantic ambiguity. Disclaimer: This paper may contain content that is disturbing to some readers.

## Metadata
- **Published**: 2026-08-09T03:41:39Z
- **Authors**: Haojie Yu, Ziyou Jiang, Junjie Wang, Mingyang Li, Yuekai Huang, Jie Huang, Qing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08451v1)