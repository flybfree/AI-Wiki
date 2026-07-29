---
title: Beyond Single-Episode Optimization: Sliding-Window Aware Generative Auto-Bidding for Long-Term Advertising Effectiveness
published: 2026-07-28T03:21:13Z
authors: Binglin Wu, Chuan Yue, Yingyi Zhang, Xianneng Li, Ruyue Deng, Weiru Zhang, Xiaoyi Zeng
url: http://arxiv.org/abs/2607.25233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Single-Episode Optimization: Sliding-Window Aware Generative Auto-Bidding for Long-Term Advertising Effectiveness

## Abstract
Auto-bidding systems optimize bids to maximize value under efficiency constraints such as Cost-Per-Action (CPA). Existing methods treat each day as an independent episode. However, many advertisers produce value so sparsely that per-day efficiency ratios become statistically unreliable, undermining advertiser retention. Platforms therefore evaluate window-level efficiency over sliding windows of $W{=}7$ days, ensuring fair evaluation and long-term advertising effectiveness. This creates cross-episode coupling: each day's bidding decisions affect up to $W$ overlapping windows, so setting daily targets requires anticipating future market conditions. We propose SWAG-Bid (Sliding-Window Aware Generative Auto-Bidding), a hierarchical framework decomposing this challenge into episode-level planning and step-level execution. The planner uses a Masked Trajectory Model to forecast markets and generate candidate plans, scored across all overlapping windows by Multi-Window Model Predictive Control Sampling (MWMS) with exponential confidence decay. The controller adjusts reliance on this guidance through a state-adaptive gate, Per-Step Gated Adaptive Layer Normalization (PSG-AdaLN), complemented by Return-to-Go and Cost-to-Go channels carrying budget and constraint information. Experiments on AuctionNet-Sparse and online A/B tests on AliExpress show that SWAG-Bid achieves competitive constraint satisfaction and value acquisition under sliding-window evaluation.

## Metadata
- **Published**: 2026-07-28T03:21:13Z
- **Authors**: Binglin Wu, Chuan Yue, Yingyi Zhang, Xianneng Li, Ruyue Deng, Weiru Zhang, Xiaoyi Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25233v1)