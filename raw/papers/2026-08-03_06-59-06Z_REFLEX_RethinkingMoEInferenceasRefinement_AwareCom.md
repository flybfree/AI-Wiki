---
title: REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models
published: 2026-08-03T06:59:06Z
authors: Xiang Xia, Cheng Yan, Yiming Zhang, Jiazheng Liu, Hongyu Zhang, Wuyang Zhang
url: http://arxiv.org/abs/2608.01784v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models

## Abstract
Mixture-of-experts (MoE) models increase parameter capacity by activating only a small subset of experts for each token. This conditional-computation paradigm has enabled autoregressive language models to scale model capacity without a proportional increase in per-token computation. In diffusion language models (DLMs), however, each denoising forward jointly revisits all token positions despite their sharply different refinement demands, while the default fixed token-choice routing assigns them a uniform expert budget, creating a mismatch between expert computation and refinement demand. We argue that MoE inference in DLMs should therefore be viewed as refinement-aware compute allocation across heterogeneous token refinement states. We propose REFLEX (\textbf{RE}finement-aware \textbf{FLEX}ible expert allocation), a training-free method that keeps the default router unchanged while reorganizing expert computation around the evolving refinement process. Specifically, REFLEX introduces a coarse-to-fine hierarchy for expert-budget allocation that aligns computation with block-relative refinement roles while using the Frontier-Progress Score to resolve active-block priorities. Across multiple widely used benchmarks on two representative MoE-based DLMs, LLaDA-MoE and LLaDA2.0-mini, REFLEX reduces allocated expert computation by 15\% on average while preserving or even improving generation quality on most benchmarks relative to default routing. Compared with autoregressive-style variable-expert routing methods, REFLEX also yields a more consistent quality--computation trade-off, further supporting the importance of allocating expert computation according to the heterogeneous refinement demands exposed within each denoising forward.

## Metadata
- **Published**: 2026-08-03T06:59:06Z
- **Authors**: Xiang Xia, Cheng Yan, Yiming Zhang, Jiazheng Liu, Hongyu Zhang, Wuyang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01784v1)