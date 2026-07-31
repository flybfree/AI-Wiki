---
title: Prox: Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience in LLMs
url: http://arxiv.org/abs/2607.27591v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_02-20-01Z_Prox_Training_FreeFFNActivationSparsityviaApproxim.md
generated_at: 2026-07-30 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Prox, a training‑free framework that sparsifies the feed‑forward network of large language models by exploiting the magnitude ranking of SwiGLU intermediate states. The method constructs a shared channel mask from input sparsity and quantized proxy weights, then computes only the selected channels for all three FFN projections, achieving high sparsity without model retraining.

## Key Takeaways
- Prox replaces dense intermediate‑state computation with a magnitude ranking that yields an effective channel mask, reducing memory traffic while preserving performance.  
- The framework achieves up to 1.99× end‑to‑end decoding speedup at 70 % FFN sparsity across ten models from six families.  
- Prox is compatible with quantization and sparse attention, enabling integration into existing inference pipelines.

## Context
Large language model inference is dominated by feed‑forward layers that consume most compute and memory, so any reduction in these operations directly improves deployment efficiency. Training‑free sparsification methods are attractive because they avoid costly retraining while still targeting the same bottleneck components.

## Implications
For practitioners, Prox offers a practical path to faster, lower‑power LLM serving without sacrificing quality, especially when combined with quantization or sparse attention strategies. The approach may become standard in model optimization toolkits aimed at maximizing throughput on edge devices and cloud servers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27591v1)
