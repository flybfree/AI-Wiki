---
title: KuaFu: Compressing Long User Behavior into Understanding at Billion Scale
published: 2026-09-25T09:39:39Z
authors: Jiahao Hui, Lin Zhu, Yishen Hu, Jingdong Shu, Zetai Jiang, Xining Ran, Ben Tan, Yeshou Cai, Gong Chen, Haijie Gu, Jie Jiang
url: http://arxiv.org/abs/2609.31045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KuaFu: Compressing Long User Behavior into Understanding at Billion Scale

## Abstract
Conversational agents, generative recommenders, and personalized advertising all rest on one capability: understanding each user from raw behavior. Prevailing industrial practice is task-specific: for each task, a relevant subsequence is extracted from the full history and a dedicated model trained on it. In production it hits two bottlenecks. First, even after filtering, a single-task sequence stays extremely long: content-interest summarization reads several hundred items per user, tens of thousands of tokens once serialized as prompt text. Second, profiles are refreshed routinely: a billion users weekly, roughly 100K QPM in aggregate, which under a fixed GPU budget sets a hard throughput floor. Compression is therefore mandatory, yet truncation or coarse compression can silently distort the profile, introducing four hallucination types (fabrication, omission, date misattribution, broken logic) that, with no way to evaluate the compressed representation itself, surface only as diffuse degradation in downstream metrics. We present KuaFu, a unified behavior-compression layer whose minimal unit is one behavior item. A two-axis projector compresses each item into 2-4 tokens of width 128-256 (about 10x along the token axis, 20x along width; per-item cache 10 KB to 0.5 KB), with fidelity-oriented four-stage training and layered intermediate evaluation. Across four production profiling tasks it matches or exceeds uncompressed single-task production models on all five headline metrics, raises per-GPU throughput by 37%-350%, and saves 190 GPUs. On public benchmarks it nearly always beats prior compressors at the same compression ratio (up to +17.7 EM on out-of-domain MRQA); on RecBench, a 4B model surpasses its 8B counterpart by 1.90 points. KuaFu has run on the Tencent advertising and recommendation platform for ten months, lifting overall GMV by 1.37%.

## Metadata
- **Published**: 2026-09-25T09:39:39Z
- **Authors**: Jiahao Hui, Lin Zhu, Yishen Hu, Jingdong Shu, Zetai Jiang, Xining Ran, Ben Tan, Yeshou Cai, Gong Chen, Haijie Gu, Jie Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31045v1)