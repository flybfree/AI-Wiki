---
title: StanceFlip: A Comprehensive Multi-Dimensional Benchmark for Multimodal Conversational Stance Flipping Forecasting
published: 2026-07-27T09:11:56Z
authors: Heyan Chai, Xin Li, Wenjie Wang, Jianyang Qin, Chaoyang Li, Lu Wang, Hao Chen, Qing Liao
url: http://arxiv.org/abs/2607.24191v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StanceFlip: A Comprehensive Multi-Dimensional Benchmark for Multimodal Conversational Stance Flipping Forecasting

## Abstract
Conversational stance detection has shifted from static text analysis to dynamic multimodal modeling. However, existing benchmarks exhibit three key limitations: failure to capture the dynamic evolution of beliefs, particularly during stance reversals; difficulty in disentangling affective states from logical reasoning; and neglect of the critical role of multimodal cues in resolving pragmatic ambiguities such as sarcasm. To address these limitations, we propose StanceFlip, a benchmark designed for multimodal conversational stance flipping forecasting over multi-turn dialogues across five modalities and multi-scenarios, which includes two novel subtasks: 1) Multimodal Stance Sextuple Extraction, extracting holder, target, emotion, sentiment, stance, and rationale as static state snapshots of dialogue to capture fine-grained cognitive structures. 2) Dynamic Stance Flip Attribution, tracking stance reversals across the conversation and identifying their underlying triggers. Alongside the dataset, we propose a dedicated framework, named ConStaFF, for Multimodal Conversational Stance Flipping Forecasting (MCSFF). Built upon a large language model, ConStaFF performs end-to-end stance reasoning, with a Thought-of-Stance (ToS) reasoning framework and a self-reflective verification mechanism integrated for structured stance modeling and faithful flip attribution. Specifically, ToS decomposes the reasoning process into specialized cognitive personas to formulate target propositions, resolve cross-modal conflicts, and infer historical stance trajectories. Extensive experiments show that our approach achieves state-of-the-art performance on both sextuple extraction and flip-trigger attribution, outperforming strong multimodal large language model baselines by substantial margins.

## Metadata
- **Published**: 2026-07-27T09:11:56Z
- **Authors**: Heyan Chai, Xin Li, Wenjie Wang, Jianyang Qin, Chaoyang Li, Lu Wang, Hao Chen, Qing Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24191v1)