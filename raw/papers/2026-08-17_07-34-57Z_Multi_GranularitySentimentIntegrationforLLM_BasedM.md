---
title: Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis
published: 2026-08-17T07:34:57Z
authors: Shanshan Lin, Yuesheng Wu, Chao Chen, Yizhe Yang, Zhihao Chen, Zexian Yang, Xiangwen Liao
url: http://arxiv.org/abs/2608.16201v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis

## Abstract
Multimodal sentiment analysis (MSA) aims to predict sentiment polarity and intensity from heterogeneous inputs such as text, audio, and vision. While large language models (LLMs) offer strong semantic priors for MSA, effectively incorporating audio and visual signals effectively remains challenging. A key challenge is that audio and visual sentiment cues evolve over different temporal scales, yet many LLM-based methods compress these signals through shallow projection or coarse pooling before fusing them with text, which can weaken cross-modal alignment and erase fine-grained affective information. We propose MGSI, a multi-granularity sentiment integration framework for LLM-based MSA. MGSI first encodes audio and visual streams at short-, medium-, and long-range temporal scales, preserving both local variations and global affective trends. It then refines non-text features through text-guided alignment, and applies polarity- and intensity-aware enhancement to better handle ambiguous and near-neutral samples. The resulting multimodal representation is finally compressed into a small set of pseudo-tokens for efficient conditioning of a frozen LLM. Experiments on four public benchmarks show that MGSI substantially outperforms frozen-LLM baselines and remains competitive with strong multimodal methods. Further ablation and sensitivity analyses support the effectiveness of multi-granularity temporal modeling, text-guided refinement, and adaptive sentiment calibration.

## Metadata
- **Published**: 2026-08-17T07:34:57Z
- **Authors**: Shanshan Lin, Yuesheng Wu, Chao Chen, Yizhe Yang, Zhihao Chen, Zexian Yang, Xiangwen Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16201v1)