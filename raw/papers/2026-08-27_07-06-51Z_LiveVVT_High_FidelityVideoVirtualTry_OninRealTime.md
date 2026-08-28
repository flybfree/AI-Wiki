---
title: LiveVVT: High-Fidelity Video Virtual Try-On in Real Time
published: 2026-08-27T07:06:51Z
authors: Yushe Cao, Shikun Feng, Ruxiang Duan, Liyong Wang, Dianxi Shi, Chun Yu, Junliang Xing
url: http://arxiv.org/abs/2608.26714v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiveVVT: High-Fidelity Video Virtual Try-On in Real Time

## Abstract
Diffusion-based Video Virtual Try-On (VVT) achieves high visual fidelity through bidirectional spatio-temporal modeling, but complete-clip dependence incurs prohibitive latency and computational overhead in practical continuous deployment. Naively enforcing causality disrupts pretrained bidirectional priors and substantially degrades synthesis quality. We introduce LiveVVT, a rolling streaming diffusion framework that preserves bounded bidirectional modeling within causal recurrent generation. Within a fixed-size window, LiveVVT jointly denoises multiple video chunks under bounded look-ahead, preserving local bidirectional interactions while emitting one clean chunk per iteration. Beyond the window, two complementary memories sustain long-term consistency: a bounded temporal memory propagates recent dynamics and occlusion context, whereas a persistent global appearance memory, constructed once from the target garment and a frontal try-on keyframe, anchors garment details and dressed appearance throughout the stream. We further introduce a progressive distillation framework integrating bidirectional VVT learning, teacher-trajectory regression for causal few-step adaptation, and Collaborative Matching Distillation, which couples teacher-distribution matching with rolling flow matching on real videos to align optimization with recurrent inference. Experiments on paired and unpaired long-sequence benchmarks demonstrate superior generation quality over similarly sized models, with $26\times$ lower latency and $11\times$ higher throughput, enabling high-fidelity real-time streaming VVT.

## Metadata
- **Published**: 2026-08-27T07:06:51Z
- **Authors**: Yushe Cao, Shikun Feng, Ruxiang Duan, Liyong Wang, Dianxi Shi, Chun Yu, Junliang Xing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26714v1)