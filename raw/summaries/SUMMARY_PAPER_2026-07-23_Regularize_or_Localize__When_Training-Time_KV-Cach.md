---
title: Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization
url: http://arxiv.org/abs/2607.17019v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_01-13-09Z_RegularizeorLocalize_WhenTraining_TimeKV_CacheGeom.md
generated_at: 2026-07-23 23:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how a training-time regularization called sigreg influences the geometry of key-value cache states during language model training and whether that geometry benefits quantization. Experiments on an 110M‑parameter model show reduced pairwise cosine anisotropy in hidden states, modest perplexity increase, and significant improvements when the regularization is applied directly to the cache vectors.

## Key Takeaways
- At λ=0.01 sigreg cuts hidden-state pairwise-cosine anisotropy by 38% while perplexity rises less than 0.35% with no consistent zero‑shot loss.
- Directly applying sigreg to K and V reduces mean cache anisotropy by 94% across checkpoints, whereas frozen‑trunk retrofits do not reproduce the effect.
- Under coarse quantization scales direct kv regularization is the only condition that prefers per‑channel scaling, causing a 4.3–7.9× lower dnll than the baseline.

## Context
This work addresses a longstanding challenge in efficient inference: how to preserve model accuracy when compressing cache memory. By treating cache geometry as a trainable variable rather than a fixed artifact, researchers can guide quantization toward better storage and speed trade‑offs without sacrificing performance.

## Implications
For practitioners deploying large language models on edge devices, the findings suggest that fine‑grained training interventions may be more effective than post‑hoc scaling adjustments. The results also highlight the importance of matching regularization to quantizer configurations, offering a roadmap for balancing model size and inference speed in real‑world systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17019v1)
