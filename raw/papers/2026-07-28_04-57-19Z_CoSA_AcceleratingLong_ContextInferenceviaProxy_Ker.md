---
title: CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention
published: 2026-07-28T04:57:19Z
authors: Yufei Xue, Lin Niu, Hong Liu, Siran Liu, Hanyong Shao, Wei Liu, Guanghua Yu, Jianchen Zhu, Jun Zhang
url: http://arxiv.org/abs/2607.25291v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention

## Abstract
The quadratic cost of self-attention makes long-context inference prohibitively expensive, and proxy-based block-sparse attention has become a practical remedy. Existing methods typically rely on a proxy to predict a binary sparse mask and a kernel to consume this mask and perform sparse attention computation. Such an approach is effective under moderate budgets. However, as the budget tightens, the estimated proxy inevitably drops some salient blocks, while the kernel can only apply the sparse mask mechanically, leading to an evident drop in model accuracy. We propose CoSA, a two-stage training-free Sparse Attention under proxy-kernel CO-design, which couples a Kernel-Aware Proxy (KAP) with an Ordered-Skipping Kernel (OSK). In the first stage, the KAP selects blocks under a moderate budget and produces an ordered mask that prescribes the order in which KV pages are visited in the kernel inner loop. In the second stage, the OSK applies this mask and skips more blocks under a tightened budget given online-softmax statistics. Across mainstream LLM backbones and long-context benchmarks, CoSA attains higher accuracy at lower budgets. Impressively, CoSA achieves a 4.93$\times$ attention speedup and reduces end-to-end Time-to-First-Token by 2.53$\times$ under a context length of 128K with negligible performance degradation.

## Metadata
- **Published**: 2026-07-28T04:57:19Z
- **Authors**: Yufei Xue, Lin Niu, Hong Liu, Siran Liu, Hanyong Shao, Wei Liu, Guanghua Yu, Jianchen Zhu, Jun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25291v1)