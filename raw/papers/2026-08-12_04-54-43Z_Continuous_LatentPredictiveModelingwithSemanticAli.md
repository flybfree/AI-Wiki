---
title: Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models
published: 2026-08-12T04:54:43Z
authors: Myeong-Ju Cho, Hye-Bin Shin, Seo-Hyun Lee, Seong-Whan Lee
url: http://arxiv.org/abs/2608.11656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models

## Abstract
Recent advances in EEG foundation models have demonstrated the potential of large-scale pretraining to enable generalizable neural decoding across subjects, recording environments, and datasets. However, dominant pretraining paradigms face key challenges: masked autoencoding tends to prioritize low-level signal reconstruction over task-relevant semantics, while autoregressive modeling creates a mismatch between continuous neural dynamics and discrete token spaces. To address these challenges, new strategies are needed to effectively align continuous EEG representations with natural-language semantics and enable their integration with large language models. Accordingly, we propose Brain Latent Predictive Model (BLPM), an EEG-language foundation model that reformulates heterogeneous EEG decoding tasks as a continuous semantic embedding prediction problem. BLPM introduces a Continuous EEG Latent Predictive (CELP) encoder that learns transferable representations through latent target prediction. Building on these representations, a Multi-Query Semantic Decomposition (MQSD) module extracts task-relevant information and aligns continuous EEG representations with textual semantics within a shared latent space according to their semantic relationships. Experiments across multiple benchmarks demonstrate consistent generalization performance across diverse tasks, establishing continuous latent semantic prediction as an effective paradigm for EEG-language foundation models.

## Metadata
- **Published**: 2026-08-12T04:54:43Z
- **Authors**: Myeong-Ju Cho, Hye-Bin Shin, Seo-Hyun Lee, Seong-Whan Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11656v1)