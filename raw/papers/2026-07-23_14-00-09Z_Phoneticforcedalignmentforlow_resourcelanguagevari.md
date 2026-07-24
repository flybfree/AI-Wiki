---
title: Phonetic forced alignment for low-resource language varieties: Model training and evaluation on Chengdu Mandarin
published: 2026-07-23T14:00:09Z
authors: Zhiheng Qian, Aini Li, Hai Hu, Liang Zhao
url: http://arxiv.org/abs/2607.21332v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Phonetic forced alignment for low-resource language varieties: Model training and evaluation on Chengdu Mandarin

## Abstract
Phonetic forced alignment is a key technique in phonetic research, yet existing alignment systems lack specialized models for low-resource language varieties. We address this by training text-dependent and text-independent aligners for Chengdu Mandarin using a 17-hour corpus and a custom G2P dictionary. We trained a text-dependent GMM-HMM model (Chengdu-MFA) and fine-tuned a pretrained audio encoder on frame classification with Chengdu-MFA's pseudo label for text-independent alignment (Chengdu-FC). Evaluation on an expert-annotated test set show that both methods significantly outperform Standard Mandarin baselines. Chengdu-MFA reduced average phone boundary differences by 31.8%, while Chengdu-FC achieved a 61.2% reduction. This work establishes a practical bootstrapping pipeline for developing accurate aligners for under-resourced varieties without labor- and time-intensive manual annotation.

## Metadata
- **Published**: 2026-07-23T14:00:09Z
- **Authors**: Zhiheng Qian, Aini Li, Hai Hu, Liang Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21332v1)