---
title: KALE: Kernel Alignment with Loss Equilibration for Stable CLIP-DINOv2 Alignment at Web Scale
published: 2026-07-21T09:14:33Z
authors: Michał Pawłowicz
url: http://arxiv.org/abs/2607.18885v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KALE: Kernel Alignment with Loss Equilibration for Stable CLIP-DINOv2 Alignment at Web Scale

## Abstract
Kernel-based alignment of CLIP toward a vision centric teacher such as DINOv2 (KUEA) improves CLIP's visual representations while preserving text-encoder compatibility, using a fixed trade-off weight tuned on curated ImageNet-1K. We ask whether this transfers to noisy, web-scale data (CC12M) and find that it does not: the alignment term's weighted contribution falls to about 0.2% of the clean term, so under any fixed weight its gradient is effectively inert. We introduce KALE, a loss-equilibration controller that tracks both losses and adaptively rescales the alignment weight toward a target ratio, restoring the signal with no per-dataset tuning; reaching balance requires increasing the weight by roughly four orders of magnitude, and the required value is configuration-dependent, so no fixed scalar suffices. We characterize the resulting regime: a bounded high learning rate and a decaying schedule with a moderate floor are needed for stability, and the controller equilibrates rather than diverging. On a 3.3M-image CC12M subset, the aligned model preserves image-text retrieval and reproducibly improves SVHN linear probing; zero-shot improves by +2.00 over CLIP on the standard 11-dataset average, exceeding KUEA's +1.29. We report all results with explicit run-to-run variance and base our conclusions on the metrics that are stable across runs.

## Metadata
- **Published**: 2026-07-21T09:14:33Z
- **Authors**: Michał Pawłowicz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18885v1)