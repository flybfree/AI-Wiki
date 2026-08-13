---
title: CLAIM: Leading Open-domain Active Clarification of Large Language Models with Uncertainty Measurement
published: 2026-08-12T04:27:45Z
authors: Kuangzhao Yang, Ziliang Zhao, Zhicheng Dou
url: http://arxiv.org/abs/2608.11631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CLAIM: Leading Open-domain Active Clarification of Large Language Models with Uncertainty Measurement

## Abstract
In open-domain human-computer interaction scenarios, large language models (LLMs) frequently encounter user queries that are ambiguous or incomplete. In such cases, directly producing an answer often leads to overgeneralized, erroneous, or low-information responses. In contrast, asking clarifying questions can substantially improve interaction quality. However, existing approaches still rely heavily on manually annotated data or preference alignment to address two fundamental challenges: when clarification is necessary, and which aspect of the query should be clarified. This reliance incurs high annotation costs and limits generalization. To address these challenges, we propose CLAIM, an uncertainty-driven framework for active clarification learning in open-domain settings. CLAIM eliminates the need for explicit human preference annotations by quantifying query uncertainty through the entropy induced by answer disagreements across multiple models. This uncertainty signal is then used to construct high-quality synthetic data, enabling the training of a unified clarification decision model through a combination of supervised learning and reinforcement learning. Specifically, we propose an entropy-driven synthetic data generation pipeline that integrates entropy-based uncertainty estimation with semantic clustering and reasoning-based judgments, enabling reliable automatic annotation of clarification requirements. To train CLAIM, we formulate the clarification process as a structured decision generation problem and adopt a training paradigm that combines supervised fine-tuning (SFT) with group-relative policy optimization (GRPO). Experimental results demonstrate that CLAIM can learn stable and generalizable clarification strategies without relying on manually labeled data, offering a low-cost and robust solution for proactive understanding in real-world open-domain interactions with LLMs.

## Metadata
- **Published**: 2026-08-12T04:27:45Z
- **Authors**: Kuangzhao Yang, Ziliang Zhao, Zhicheng Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11631v1)