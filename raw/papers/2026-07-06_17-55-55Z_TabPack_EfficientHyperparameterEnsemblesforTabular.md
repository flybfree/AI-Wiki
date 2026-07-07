---
title: "TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning"
published: "2026-07-06T17:55:55Z"
authors: Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev, Artem Babenko
url: http://arxiv.org/abs/2607.05380v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TabPack: Efficient Hyperparameter Ensembles for Tabular Deep Learning

## Abstract
In deep learning for tabular data, efficient ensembles of multilayer perceptrons (MLPs) have recently emerged as effective and practical architectures. Existing methods of this kind use the same hyperparameters for all underlying MLPs, which requires hyperparameter tuning for achieving the best performance. In this work, we introduce TabPack, an efficient MLP ensemble with strong out-of-the-box performance and reduced reliance on traditional tuning. In a single run, TabPack samples and trains many MLPs with different hyperparameters efficiently in parallel and selects ensemble members on the fly during training. Thus, TabPack only requires specifying ranges from which to sample MLP hyperparameter rather than exact hyperparameter values, which naturally demands less precision for good performance. In experiments on medium-to-large public datasets, TabPack with default settings performs on par with extensively tuned prior methods, thus substantially reducing effort and compute resources needed to achieve competitive results on tabular tasks. Notably, running the default TabPack configuration on a modern MacBook took less time than tuning some baselines on an industry-grade GPU.

## Metadata
- **Published**: 2026-07-06T17:55:55Z
- **Authors**: Yury Gorishniy, Akim Kotelnikov, Ivan Rubachev, Artem Babenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.05380v1)