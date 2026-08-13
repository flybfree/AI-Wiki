---
title: RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation
published: 2026-08-12T14:21:05Z
authors: Rong Chao, Sung-Feng Huang, Moreno La Quatra, Sabato Marco Siniscalchi, Wen-Huang Cheng, Szu-Wei Fu, Yu Tsao
url: http://arxiv.org/abs/2608.12099v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation

## Abstract
We present RT-SEMamba, a fully causal speech enhancement (SE) model built upon causal time-frequency Mamba blocks. Unlike Transformer-based architectures that rely on a growing key-value cache, Mamba propagates a fixed-size recurrent state per layer, enabling memory- and bandwidth-efficient long-form inference. We further introduce a progressive knowledge distillation (KD) strategy that compresses an 8-layer teacher into a shallow 1-layer student by jointly distilling complex spectral outputs and intermediate representations. On Voicebank-DEMAND, the 8-layer RT-SEMamba achieves 3.32 PESQ with a 25 ms algorithmic latency constraint, and the distilled 1-layer student improves over a naive 1-layer baseline from 3.06 to 3.18 PESQ while preserving the same steady-state RTF, delivering a 2.75x speedup over the teacher. These results demonstrate that state-space models with progressive KD provide a competitive quality-latency trade-off for real-time SE.

## Metadata
- **Published**: 2026-08-12T14:21:05Z
- **Authors**: Rong Chao, Sung-Feng Huang, Moreno La Quatra, Sabato Marco Siniscalchi, Wen-Huang Cheng, Szu-Wei Fu, Yu Tsao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12099v1)