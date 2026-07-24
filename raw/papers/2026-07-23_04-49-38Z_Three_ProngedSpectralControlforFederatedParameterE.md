---
title: Three-Pronged Spectral Control for Federated Parameter Efficient Fine Tuning
published: 2026-07-23T04:49:38Z
authors: Shiva Raj Pokhrel, Dipsan Bhattarai, Anwar Walid
url: http://arxiv.org/abs/2607.20914v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Three-Pronged Spectral Control for Federated Parameter Efficient Fine Tuning

## Abstract
Federated parameter-efficient fine-tuning (PEFT) enables communication-efficient adaptation of large pretrained models on decentralized edge data, but it remains fragile under non-IID client heterogeneity. In low-rank adaptation (LoRA), different clients may learn locally useful but spectrally misaligned update subspaces, causing high-variance aggregation and poor global transfer. We propose TRISHUL, a spectral-control framework for robust federated PEFT. TRISHUL follows the FL no-raw-data-sharing setting but does not itself provide formal privacy guarantees. TRISHUL uses shared frozen multi-head low-rank bases to obtain algebraically exact aggregation of compact core updates, applies nuclear norm proximal shrinkage to suppress client-specific high-rank spectral components before upload, and allocates adaptation heads non-uniformly across layers using a concave water filling budget rule derived from pretrained layer capacity. Because shrinkage is performed only on small core matrices, TRISHUL adds negligible computation and no extra per-round communication over the underlying multi-head PEFT protocol. Across vision and language benchmarks, including CIFAR-100, SVHN, 20 Newsgroups, MRQA, and GLUE with LLaMA3.2-1B, TRISHUL improves convergence, stability, and final performance over federated LoRA baselines, with greater gains under stronger heterogeneity.

## Metadata
- **Published**: 2026-07-23T04:49:38Z
- **Authors**: Shiva Raj Pokhrel, Dipsan Bhattarai, Anwar Walid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20914v1)