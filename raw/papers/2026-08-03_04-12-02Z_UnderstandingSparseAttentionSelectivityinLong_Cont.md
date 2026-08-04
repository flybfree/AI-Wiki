---
title: Understanding Sparse Attention Selectivity in Long-Context Foundation Models via Counterfactual Evaluation
published: 2026-08-03T04:12:02Z
authors: Xingyu Ren, Youran Sun, Chugang Yi, Haizhao Yang
url: http://arxiv.org/abs/2608.01676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Sparse Attention Selectivity in Long-Context Foundation Models via Counterfactual Evaluation

## Abstract
Sparse attention is widely deployed in long-context serving stacks, yet no framework audits how discarding blocks changes the influence of specific content on model output. We first establish that the phenomenon is real and causal: Block Sparse Flash Attention (BSFA) route replay across four architectures changes output decisions in 13 of 16 cells, with zero identity-replay label flips. We then introduce a dense-calibrated counterfactual audit using matched probe cards---Gold (carrying the correct answer label), Poison (carrying a target wrong label), and Benign (filler only)---under six-layout position symmetry, isolating the sparsification-specific effect.   Two patterns compete. Signal concentration: the selector preserves Gold and Poison blocks far above filler-matched Benign blocks (G$\approx$P$\gg$B across all model--task pairs). Integration loss: discarding blocks severs cross-block attention---confirmed by an ablation where isolating the probe block collapses its influence from 4.48 logits to zero. Compression ratio governs the balance: a full sweep from mild ($c=0.25$) to aggressive ($c=0.75$) compression across four model--task pairs reveals that three of four cells move toward stronger sparse amplification at higher compression, with two exhibiting sign reversals.   Three independent arms---BSFA route replay, controlled block-top-$k$, and KV-cache eviction---converge: sparsification changes content influence in ways aggregate accuracy cannot detect. We provide an open measurement framework deployable on any model exposing block identities.

## Metadata
- **Published**: 2026-08-03T04:12:02Z
- **Authors**: Xingyu Ren, Youran Sun, Chugang Yi, Haizhao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01676v1)