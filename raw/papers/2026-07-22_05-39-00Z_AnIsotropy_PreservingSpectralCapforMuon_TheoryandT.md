---
title: An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies
published: 2026-07-22T05:39:00Z
authors: Jiachun Li
url: http://arxiv.org/abs/2607.19771v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies

## Abstract
Muon and related matrix-sign optimizers are increasingly used to pre-train large language models, but their effect on the internal geometry of individual weight matrices is not well understood. This preliminary report proposes a unified framework built on a single idealizing assumption -- exact scale invariance of the loss under weight rescaling, which holds approximately in normalization-heavy networks. Under this assumption, plain SGD carries a built-in 1/||W|| brake on its update size, whereas Muon's matrix-sign step removes that brake, so both the Frobenius and spectral norms drift outward faster (t^{1/2} versus t^{1/4}). We further observe that the spectral-norm perturbation has a non-negative second-order term. This implies that a lightweight "spectral cap" -- which projects out only the first-order growth of the single top singular direction from each update -- can control the output covariance W K_X W^T without freezing training: the weight keeps learning through non-top directions, top-direction rotation, and top switching. We relate this cap to the min-entropy (H-infinity) of the singular-value spectrum. We then study three systems trained with Muon: a nanoGPT feed-forward projection, a 64-expert mixture-of-experts router, and the query/key projections of a bf16 FlashAttention block. In each case the cap increases isotropy and, at the margins -- a router collapsing to a single expert, and the near-divergence of one attention head -- prevents a concrete failure, while leaving validation loss essentially unchanged. We emphasize that the scale-invariance assumption is strong and that these small-scale results are preliminary; comments are welcome.

## Metadata
- **Published**: 2026-07-22T05:39:00Z
- **Authors**: Jiachun Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19771v1)