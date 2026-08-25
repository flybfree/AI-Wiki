---
title: SANE: State Anomaly Neutralization for Stable Extreme-Context Delta-Rule Models
published: 2026-08-23T10:41:07Z
authors: Qingwen Lin, Boyan Xu, Xiao Liu, Zhifeng Hao, Ruichu Cai
url: http://arxiv.org/abs/2608.22354v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SANE: State Anomaly Neutralization for Stable Extreme-Context Delta-Rule Models

## Abstract
Delta-Rule recurrent models maintain a fixed-size state, enabling $O(1)$ inference memory but potentially becoming unstable under extreme-context extrapolation. By tracking RWKV-7 over sequences of up to 100M tokens, we empirically identify a distinct failure pattern: \textbf{localized norm explosion atop a relatively sparse substrate}, rather than global state saturation. Analysis of the recurrent update suggests that persistent decay keeps weakly updated entries small, whereas uneven injections allow a few channels to accumulate extreme values. Motivated by this diagnosis, we propose \textbf{State Anomaly Neutralization (SANE)}, which applies adaptive $\tanh$ compression at chunk boundaries while preserving the intra-chunk parallel structure. Within a safe threshold range ($3 \le α\le 5$), SANE matches the baseline on 11 short-context reasoning benchmarks with no statistically significant degradation. After a 100M-token prefix, which exceeds the training length by over $24{,}000\times$, SANE retains functional reasoning ($33.46$--$35.56$) while the baseline encounters numerical overflow. In contrast, overly permissive thresholds ($α\ge 8$) remain numerically stable but lose reasoning capability entirely, showing that numerical stabilization alone does not guarantee functional reasoning and revealing a capacity--stability trade-off in state compression.

## Metadata
- **Published**: 2026-08-23T10:41:07Z
- **Authors**: Qingwen Lin, Boyan Xu, Xiao Liu, Zhifeng Hao, Ruichu Cai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22354v1)