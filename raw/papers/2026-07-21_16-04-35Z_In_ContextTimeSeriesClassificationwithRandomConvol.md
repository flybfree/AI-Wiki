---
title: In-Context Time Series Classification with Random Convolutional Features
published: 2026-07-21T16:04:35Z
authors: Joscha Cüppers, Jilles Vreeken
url: http://arxiv.org/abs/2607.19234v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Time Series Classification with Random Convolutional Features

## Abstract
Time series classification is central to domains like medical signal analysis, industrial monitoring, and sensor-based activity recognition, where class information manifests as localized shapes, specific frequencies, temporal shifts, or complex cross-channel interactions. Random convolutional transforms efficiently map these sequences to fixed-dimensional tabular features but are traditionally paired with simple linear classifiers. We investigate whether a pretrained tabular foundation model can more effectively harness these rich representations.   We propose MASHT, a pipeline that marries MultiRocket and Hydra features with the power of in-context tabular foundation models. By leveraging a pretrained tabular foundation model, our approach completely bypasses task-specific model training, requiring only feature extraction and direct inference. Extensive experiments demonstrate that MASHT matches state-of-the-art time series classification baselines on univariate tasks, achieving a lower average rank than HIVE-COTE 2.0. On multivariate datasets, MASHT remains highly competitive with the strongest reference methods.

## Metadata
- **Published**: 2026-07-21T16:04:35Z
- **Authors**: Joscha Cüppers, Jilles Vreeken
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19234v1)