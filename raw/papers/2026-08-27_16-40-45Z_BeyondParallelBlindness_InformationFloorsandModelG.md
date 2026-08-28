---
title: Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting
published: 2026-08-27T16:40:45Z
authors: Xinwei Qiang, Xiang Fang, Chang Chen, Yue Guan, Yufei Ding
url: http://arxiv.org/abs/2608.27339v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting

## Abstract
Block drafters propose several tokens in one forward pass, before earlier target tokens are realised. Their rejection mixes two losses: missing within-block path information and imperfect modelling of observable information. Accepted length cannot distinguish them. We separate the two with an information floor, the minimum expected rejection at a specified conditioning order; rejection above this floor is the model gap. Estimating both from target rollouts across four domains, four open-weight targets, and a frontier API target yields three findings. First, the all-parallel floor reaches $0.286$ at the final slot on Qwen3-4B, limiting even the best proposal to $71\%$ per-slot acceptance. Second, one realised token removes $86$--$100\%$ of this floor, a locality also recovered by an independent mutual-information analysis. Third, current drafters remain far above their floors: the final-slot model gap accounts for $43$--$64\%$ of DFlash rejection and $85$--$92\%$ of DSpark's oracle-conditioned rejection. These findings separate the value of short-range conditioning from proposal quality.

## Metadata
- **Published**: 2026-08-27T16:40:45Z
- **Authors**: Xinwei Qiang, Xiang Fang, Chang Chen, Yue Guan, Yufei Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27339v1)