---
title: TDDM-Melatt: A Decoupled Memory and Diffusion Framework for Generalizable Encrypted Traffic Classification
published: 2026-08-31T13:11:52Z
authors: Ze Chen, Qiming Yu, Zijia Song, Guozheng Yang, Wei Yan
url: http://arxiv.org/abs/2608.30745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TDDM-Melatt: A Decoupled Memory and Diffusion Framework for Generalizable Encrypted Traffic Classification

## Abstract
The widespread adoption of encrypted traffic poses severe challenges to current security situational awareness systems based on network traffic monitoring. In existing dataset-driven training and testing studies, limitations such as shortcut learning induced by spurious feature correlations and sample imbalance caused by the long-tail distribution of real-world traffic result in weak generalization of traffic identification performance to real-world network traffic. To address these limitations, we propose TDDM-Melatt, a disentangled memory-based traffic classification framework with diffusion-based data augmentation. First, we design Melatt, a memory-decoupled traffic representation model, which employs Competitive Gating Long Short-Term Memory (CG-LSTM) to construct the encoder and decoder. We design a spurious-correlation-free pre-training and inference paradigm, employing strict topology anonymization and a frozen pre-trained encoder strategy to cut off the model's learning pathways for spurious features. During inference, classification is performed efficiently by a downstream classifier on the frozen representations. Second, we propose a Traffic Denoising Diffusion Model (TDDM) tailored to the characteristics of traffic data. Extensive experiments are conducted on 4 representative public benchmark datasets. Under strict flow-level splitting and anonymization, TDDM-Melatt outperforms 6 basic classification models and 6 SOTA representation learning models. The proposed method provides a new and effective technical pathway for encrypted traffic classification in real-world network environments.

## Metadata
- **Published**: 2026-08-31T13:11:52Z
- **Authors**: Ze Chen, Qiming Yu, Zijia Song, Guozheng Yang, Wei Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30745v1)