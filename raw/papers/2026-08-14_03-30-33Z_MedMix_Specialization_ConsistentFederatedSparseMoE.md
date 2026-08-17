---
title: MedMix: Specialization-Consistent Federated Sparse MoEs under Modality Heterogeneity
published: 2026-08-14T03:30:33Z
authors: Adiba Orzikulova, Dong Min Kim, Jaehong Yoon, Sung-Ju Lee
url: http://arxiv.org/abs/2608.13911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedMix: Specialization-Consistent Federated Sparse MoEs under Modality Heterogeneity

## Abstract
Federated multimodal medical AI faces modality heterogeneity at both the client and sample levels: clients may systematically lack access to specific modality types, while individual records within the same client may contain different partial modality subsets. Sparse Mixture-of-Experts (MoE) architectures are a promising remedy for modality-adaptive computation, but their use in federated learning is fragile under cross-client modality heterogeneity, where locally learned routing policies can diverge across clients and drive experts toward incompatible specializations. Different clients may assign the same observed modality configuration to different experts, or train similarly indexed experts on different missing-modality configurations, causing standard aggregation to misalign or overwrite the expert specialization that sparse MoEs are intended to learn. To address this challenge, we propose MedMix, a semantic-alignment framework for federated multimodal sparse MoEs that coordinates cross-client routing and expert specialization using modality context. At the client side, MedMix uses modality-context-aware routing to guide expert selection using each token's modality identity, position, and incompleteness context. Across clients, it uses consensus-guided routing alignment to construct server-side consensus anchors for shared modality patterns and align local routing distributions across clients. Complementing these routing mechanisms, client-adaptive expert aggregation leverages client-specific modality-pattern prototypes to match and aggregate functionally similar experts across clients. Experiments on real-world multimodal medical datasets show that MedMix achieves the best average F1 across diverse modality heterogeneity and modality incompleteness settings, with especially clear gains under severe heterogeneity.

## Metadata
- **Published**: 2026-08-14T03:30:33Z
- **Authors**: Adiba Orzikulova, Dong Min Kim, Jaehong Yoon, Sung-Ju Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13911v1)