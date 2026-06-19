---

title: "Summary: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion"
url: http://arxiv.org/abs/2605.30351v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-28_17-59-57Z_VideoMLA_Low_RankLatentKVCacheforMinute_ScaleAutor.md
generated_at: "2026-06-11 10:49"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces VideoMLA, a method for compressing the key‑value cache in causal video diffusion models by replacing per‑head keys and values with a shared low‑rank content latent and a decoupled 3D‑RoPE positional key. Experiments show that this replacement cuts KV memory usage by 92.7 % without sacrificing performance, especially at long rollout horizons.

## Key Takeaways
- VideoMLA reduces per‑token KV memory by 92.7 % while preserving video quality across all cached layers.  
- The compression works despite the pretrained attention spectrum having a high effective rank (≈99 %), indicating that the bottleneck is not the spectral approximation but the MLA bottleneck itself.  
- Throughput on B200 improves by 1.23×, and VideoMLA achieves the best overall score at long horizons compared with other baselines.

## Context
Video diffusion models rely heavily on streaming KV caches to balance quality and latency, yet most recent work only modifies token selection or encoding within a fixed layout. This paper addresses that limitation by rethinking the cache structure itself, offering a scalable alternative that could benefit any autoregressive video generation system.

## Implications
For practitioners developing real‑time video diffusion pipelines, VideoMLA provides a clear path to lower memory footprints and higher throughput without retraining models. The approach may also inspire similar low‑rank adaptations for other long‑range generative tasks beyond video.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.30351v1)
