---
title: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating
published: 2026-07-22T06:32:34Z
authors: Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu
url: http://arxiv.org/abs/2607.19802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Zero-Observation User Reactivation with Gap-Driven Dimensional Gating

## Abstract
Sequential recommendation (SR) models capture continuously observed behavior, but a returning user may have no interactions for months or years. We define this setting as Zero-Observation Reactivation: the user has a pre-gap history, while the platform observes no behavioral signals during a macro-gap Delta t. Under a chronologically aligned Gap-Synthesize Protocol on three Amazon datasets (Video Games, CDs & Vinyl, and Movies & TV), Hit@10 decreases monotonically across the evaluated gap buckets and reaches its lowest level beyond one year. The pattern appears across recurrent, unidirectional, and bidirectional SR backbones.   We propose DeltaGate, a lightweight output-layer plugin that keeps the backbone frozen and routes each representation dimension between the personalized history and a learned, zero-initialized global prior. The gate is conditioned jointly on Delta t and the personalized representation. In a controlled diagnostic, we hold the personalized representation fixed and vary Delta t to isolate the trained gate's response to the gap input. In the >365d Video Games bucket, DG-SASRec reaches 0.047 Hit@10 versus 0.031 for SASRec, while DG-BERT4Rec reaches 0.046 versus 0.025 for BERT4Rec, with 66K trainable parameters (2--4% overhead). End-to-end retraining attains higher absolute accuracy but changes the backbone embeddings; the frozen plugin preserves zero backbone drift, uses about 40x fewer trainable parameters, and retains observable dimension-wise routing. The source code is available at https://github.com/jdding/DeltaGate.

## Metadata
- **Published**: 2026-07-22T06:32:34Z
- **Authors**: Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19802v1)