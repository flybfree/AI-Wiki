---
title: Efficient Multilingual Neural Machine Translation via Corpus-Driven Vocabulary Pruning: An English-Arabic Case Study
published: 2026-08-04T11:17:54Z
authors: Ahmed Amine Aliane, Nasredine Semmar, Hassina Aliane
url: http://arxiv.org/abs/2608.03480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Multilingual Neural Machine Translation via Corpus-Driven Vocabulary Pruning: An English-Arabic Case Study

## Abstract
The adoption of large pre-trained multilingual models for neural machine translation (MNMT) faces a major challenge: excessive memory and computational consumption due to overly large vocabularies and embedding layers. Although existing compression methods like pruning, quantization and knowledge distillation reduce parameter redundancy, they mainly preserve the structure of the original vocabulary, thereby leaving a major source of inefficiency unresolved. We propose in this paper a general optimization framework that combines a vocabulary pruning method with a targeted fine-tuning protocol for MNMT models. We evaluate the proposed framework using three models (M2M100, NLLB-200, mBART-50) on the English-Arabic language pair. Our approach reduces the vocabulary size from over 128,000 to approximately 10,000 tokens, enabling a 60% memory saving without any loss in performance. Results show that optimized multilingual models can match or exceed the performance of dedicated bilingual baselines. In particular, the pruned and fine-tuned M2M100 model achieves a competitive BLEU score of 42.04 (against 44.59 for the OPUS-MTen- ar bilingual model) while it significantly outperforms it on the COMET metric (0.8730 vs 0.7911) revealing superior semantic adequacy and fluency.

## Metadata
- **Published**: 2026-08-04T11:17:54Z
- **Authors**: Ahmed Amine Aliane, Nasredine Semmar, Hassina Aliane
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03480v1)