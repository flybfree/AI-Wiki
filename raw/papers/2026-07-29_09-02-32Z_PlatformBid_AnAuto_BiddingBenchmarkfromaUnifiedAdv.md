---
title: PlatformBid: An Auto-Bidding Benchmark from a Unified Advertising Platform's Perspective
published: 2026-07-29T09:02:32Z
authors: Shengtian Yang, Yewen Li, Peng Jiang, Zhiyi Lyu, Bo An, Peng Jiang, Qingpeng Cai, Lei Feng
url: http://arxiv.org/abs/2607.27265v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PlatformBid: An Auto-Bidding Benchmark from a Unified Advertising Platform's Perspective

## Abstract
Real-time bidding is central to computational advertising, comprising three elements: Supply Side Platform (SSP) selling ad impressions, Demand Side Platform (DSP) bidding for advertisers, and Ad Exchange conducting auctions between them. Traditional auto-bidding algorithms focus solely on the DSP side, maximizing advertiser conversions by adjusting bids against competitors. However, current big ad platforms, such as social media and e-commerce companies, now integrate SSP, DSP, and Ad Exchange functions internally. From such ad platforms' perspective, the goal of the auto-bidding algorithms is not only to maximize the advertisers' conversions, but also the total revenue of the platform. Given the lack of platform-centric evaluation frameworks and the pressing need to advance auto-bidding research, we propose PlatformBid - the first comprehensive benchmark designed from a unified ad platform's perspective. To accurately reflect the real-world auto-bidding scenarios, we define three representative settings: (1) homogeneous competition with identical algorithms across advertisers, (2) heterogeneous competition with diverse algorithmic strategies, and (3) promotional competition where some advertisers surge budgets for boosting sales during promotional events like Black Friday. We systematically evaluate a broad spectrum of existing auto-bidding methods across these settings, encompassing classical control methods, RL-based methods, and recent generative methods. Besides these methods, we further propose a novel auto-bidding method based on flow-matching, termed BidFlow, which leverages the flow-matching method's expressive policy representation to effectively handle dynamic competitive environments. Online experiments on Kuaishou further show a +0.68\% improvement in target cost, providing deployment evidence for the offline-online consistency of PlatformBid.

## Metadata
- **Published**: 2026-07-29T09:02:32Z
- **Authors**: Shengtian Yang, Yewen Li, Peng Jiang, Zhiyi Lyu, Bo An, Peng Jiang, Qingpeng Cai, Lei Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27265v1)