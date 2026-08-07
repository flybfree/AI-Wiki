---
title: Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling
published: 2026-08-05T23:17:08Z
authors: Sanjith Senthil, Rishidev Chaudhuri
url: http://arxiv.org/abs/2608.05464v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Effective pruning of task-trained recurrent neural networks using noisy fluctuations and connection rescaling

## Abstract
The pruning of network connections is key to brain function but, despite its importance, there exist few biologically-plausible pruning rules with demonstrated good performance. In this work we evaluate noise-prune, a recently introduced unsupervised local pruning rule for recurrent networks that uses noisy fluctuations to determine the importance of connections. Noise-prune has previously only been empirically tested on random networks without a specific computational function. We show that noise-prune preserves task-performance in task-trained recurrent neural networks, greatly outperforming a strategy that only uses the magnitude of connections and performing on par with or exceeding a non-local strategy that uses second-order information. Rather than deterministically removing connections that fall below a certain threshold importance, noise-prune samples connections to preserve based on their importance and strengthens retained connections to preserve average synaptic strength. We show that this sampling and rescaling is essential to good performance, but that the optimal empirical degree of rescaling is lower than that predicted by the original theoretical argument. Our work thus validates noise-prune as a biologically-plausible pruning rule for functional recurrent network architectures and characterizes its optimal parameter settings.

## Metadata
- **Published**: 2026-08-05T23:17:08Z
- **Authors**: Sanjith Senthil, Rishidev Chaudhuri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05464v1)