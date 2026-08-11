---
title: Targeted Label-Flipping and Oversampling Attacks on Federated Conditional GANs
published: 2026-08-10T08:56:50Z
authors: Panav Shah, Avishek Ghosh
url: http://arxiv.org/abs/2608.09314v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Targeted Label-Flipping and Oversampling Attacks on Federated Conditional GANs

## Abstract
In a federated learning setup for GANs, several adversarial attacks are possible. One such attack is label flipping, in which malicious clients deliberately alter label information during local training in order to manipulate the global generator. The objective of this attack is to skew the learned generation distribution so that samples conditioned on a target label are instead mapped to a source class. In this work, we investigate the effectiveness of label flipping attacks in federated GANs through both theoretical analysis and empirical evaluation. We further consider an oversampling based variant, in which malicious clients upweight poisoned samples during local training to amplify their influence on the aggregated global model. We quantify the resulting distributional shift by computing the Kullback Leibler divergence between the clean and poisoned class conditional distributions, and show both analytically and on FEMNIST, MNIST, and CIFAR10 that the semantic damage of the attack grows linearly in the effective poisoning strength while deviation from the true target distribution grows only quadratically, making the attack effective yet difficult to detect from label agnostic metrics.

## Metadata
- **Published**: 2026-08-10T08:56:50Z
- **Authors**: Panav Shah, Avishek Ghosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09314v1)