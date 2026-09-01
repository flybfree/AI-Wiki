---
title: A.X K2 Technical Report
published: 2026-08-31T03:04:30Z
authors: Cheolseung Baek, Dhammiko Arya, Eunki Kim, Gun Song, Gyoungeun Han, Hyunho Yang, Hyunjun Eun, Jin Kim, Junyoung Park, Juyun Wee, Minki Hong, Minkyung Park, Minsang Kim, Minsoo Kang, SaeRom Kim, Sangjin Kim, Sangyeol Lee, Seojin Lee, Seokhwan Jo, Seokyoung Hong, Seongho Choi, Seonghye Cho, Seongmin Ok, Sereimony Sek, Seungmo Cho, Seungsik Kim, Singon Kim, Sohee Park, Sooyeon Park, Subin Yi, Sungbin Yoon, Sungeun Lee, Sung Jun Cheon, Sungwan Kim, Sunwoo Lee, Tae Yoon Kim, Wonbeom Jang, Yohan Ra, Yong-jin Han, Youngjin Kim, Youngrang Kim, Yujin Kang, Yujin Lee
url: http://arxiv.org/abs/2608.30181v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A.X K2 Technical Report

## Abstract
We introduce A.X K2, a 688B-parameter Mixture-of-Experts (MoE) language model trained from scratch as a high-performance foundation for \emph{agentic} applications. Trained on approximately 8.5T tokens---fewer than its predecessor, A.X K1---on a smaller but higher-quality mixture with substantially expanded agentic and software-engineering data, it nonetheless improves over A.X K1 across the board, by over 30 percentage points on some benchmarks, reflecting large gains in token efficiency. To support long contexts efficiently, we introduce Sparse Gated Attention (SGA), which combines sparse attention with gated attention, and adopt Gated Norm (GN) to stabilize large-scale training. SGA is trained natively at 128K through a \emph{sparse} indexer warmup that optimizes the indexer against its own sparse top-$k$ selection rather than the dense attention distribution, making adaptation markedly cheaper: each query reads only 2,048 positions, yet long-context quality is unchanged and A.X K2 scores 94.6 on RULER out to 256K. The outlier suppression of GN in turn keeps 4-bit NVFP4 serving within one point of FP8 accuracy. A simple yet effective Think-Fusion recipe further lets users switch between thinking and non-thinking modes within a single unified model. Extensive evaluations show that A.X K2 performs competitively against strong open-weight baselines, matching or exceeding them on math and Korean-language benchmarks.

## Metadata
- **Published**: 2026-08-31T03:04:30Z
- **Authors**: Cheolseung Baek, Dhammiko Arya, Eunki Kim, Gun Song, Gyoungeun Han, Hyunho Yang, Hyunjun Eun, Jin Kim, Junyoung Park, Juyun Wee, Minki Hong, Minkyung Park, Minsang Kim, Minsoo Kang, SaeRom Kim, Sangjin Kim, Sangyeol Lee, Seojin Lee, Seokhwan Jo, Seokyoung Hong, Seongho Choi, Seonghye Cho, Seongmin Ok, Sereimony Sek, Seungmo Cho, Seungsik Kim, Singon Kim, Sohee Park, Sooyeon Park, Subin Yi, Sungbin Yoon, Sungeun Lee, Sung Jun Cheon, Sungwan Kim, Sunwoo Lee, Tae Yoon Kim, Wonbeom Jang, Yohan Ra, Yong-jin Han, Youngjin Kim, Youngrang Kim, Yujin Kang, Yujin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30181v1)