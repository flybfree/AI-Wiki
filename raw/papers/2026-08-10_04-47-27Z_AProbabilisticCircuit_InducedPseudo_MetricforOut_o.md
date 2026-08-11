---
title: A Probabilistic Circuit-Induced Pseudo-Metric for Out-of-Distribution Detection
published: 2026-08-10T04:47:27Z
authors: Bhumika K, Vidhya S, Narayanan C Krishnan
url: http://arxiv.org/abs/2608.09117v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Probabilistic Circuit-Induced Pseudo-Metric for Out-of-Distribution Detection

## Abstract
Probabilistic Circuits (PCs) are tractable generative models whose internal nodes encode a hierarchy of probabilistic sum- maries over different variable scopes. Existing PC-based out- of-distribution (OOD) detection methods ignore this hierar- chy, reducing the entire circuit to the scalar likelihood (or its uncertainty) computed at the root. We introduce Hierar- chical Likelihood Vector (HLV), a representation whose en- tries are the likelihoods associated with selected PC nodes and define the Hierarchical Likelihood Distance (HLD), a PC-induced pseudo-metric that compares the probability dis- tributions through the expectations of their HLVs. We show that HLD is an integral probability metric over a function class naturally induced by the PC and develop a principled goodness-of-fit hypothesis test for unsupervised OOD detec- tion. Unlike existing approaches, the trained PC alone serves as the representation of the in-distribution: no held-out in- distribution data are required at deployment. We further show that the quantities required by the hypothesis test can be com- puted exactly, directly from the trained circuit, yielding an ap- proximate analytic decision threshold. Experiments on tabular and MNIST datasets demonstrate that exploiting the hierarchi- cal probabilistic summaries encoded through the PC improve OOD detection over root-likelihood, uncertainty-, typicality- and kernel-based baselines, while naturally localizing distri- bution shifts to the PC nodes responsible for the shift.

## Metadata
- **Published**: 2026-08-10T04:47:27Z
- **Authors**: Bhumika K, Vidhya S, Narayanan C Krishnan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09117v1)