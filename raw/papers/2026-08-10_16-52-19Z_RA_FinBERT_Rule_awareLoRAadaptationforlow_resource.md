---
title: RA-FinBERT: Rule-aware LoRA adaptation for low-resource financial sentiment classification
published: 2026-08-10T16:52:19Z
authors: Fan Zhang, Jiaming Li
url: http://arxiv.org/abs/2608.09834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RA-FinBERT: Rule-aware LoRA adaptation for low-resource financial sentiment classification

## Abstract
Financial sentiment analysis converts unstructured financial news into quantitative signals that can support market analysis and decision-making. Existing work on resource-efficient financial NLP has largely focused on compressing or adapting pretrained language models, with less attention to combining contextual representations with lightweight rule-derived features. This study develops Rule-Aware FinBERT (RA-FinBERT), a parameter-efficient framework that integrates low-rank adaptation (LoRA) with three continuous VADER-derived sentiment proportions (positive, negative, and neutral) and a source-level metadata feature. The standardized four-dimensional feature vector is directly concatenated with the 768-dimensional final-layer FinBERT [CLS] representation and passed through a lightweight classification head. This design introduces only 1,024 additional trainable weights relative to a structurally matched text-only FinBERT model. RA-FinBERT was evaluated against text-only FinBERT and a lightweight DistilBERT baseline for three-class sentiment classification of financial-news titles and descriptions. On the held-out test set, RA-FinBERT achieved 69.89% accuracy and a macro F1 score of 0.634, compared with 63.44% and 0.526 for text-only FinBERT. Neutral-class recall increased from 18.18% to 45.45%. The framework supports both CPU and GPU execution, offering a lightweight and practical approach to financial sentiment classification under constrained computational resources. These findings indicate that rule-derived sentiment information and source metadata can provide complementary signals to contextual FinBERT representations and improve performance with minimal additional model complexity.

## Metadata
- **Published**: 2026-08-10T16:52:19Z
- **Authors**: Fan Zhang, Jiaming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09834v1)