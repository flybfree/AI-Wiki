---
title: Dual-Primal Graph VAEs for Noisy Label Aggregation
published: 2026-08-11T22:24:16Z
authors: Patrick Stinson, Nikolaus Kriegeskorte
url: http://arxiv.org/abs/2608.11473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual-Primal Graph VAEs for Noisy Label Aggregation

## Abstract
Inferring the ground-truth from noisy crowdsourced labels is an important theoretical and practical problem. Neural network-based methods offer an alternative to classical Bayesian models which require specifying a family of generative models used for inference. However, current models either still rely on fairly simple generative models for inference or require pseudo-labels or synthetic data to train the aggregate classifier. We propose a graph VAE architecture in which the decoder and encoder use GAT-based message passing on the adjacency graph of a crowdsourced dataset and its dual, respectively. The ground-truth labels are treated as latent variables, enabling unsupervised representation learning without needing to train a separate classifier. We show our model achieves state of the art performance on crowdsourcing benchmarks. We then demonstrate the generality of our approach by showing how the original crowdsourcing graph can be augmented to incorporate side information such as representations from neural network classifiers trained on the noisy labels to substantially boost their classification performance at test time.

## Metadata
- **Published**: 2026-08-11T22:24:16Z
- **Authors**: Patrick Stinson, Nikolaus Kriegeskorte
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11473v1)