---
title: DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
published: 2026-08-13T17:43:44Z
authors: Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
url: http://arxiv.org/abs/2608.13524v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees

## Abstract
Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel. Diffusion-based drafters further reduce proposal latency by predicting an entire token block in parallel, but their position-wise distributions are marginal rather than conditioned on tokens selected along each draft path. Existing recurrent correction incorporates causal information along a single draft chain, whereas diffusion-based tree construction broadens candidate coverage without carrying this correction along individual branches. We introduce DARTree, a training-free speculative decoding method that extends a pretrained AR correction head from chains to trees. DARTree first constructs a fixed-width candidate tree by expanding and scoring all nodes at each depth in a single batch, and then only applies best-first pruning to select the verification tree, decoupling AR-head inference from sequential heap operations. Across seven math, code, and chat benchmarks, DARTree achieves the highest average acceptance length and speedup in all four model--temperature configurations, accepting up to 12.97 tokens per verification round, 98.6\% more than DFlash and 27.9\% more than Domino in the same setting, and reaching up to 9.73$\times$ lossless speedup over locally measured autoregressive decoding.

## Metadata
- **Published**: 2026-08-13T17:43:44Z
- **Authors**: Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13524v1)