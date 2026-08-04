---
title: Linear Multi-Timescale Retention as a Memory-Efficient Vision-Language Bridge
published: 2026-08-03T02:43:25Z
authors: Ashfak Yeafi, Mehedi Hasan, Md Khairul Islam
url: http://arxiv.org/abs/2608.01614v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Linear Multi-Timescale Retention as a Memory-Efficient Vision-Language Bridge

## Abstract
Vision-Language Models (VLMs) face a critical computational bottleneck when processing high-resolution imagery due to the $O(N^2)$ memory complexity of Softmax Multi-Head Attention (MHA). While substituting MHA with independent Multi-Layer Perceptrons (MLPs) achieves $O(N)$ scaling, it strips the architecture of spatial sequence routing, severely degrading global scene understanding and object permanence. In this paper, we propose the Linear Multi-Timescale Retention (LIA-MTR) module, a memory-efficient cross-modal bridge. By integrating an ELU-based positive feature mapping with adaptive write-gating and log-linearly distributed recurrent decays, LIA-MTR mathematically compresses continuous visual sequences into bounded memory states. Theoretical analysis proves the architecture operates with strict $O(N)$ sequence-interaction complexity. Empirically, synthetic retrieval evaluations demonstrate that LIA-MTR flawlessly routes context across 16,000 tokens, eliminating the "Lost in the Middle" degradation typical of naive linear attention. Hardware benchmarking reveals infinite-context scaling capabilities, natively processing 262,144 visual patches within an 11.2 GB VRAM footprint, whereas standard MHA suffers out-of-memory failure at 16,384 patches. Furthermore, following instruction tuning on 665K conversational samples, LIA-MTR significantly outperforms an industry-standard MLP baseline on the MME benchmark (71.00% vs. 68.11%), driven by a 10% absolute improvement in object permanence and superior global semantic extraction. This work establishes a mathematically rigorous, computationally flat foundation for infinite-context Vision-Language integration.

## Metadata
- **Published**: 2026-08-03T02:43:25Z
- **Authors**: Ashfak Yeafi, Mehedi Hasan, Md Khairul Islam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01614v1)