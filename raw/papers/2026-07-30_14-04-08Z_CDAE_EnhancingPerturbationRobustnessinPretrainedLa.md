---
title: CDAE: Enhancing Perturbation Robustness in Pretrained Language Models with Contrastive Denoising
published: 2026-07-30T14:04:08Z
authors: Sina Heydari, Amirreza Abbasi, Mohsen Hooshmand, Majid Ramezani
url: http://arxiv.org/abs/2607.28236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CDAE: Enhancing Perturbation Robustness in Pretrained Language Models with Contrastive Denoising

## Abstract
Pre-trained language models have significantly improved sentence representation learning, yet their embedding remain sensitive to semantic preserving textual perturbations such as synonym substitution, masking and word dropout. This work proposes a lightweight Contrastive Denoising Autoencoder (CDAE) that refines pre-trained BERT embedding by jointly optimizing contrastive and reconstruction objective to learn perturbation-invariant representation. We evaluate the proposed framework using multiple perturbation strategies with varying strengths and compare it against the original BERT embeddings and SimCSE. Experimental results show that CDAE consistently preserves higher embedding similarity under perturbations, with the improvements becoming more pronounced as framework effectively enhances representation stability while preserving semantic information, highlighting perturbation-invariant learning as a promising direction for improving sentence embeddings. The source code is publicly available at: https://github.com/ComputationIASBS/CDAE

## Metadata
- **Published**: 2026-07-30T14:04:08Z
- **Authors**: Sina Heydari, Amirreza Abbasi, Mohsen Hooshmand, Majid Ramezani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28236v1)