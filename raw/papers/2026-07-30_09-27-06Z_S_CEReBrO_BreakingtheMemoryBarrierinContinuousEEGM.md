---
title: S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring
published: 2026-07-30T09:27:06Z
authors: Glenn Anta Bucagu, Thorir Mar Ingolfsson, Yawei Li, Luca Benini
url: http://arxiv.org/abs/2607.27913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring

## Abstract
Foundation models offer a promising paradigm for Electroencephalography (EEG) analysis, leveraging generalizable representations from vast unlabeled datasets. Yet, Transformer-based architectures face a critical bottleneck: global attention mechanisms couple the attention memory state to the signal duration, causing memory overflow during continuous monitoring. To address this, we introduce S-CEReBrO (Streaming CEReBrO), an evolution of the CEReBrO architecture designed for continuous monitoring. Our novel Windowed Alternating Attention mechanism factorizes attention computation into fixed-size spatiotemporal windows, guaranteeing constant KV cache memory as only the active window requires resident attention maps. Empirical scaling analysis confirms that windowed alternating attention can process signals 100X longer than full self-attention and 3X longer than low-rank linear attention. Compared to low-rank linear attention on long contexts, windowed alternating attention requires 55% of the memory while increasing inference throughput by 2.1X. Pre-trained on >25,000 hours of recordings from >12,000 subjects, S-CEReBrO achieves state-of-the-art performance on 7 of 11 downstream tasks, with up to 60% fewer parameters. This work represents a significant step toward the realization of efficient, generalizable, and continuous EEG monitoring. An accompanying code repository is available.

## Metadata
- **Published**: 2026-07-30T09:27:06Z
- **Authors**: Glenn Anta Bucagu, Thorir Mar Ingolfsson, Yawei Li, Luca Benini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27913v1)