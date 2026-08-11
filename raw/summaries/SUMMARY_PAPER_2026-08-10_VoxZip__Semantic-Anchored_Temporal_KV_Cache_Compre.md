---
title: VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference
url: http://arxiv.org/abs/2608.08569v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_08-17-18Z_VoxZip_Semantic_AnchoredTemporalKVCacheCompression.md
generated_at: 2026-08-10 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VoxZip, a train-free two‑stage compression framework that tackles the KV cache bottleneck in long‑context audio inference for speech large language models. By leveraging automatic speech recognition transcriptions as semantic anchors, VoxZip compresses and fuses audio tokens temporally, achieving up to 20× reduction in cache size while preserving high‑fidelity perception on short tasks.

## Key Takeaways
- The first stage replaces raw audio tokens with compressed representations anchored by ASR transcripts, dramatically lowering the initial KV cache memory footprint without sacrificing semantic information density.  
- A second dynamic filtering step uses temporally decayed accumulated attention to selectively evict non‑essential tokens, mitigating early‑token bias and further boosting compression ratios.  
- On Qwen3‑Omni across six audio benchmarks, VoxZip maintains over 90% of the uncompressed baseline performance even at a 20× compression ratio, delivering a 1.9× increase in inference throughput and a 3.3× reduction in peak memory usage.

## Context
Long‑context audio processing is a critical bottleneck for next‑generation speech large language models, where KV cache size scales quadratically with sequence length. Existing text‑centric compression techniques often disrupt temporal continuity or discard essential acoustic cues, limiting their applicability to spoken data. VoxZip’s semantic‑anchored approach addresses these limitations by aligning audio tokens with linguistic semantics.

## Implications
For researchers, VoxZip offers a practical path to deploy state‑of‑the‑art models on resource‑constrained devices without retraining. For industry practitioners, the framework enables real‑time long‑audio reasoning at lower latency and memory cost, opening new possibilities for voice assistants and streaming services that handle extended conversations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08569v1)
