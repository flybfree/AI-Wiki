---
title: Less Traffic, Better Outcomes: Competition-Aware Request Dispatch in Real-Time Ad Exchanges
published: 2026-08-04T14:11:42Z
authors: Jonaid Shianifar, Blaz Mramor, Fangda Zou, Matthieu C. Martin, Xingsheng Guo, Zhihua Zhu, Rong Zhou, Bichen Shi
url: http://arxiv.org/abs/2608.03705v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Less Traffic, Better Outcomes: Competition-Aware Request Dispatch in Real-Time Ad Exchanges

## Abstract
Real-time bidding (RTB) ad exchanges typically forward nearly all incoming requests to demand-side platforms (DSPs), even though only a small fraction receive bids. This over-distribution weakens auction outcomes: DSPs throttle participation under compute and budget constraints, reducing the effective use of limited bidding capacity. We present a competition-aware request dispatch framework that uses distributional bid prediction and probabilistic forwarding to decide whether each request should be sent to each DSP. The system adapts per-DSP thresholds over time through lightweight policy optimization to track non-stationary market conditions. We evaluate the framework through four sequential online experiments on a production platform serving over 20 billion daily requests. A full multi-DSP deployment reduces DSP request volume under the policy by 34.2% while increasing net revenue by 4.6% (p<0.001) in a recent 14-day window after an initial DSP adaptation period. Further analysis highlights strong heterogeneity across traffic segments and reveals that aggregate metrics can be misleading. Segment-level and per-DSP analyses suggest that the policy surfaces comparative advantages among DSPs, improving monetized outcomes without increasing overall request volume.

## Metadata
- **Published**: 2026-08-04T14:11:42Z
- **Authors**: Jonaid Shianifar, Blaz Mramor, Fangda Zou, Matthieu C. Martin, Xingsheng Guo, Zhihua Zhu, Rong Zhou, Bichen Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03705v1)