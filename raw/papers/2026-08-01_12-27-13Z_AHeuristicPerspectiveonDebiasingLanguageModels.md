---
title: A Heuristic Perspective on Debiasing Language Models
published: 2026-08-01T12:27:13Z
authors: Tian Lan, Yemin Wang, Chuancheng Shi, Xiangyu Wu, Zesheng Shi, Yuan Wang, Jiang Li, Guanglai Gao, Xiangdong Su
url: http://arxiv.org/abs/2608.00622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Heuristic Perspective on Debiasing Language Models

## Abstract
Language models (LMs) often acquire various biases during pre-training and may express them in interactions, potentially causing social harm. Existing methods often rely on counterfactual augmentation or representation projection. These strategies remain limited in practice due to their high computational costs and difficulty in scaling to larger models. Additionally, many of these strategies require manual data annotation, narrowing their scope to specific cultures and bias categories. To overcome these limitations, we propose HEIMAT, a HEurIstic-style autoMATic debiasing framework for LMs. HEIMAT consists of two main steps: bias disclosure and debiasing fine-tuning. In the first step, it uses simple templates to construct heuristic prompts, which are applied to reveal model biases and generate corresponding context prompts. In the second step, it fine-tunes the model by minimizing the Jensen-Shannon divergence of predictions on these context prompts to reduce bias. Extensive experiments show that HEIMAT effectively mitigates bias in different cultures while maintaining the model's natural language understanding (NLU) performance.

## Metadata
- **Published**: 2026-08-01T12:27:13Z
- **Authors**: Tian Lan, Yemin Wang, Chuancheng Shi, Xiangyu Wu, Zesheng Shi, Yuan Wang, Jiang Li, Guanglai Gao, Xiangdong Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00622v1)