---
title: BioSentinel at EXIST 2026: Soft-Label Optimization with XLM-RoBERTa for Sexism Intent Classification in Memes
published: 2026-07-27T08:18:05Z
authors: Chandru Munisamy, Karthikeya Raguveer, Alapan Kuila
url: http://arxiv.org/abs/2607.24137v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BioSentinel at EXIST 2026: Soft-Label Optimization with XLM-RoBERTa for Sexism Intent Classification in Memes

## Abstract
This paper describes the BioSentinel team's participation in EXIST 2026 Task 2.2: Source Intention in Memes, part of the CLEF 2026 evaluation campaign. The task requires classifying the communicative intent behind memes as direct, judgemental, or no (non-sexist), under a Learning with Disagreement (Le-Wi-Di) paradigm that mandates both hard-label and soft-label (probability distribution) predictions. We present a text-centric approach built on xlm-roberta-base (270M parameters) trained with a composite loss function combining KL divergence on soft annotator distributions and weighted cross-entropy on hard labels. On the official test set, the system achieved an ICM-Soft-Norm of 0.3229 and ICM-Norm of 0.3778, with a hard F1-score of 0.4236, ranking 40th (out of 118 submissions) in the soft-soft evaluation and 49th (out of 187 submissions) in the hard-hard evaluation. We provide an analysis of the dataset characteristics, exploratory larger-architecture runs, and the role of annotator disagreement in shaping model design for subjective NLP tasks. Ablation results show that KL loss improves soft-label metrics, while CE loss improves hard-label accuracy. We also report a separate validation-set temperature analysis.

## Metadata
- **Published**: 2026-07-27T08:18:05Z
- **Authors**: Chandru Munisamy, Karthikeya Raguveer, Alapan Kuila
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24137v1)