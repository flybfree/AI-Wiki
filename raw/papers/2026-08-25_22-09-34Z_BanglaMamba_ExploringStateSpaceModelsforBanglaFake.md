---
title: BanglaMamba: Exploring State Space Models for Bangla Fake News Detection
published: 2026-08-25T22:09:34Z
authors: M. K. Khalidi Siam
url: http://arxiv.org/abs/2608.25190v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BanglaMamba: Exploring State Space Models for Bangla Fake News Detection

## Abstract
Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media. While transformer-based models such as BanglaBERT achieve strong performance for Bangla text classification, their quadratic computational complexity makes them less suitable for long-document processing in resource-constrained environments. This paper investigates Mamba-based State Space Models (SSMs) as an efficient alternative for Bangla fake news detection. We propose BanglaMamba and compare it with pre-trained BanglaBERT and a similarly configured BERT model trained from scratch. Experimental results show that BanglaBERT achieves the highest Macro-F1 score (0.9260), while BanglaMamba (0.9029) achieves performance comparable to the from-scratch CustomBERT (0.9057) despite using a different architecture. Meanwhile, BanglaMamba achieves approximately $2.2\times$ higher inference throughput and 49% lower inference peak GPU memory usage than the BERT-based models. Cross-dataset evaluation shows that BanglaBERT generalizes better to an external dataset, highlighting the importance of large-scale pretraining. These findings demonstrate that Mamba-based SSMs can provide a competitive and computationally efficient alternative to Transformer-based architectures for Bangla fake news detection, particularly in resource-constrained settings.

## Metadata
- **Published**: 2026-08-25T22:09:34Z
- **Authors**: M. K. Khalidi Siam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25190v1)