---
title: Signature-Guided Capacity Occupancy for Dense Expert Merging
published: 2026-08-10T07:16:10Z
authors: Lingching Tung, Chi-Jui Kim, Beicheng Xu, Yuchen Wang, Bin Cui
url: http://arxiv.org/abs/2608.09201v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Signature-Guided Capacity Occupancy for Dense Expert Merging

## Abstract
Dense expert merging combines domain-specialized language models into one single checkpoint, typically by admitting task-vector support in weight space. However, this admission is governed by three decisions that existing methods answer only partially: where to open layer capacity from cross-expert conflict, who should occupy that capacity based on domain demand, and how to admit the resulting support without relying on costly recipe search. To tackle these issues, we propose SigMerge (Signature-Guided Capacity Occupancy), a structured capacity assignment framework for dense expert merging. Starting from a dense base merge, conflict signatures set each layer's capacity from cross-expert conflict, positive base-merge deficits set each domain's share of that capacity, and a sequential occupancy rule admits each expert delta up to the resulting layer-domain budget. Across 21 paired settings spanning seven dense base merges and three model pools, SigMerge improves every one (by 15.0% on average) and achieves the best average rank (1.67) among six merging methods, outperforming three categories of merging baselines.

## Metadata
- **Published**: 2026-08-10T07:16:10Z
- **Authors**: Lingching Tung, Chi-Jui Kim, Beicheng Xu, Yuchen Wang, Bin Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09201v1)