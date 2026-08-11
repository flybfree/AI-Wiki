---
title: Deferred Audio Pruning with Local Audio-Visual Dynamics for Omni-LLMs
url: http://arxiv.org/abs/2608.08794v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_16-18-41Z_DeferredAudioPruningwithLocalAudio_VisualDynamicsf.md
generated_at: 2026-08-10 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces A-PACK, a two‑stage framework that defers audio pruning until multimodal interactions emerge, showing audio has higher task‑relevant information density than video. It preserves audio while compressing video using local dynamics and then progressively removes low‑relevance tokens inside the LLM. Across benchmarks, A-PACK achieves strongest performance with up to 78% prefill FLOP reduction and 2.21× decoding throughput gain. The framework also preserves audio fidelity, ensuring no loss in downstream tasks.

## Key Takeaways
- Audio exhibits higher task‑relevant information density per token than video, making it less suitable for early compression.
- Local audio‑visual dynamics provide a more effective cue for visual selection than token‑wise matching.
- A-PACK reduces prefill FLOPs by up to 78% and improves decoding throughput by up to 2.21× while maintaining or improving performance.

## Context
In omni‑modal LLMs, long sequences cause heavy prefill and KV‑cache costs, limiting scalability. Existing compression focuses on token reduction before the model, ignoring modality‑specific optimizations.

## Implications
This work demonstrates that modality‑aware pruning can be integrated seamlessly within LLM inference pipelines, offering a path to lower compute budgets for large multimodal systems. Practitioners can adopt similar two‑stage strategies to balance quality and efficiency in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08794v1)
