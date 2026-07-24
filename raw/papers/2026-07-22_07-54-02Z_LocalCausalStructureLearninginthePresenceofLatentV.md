---
title: Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias
published: 2026-07-22T07:54:02Z
authors: Zheng Li, Hao Zhang, Ruxin Wang, Ruichu Cai, Kun Zhang, Feng Xie
url: http://arxiv.org/abs/2607.19866v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias

## Abstract
Discovering the direct causes and effects of a target variable from observational data is a fundamental problem in causal discovery, with broad applications in domains such as gene regulatory analysis and biomedical research. Existing causal discovery methods either learn a global causal structure, which incurs substantial computational cost, or assume the absence of latent variables and selection bias, assumptions that are often violated in real-world settings. Motivated by these challenges, we study local causal structure learning in the presence of latent variables and selection bias. Specifically, we first characterize a local region that enables target-specific causal discovery without recovering the entire global structure. We then establish a theoretical bridge between causal information learned from the observed distribution induced on this local region and the corresponding information in the global causal structure. Building on these foundations, we propose LoCaLS, a local causal structure learning algorithm that is sound and complete under standard assumptions and identifies the same direct causes and effects of a target variable as those identifiable by global causal discovery methods, while allowing for latent variables and selection bias. Extensive experiments on random and real-world structures demonstrate that the proposed method consistently achieves higher structural accuracy than existing local methods while requiring substantially less computational effort than state-of-the-art global methods. Furthermore, applications to two real-world gene expression datasets reveal biologically plausible target-specific causal structures, demonstrating its practical applicability in large-scale biological data analysis.

## Metadata
- **Published**: 2026-07-22T07:54:02Z
- **Authors**: Zheng Li, Hao Zhang, Ruxin Wang, Ruichu Cai, Kun Zhang, Feng Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19866v1)