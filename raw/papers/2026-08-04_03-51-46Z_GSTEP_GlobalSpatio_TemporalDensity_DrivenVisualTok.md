---
title: GSTEP: Global Spatio-Temporal Density-Driven Visual Token Pruning for Efficient Video Large Language Models
published: 2026-08-04T03:51:46Z
authors: Mengjie Zhang, Qihui Zhu, Tao Zhang, Shuangwu Chen, Huihuang Qin, Yu Guo, Shenghao Ye, Zijian Wen, Yunpeng Hou, Dong Jin, Xiaobin Tan, Huasen He, Jian Yang
url: http://arxiv.org/abs/2608.03083v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GSTEP: Global Spatio-Temporal Density-Driven Visual Token Pruning for Efficient Video Large Language Models

## Abstract
Video large language models (VideoLLMs) achieve strong video understanding performance, but their inference remains expensive due to the large number of redundant spatio-temporal visual tokens in long videos. Existing token pruning methods alleviate this cost by reducing redundant tokens, yet most of them rely on segment-level local pruning, where videos are partitioned into isolated segments and tokens are selected independently within each segment. Such designs may under-preserve short but semantically dense segments and discard tokens that appear non-salient locally but remain critical from a global perspective. To address this issue, we propose GSTEP (Global Spatio-Temporal Density Pruning), a plug-and-play pruning framework that models video as a continuous spatio-temporal information flow. GSTEP constructs a token-level spatio-temporal density by combining a continuous temporal density, obtained from a smoothed centered frame-level change signal, with intra-frame spatial density, and then performs global token sampling by jointly balancing information density and coverage. Extensive experiments on multiple VideoLLMs and public benchmarks demonstrate that GSTEP consistently achieves strong accuracy-efficiency trade-offs and generalizes well across model architectures and evaluation settings. On LLaVA-OneVision-7B, GSTEP prunes 75% of visual tokens, preserves up to 100.2% of the original average performance across benchmarks, and achieves a 1.17 end-to-end speedup.

## Metadata
- **Published**: 2026-08-04T03:51:46Z
- **Authors**: Mengjie Zhang, Qihui Zhu, Tao Zhang, Shuangwu Chen, Huihuang Qin, Yu Guo, Shenghao Ye, Zijian Wen, Yunpeng Hou, Dong Jin, Xiaobin Tan, Huasen He, Jian Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03083v1)