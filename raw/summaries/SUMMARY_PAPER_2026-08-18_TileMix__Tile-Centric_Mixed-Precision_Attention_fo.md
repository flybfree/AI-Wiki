---
title: TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration
url: http://arxiv.org/abs/2608.17336v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_03-53-02Z_TileMix_Tile_CentricMixed_PrecisionAttentionforLLM.md
generated_at: 2026-08-18 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
TileMix introduces a tile-centric precision-routing kernel for LLM inference that partitions the attention matrix into hardware-aligned score tiles and uses bitmasks to dispatch each tile group through either FP16 or INT8 computation while updating a shared online-softmax state. The method preserves dense token connectivity without training, supports grouped-query attention, variable-length batches, and INT8 key/value caches. Benchmarks on LongEval, LV‑Eval, and A100 prefill show TileMix recovers long-context quality lost under uniform INT8 and improves throughput over FP16.

## Key Takeaways
- TileMix partitions the attention matrix into hardware-aligned score tiles and uses compact bitmasks to dispatch each tile group through either FP16 or INT8 computation while maintaining a shared online‑softmax state.
- The precision routing is executable at inference time, allowing mixed‑precision execution without sacrificing model connectivity.
- Benchmarks on LongEval, LV‑Eval, and A100 prefill show TileMix recovers long-context quality lost under uniform INT8 and improves throughput over FP16.

## Context
LLMs face quadratic memory and compute costs for long contexts due to dense self-attention. Existing mixed-precision strategies either apply a single precision globally or route individual tokens, which misaligns with hardware tile structures. TileMix addresses this by aligning precision decisions with hardware tiles, reducing overhead.

## Implications
This approach enables efficient inference on large models at scale where memory and latency are critical. Practitioners can adopt TileMix to balance accuracy and efficiency without retraining, supporting deployment of long-context LLMs in resource-constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17336v1)
