---
title: The Fairness Collapse Phenomenon: Bias Amplification in Language Models Trained on Synthetic Data
published: 2026-08-04T22:56:39Z
authors: Irina Proskurina, Antoine Gourru, Julien Velcin
url: http://arxiv.org/abs/2608.04268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Fairness Collapse Phenomenon: Bias Amplification in Language Models Trained on Synthetic Data

## Abstract
Generative models trained on artificially generated data have been shown to exhibit model collapse, resulting in significant performance degradation. As synthetic content increasingly contaminates the training corpora of language models, this raises critical concerns about the use of open data in continued pretraining. Although previous work has demonstrated model collapse in language models, it remains unclear whether exposure to synthetic data amplifies or attenuates the social biases already present in pretrained models. Because language models are known to reproduce and amplify demographic stereotypes, recursive training on self-generated data may create a self-reinforcing feedback loop in which biased associations become progressively stronger across generations. We call this hypothesized phenomenon fairness collapse. In this work, we construct controlled training regimes in which models are repeatedly trained on synthetic data using the Bias in Bios dataset. Across experiments, we observe a consistent and concerning pattern: fairness degradation emerges before substantial degradation is reflected by standard language-modeling metrics. This result highlights a critical risk associated with synthetic data contamination in language model training: bias can increase silently before strong indicators of model collapse become apparent.

## Metadata
- **Published**: 2026-08-04T22:56:39Z
- **Authors**: Irina Proskurina, Antoine Gourru, Julien Velcin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04268v1)