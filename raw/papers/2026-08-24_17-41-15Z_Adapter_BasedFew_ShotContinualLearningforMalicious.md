---
title: Adapter-Based Few-Shot Continual Learning for Malicious Packet Recognition
published: 2026-08-24T17:41:15Z
authors: Kyle Stein, Guillermo Francia, III Eman El-Sheikh, Andrew Arash Mahyari
url: http://arxiv.org/abs/2608.23536v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adapter-Based Few-Shot Continual Learning for Malicious Packet Recognition

## Abstract
The continual evolution of malware variants necessitates detection systems that can adapt to new threats without retraining from scratch. However, continually updating models on new data often leads to catastrophic forgetting, where previously learned knowledge is overwritten. While continual learning has been increasingly explored for malware detection, the specific setting of Few-Shot Class-Incremental Learning (FSCIL), where new malware classes must be learned from only a small number of labeled examples, remains comparatively underexplored. Therefore, this work investigates the FSCIL setting for malware classification. To address the stability-plasticity dilemma, we propose a hybrid framework that leverages a Self-Supervised Learning (SSL) backbone initialized through domain-specific pre-training on malware packets. Our method incorporates Low-Rank Adaptation (LoRA) to efficiently adapt the model during the base session while freezing the core backbone to preserve previously learned representations, alongside a prototype-based classification head for incremental sessions to establish robust decision boundaries from limited samples. Extensive experiments across several datasets demonstrate that our approach consistently outperforms prior malware FSCIL baselines and achieves state-of-the-art performance.

## Metadata
- **Published**: 2026-08-24T17:41:15Z
- **Authors**: Kyle Stein, Guillermo Francia, III Eman El-Sheikh, Andrew Arash Mahyari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23536v1)