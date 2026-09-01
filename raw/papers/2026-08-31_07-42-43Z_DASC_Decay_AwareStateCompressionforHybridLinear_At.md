---
title: DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving
published: 2026-08-31T07:42:43Z
authors: Yanqi Yu, Pingwei Sun, Jianchao Tan, Tao Zhang, Yuchen Xie, Xunliang Cai, Yao Liu
url: http://arxiv.org/abs/2608.30386v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving

## Abstract
Hybrid linear-attention architectures have recently scaled to large open-weight models, offering quality competitive with full attention while substantially reducing key/value (KV) cache growth. However, their in-place recurrent-state updates complicate cache management: prefix reuse requires state checkpoints alongside full-attention KV, while storing state checkpoints in full increases memory pressure, leading to more evictions and repeated prefill. By analyzing the decay structure of Gated DeltaNet (GDN) and Kimi Delta Attention (KDA), we find that different heads and channels retain prefix information over markedly different timescales, which we term \emph{retention horizons}. This variation suggests substantial compression potential in persistent state checkpoints. Building on this observation, we introduce \emph{Decay-Aware State Compression} (DASC), which derives retention horizons from model weights, selects long-horizon state units, and packs them into a ragged state checkpoint layout. To integrate efficiently with tensor-parallel inference engines, DASC furtherly balances compressed state checkpoints across TP ranks. On reuse, DASC either zero-fills omitted units or refreshes them from a bounded suffix with additional compute cost. Across retrieval and end-to-end reasoning benchmarks on Kimi-Linear, conservative DASC configurations remain close to full caching while compressing KDA recurrent state checkpoints by $2.63\times$. Under fixed state checkpoint memory budgets, the resulting capacity gains reduce mean Time to First Token (TTFT) by 42.6\% and improve input throughput by 68.4\%. At larger compression ratio, suffix refresh recovers much of the accuracy lost to more aggressive omission, at the cost of additional replay computation. Qwen with GDN exhibits a similar quality--efficiency trend, showing that DASC extends from channel-wise KDA to head-wise GDN.

## Metadata
- **Published**: 2026-08-31T07:42:43Z
- **Authors**: Yanqi Yu, Pingwei Sun, Jianchao Tan, Tao Zhang, Yuchen Xie, Xunliang Cai, Yao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30386v1)