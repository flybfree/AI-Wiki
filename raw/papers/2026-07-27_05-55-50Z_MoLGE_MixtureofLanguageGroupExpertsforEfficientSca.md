---
title: MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition
published: 2026-07-27T05:55:50Z
authors: Sangmin Lee, Woojin Chung, Woongjib Choi, Hong-Goo Kang
url: http://arxiv.org/abs/2607.24030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition

## Abstract
Massively multilingual automatic speech recognition (ASR) models covering hundreds of languages must maintain robust performance across diverse linguistic and acoustic conditions. However, these models often encounter the curse of multilinguality, where model capacity is diluted across languages. To address this challenge, we propose Mixture of Language Group Experts (MoLGE), built upon speech self-supervised models (S3Ms). MoLGE assigns dedicated expert modules to clusters of similar languages, reducing the number of required submodules compared to conventional language-specific Mixture-of-Experts (MoE) schemes. It further integrates a hierarchical Low-Rank Adaptation (LoRA) strategy into the disentangled acoustic and linguistic components of the S3M architecture, enabling efficient modeling of language-specific characteristics while maintaining parameter efficiency. Further, we investigate the impact of language grouping strategies based on both linguistic and data-driven criteria on overall performance, providing an interpretable perspective on how language structure influences scalability in multilingual speech systems. In experiments, we evaluate MoLGE on a multilingual benchmark encompassing 495 languages. Results demonstrate that MoLGE consistently outperforms dense multilingual baselines with a minimal increase in trainable parameters. Notably, these language grouping strategies yield substantial improvements for both phonetic and orthographic aspects of ASR modeling. Our findings suggest that structured language specialization provides an effective pathway for massively scaling language coverage of multilingual ASR.

## Metadata
- **Published**: 2026-07-27T05:55:50Z
- **Authors**: Sangmin Lee, Woojin Chung, Woongjib Choi, Hong-Goo Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24030v1)