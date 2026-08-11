---
title: Loss-Resilient Wireless Video Token Communication over Block Fading Channels
published: 2026-08-09T13:23:45Z
authors: Bingyan Xie, Yongjeong Oh, Zihan Chen, Jihong Park, Yongpeng Wu, Wenjun Zhang
url: http://arxiv.org/abs/2608.08698v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loss-Resilient Wireless Video Token Communication over Block Fading Channels

## Abstract
Video token communication represents video content as discrete tokens that differ in their importance to reconstruction and exhibit temporal dependencies. When these tokens are packetized for wireless transmission, block fading can cause multiple important or correlated tokens to be lost together, severely degrading video reconstruction. To address this issue, we propose a loss-resilient wireless video token communication (WVTC) framework. WVTC evaluates token importance from the intrinsic predictive structure of video tokens, assigning high priority to structural I-tokens and measuring P-token importance by temporal neighborhood novelty. A shuffled mixed I/P-token packetization scheme disperses structural anchors and correlated temporal regions across packets. Using only current block channel state information, an online scheduler jointly considers packet importance density, MCS-dependent decoding reliability, block capacity, and importance concentration when allocating packets to fading blocks. At the receiver, a fine-tuned detokenizer reconstructs missing content from surviving tokens without retransmission. Numerical results demonstrate improved perceptual quality and more graceful degradation under increasing packet error rates.

## Metadata
- **Published**: 2026-08-09T13:23:45Z
- **Authors**: Bingyan Xie, Yongjeong Oh, Zihan Chen, Jihong Park, Yongpeng Wu, Wenjun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08698v1)