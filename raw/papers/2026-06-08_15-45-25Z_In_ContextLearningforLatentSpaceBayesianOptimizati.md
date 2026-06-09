---
title: In-Context Learning for Latent Space Bayesian Optimization
published: 2026-06-08T15:45:25Z
authors: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
url: http://arxiv.org/abs/2606.09664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Learning for Latent Space Bayesian Optimization

## Abstract
Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.

## Metadata
- **Published**: 2026-06-08T15:45:25Z
- **Authors**: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.09664v1)