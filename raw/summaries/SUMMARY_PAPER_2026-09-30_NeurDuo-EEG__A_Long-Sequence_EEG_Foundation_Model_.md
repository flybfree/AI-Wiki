---
title: NeurDuo-EEG: A Long-Sequence EEG Foundation Model with Persistent State and Explicit Memory
url: http://arxiv.org/abs/2609.38587v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_21-46-11Z_NeurDuo_EEG_ALong_SequenceEEGFoundationModelwithPe.md
generated_at: 2026-09-30 21:10
model: qwen3.6-35b-a3b
---

## Summary
NeurDuo-EEG introduces a causal foundation model for electroencephalography that overcomes the limitations of fixed-window processing by implementing channel-resolved persistent memory with multi-timescale management. By employing learned consolidation and selective retrieval mechanisms, the model captures long-range temporal dynamics within a fixed-size state, enabling continuous analysis of EEG data spanning hours. Pre-trained on 3,955 hours of data across 17 datasets, NeurDuo-EEG achieves state-of-the-art performance in seizure detection and competitive results in sleep staging while supporting efficient streaming inference with constant latency as history grows.

## Key Takeaways
- NeurDuo-EEG addresses the implicit compression of long-range information in standard state-space models by introducing a channel-resolved persistent memory architecture that utilizes learned consolidation and selective retrieval to maintain explicit, multi-timescale representations within a fixed-size state for continuous EEG modeling.
- The model demonstrates superior empirical performance across diverse benchmarks, achieving the best results on four out of five downstream tasks including all short-window tasks; notably, it improves seizure detection AUC-PR from 0.285 to 0.471 over the strongest non-Ne

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38587v1)
