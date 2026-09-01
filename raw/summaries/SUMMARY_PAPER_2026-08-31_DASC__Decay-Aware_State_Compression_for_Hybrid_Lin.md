---
title: DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving
url: http://arxiv.org/abs/2608.30386v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_07-42-43Z_DASC_Decay_AwareStateCompressionforHybridLinear_At.md
generated_at: 2026-08-31 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Decay-Aware State Compression (DASC) to address the memory challenges of hybrid linear‑attention models that rely on recurrent state updates. By analyzing the decay patterns of Gated DeltaNet and Kimi Delta Attention, DASC identifies retention horizons for different heads and channels, enabling selective compression of persistent state checkpoints without sacrificing performance. Experiments show up to 2.63× reduction in checkpoint size while maintaining competitive quality‑efficiency trade‑offs on retrieval and reasoning tasks.

## Key Takeaways
- Retention horizons vary across model components, allowing long‑term state units to be compressed while short‑lived ones are refreshed from a bounded suffix.  
- DASC packs selected state units into a ragged checkpoint layout and balances them across tensor‑parallel ranks for efficient TP inference.  
- The compression yields 42.6 % lower TTFT and 68.4 % higher input throughput under fixed memory budgets, with accuracy recovery via suffix refresh.

## Context
Hybrid linear‑attention architectures promise scalable serving by limiting key/value cache growth, yet their recurrent state management remains a bottleneck for large models. DASC tackles this by leveraging the intrinsic decay of model states, turning a theoretical observation into a practical compression strategy that fits within existing tensor‑parallel pipelines.

## Implications
For practitioners deploying massive open‑weight models, DASC offers a low‑overhead way to reduce memory pressure without retraining or extensive architectural changes. The approach can be adopted across various attention variants, promising faster inference and lower hardware costs in real‑world serving environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30386v1)
