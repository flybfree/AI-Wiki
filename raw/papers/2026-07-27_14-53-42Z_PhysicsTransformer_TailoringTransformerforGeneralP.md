---
title: Physics Transformer: Tailoring Transformer for General PDE Prediction
published: 2026-07-27T14:53:42Z
authors: Guoze Sun, Rui Zhang, Jiankai Tang, Mengtao Yan, Runze Mao, Zhi X. Chen, Hao Sun
url: http://arxiv.org/abs/2607.24513v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physics Transformer: Tailoring Transformer for General PDE Prediction

## Abstract
Transformer architectures have attracted increasing attention for solving partial differential equations (PDEs), owing to their flexibility in handling irregular discretizations and their ability to capture long-range physical dependencies. However, unlike discrete language tokens or fixed-resolution image patches, observed physical fields are finite samples of underlying infinite-dimensional functions. Consequently, effectively applying Transformers to PDEs requires a tokenizer that respects the functional nature of physical fields and constructs physically expressive tokens from arbitrary discretizations.To this end, we propose \methodname{Physics Transformer}, a function-projection-based Transformer architecture for physical field prediction. Physics Transformer treats a physical field as a continuous function and partitions its discretization into locality-preserving spatial patches. Within each patch, it dynamically learns a set of adaptive local basis functions and projects the sampled field onto these bases to obtain compact physics tokens. The resulting tokens capture diverse latent physical states while preserving fine-scale spatial structures, enabling efficient global interaction through factorized attention across space and physical states. The projected representation further supports efficient decoding at arbitrary query locations. Extensive experiments on diverse benchmarks, ranging from two-dimensional PDE dynamics to industrial-scale three-dimensional CFD simulations, demonstrate that Physics Transformer accurately captures fine-grained physical structures and achieves state-of-the-art predictive performance. These results establish function projection as a practical and effective foundation for designing Transformer architectures for PDE solving.

## Metadata
- **Published**: 2026-07-27T14:53:42Z
- **Authors**: Guoze Sun, Rui Zhang, Jiankai Tang, Mengtao Yan, Runze Mao, Zhi X. Chen, Hao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24513v1)