---
title: MoNo: Multiscale Optimal Transport Neural Operator for Solving PDEs on General Geometries
published: 2026-08-10T15:55:11Z
authors: Zijiang Yang, Xiaomeng Wu, Dongmei Fu
url: http://arxiv.org/abs/2608.09764v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoNo: Multiscale Optimal Transport Neural Operator for Solving PDEs on General Geometries

## Abstract
Transformer-based neural operators have achieved substantial progress in solving Partial Differential Equations (PDEs) by projecting spatial observations into compact latent tokens and learning physical interactions in latent spaces. However, we reveal that existing learnable projection mechanisms cannot ensure stable and balanced assignments from observation points to latent tokens, causing some latent tokens to be over-assigned while others remain underutilized. This limitation further restricts the design of hierarchical architectures, as assignment imbalance is continuously inherited and amplified across latent spaces, eventually causing severe token collapse in deeper spaces. To address these issues, we propose MoNo (Multiscale Optimal Transport Neural Operator), a progressive multiscale neural operator that efficiently solves PDEs on general geometries through stable latent-space construction. At its core is CoTAP (Cross-scale Optimal Transport Assignment and Projection), a novel latent-space construction method that formulates cross-space assignment between adjacent spaces as an entropy-regularized optimal transport problem, thereby constructing balanced bidirectional projections and stable latent spaces. CoTAP also ensures stable information transfer across multiple latent spaces, further enabling multiscale architectures on general geometries, which in turn support more efficient learning of long-range physical interactions. Extensive experiments demonstrate that MoNo outperforms existing state-of-the-art neural operators in both prediction performance and computational efficiency. Code is available at https://github.com/ZijiangY1116/MoNo.

## Metadata
- **Published**: 2026-08-10T15:55:11Z
- **Authors**: Zijiang Yang, Xiaomeng Wu, Dongmei Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09764v1)