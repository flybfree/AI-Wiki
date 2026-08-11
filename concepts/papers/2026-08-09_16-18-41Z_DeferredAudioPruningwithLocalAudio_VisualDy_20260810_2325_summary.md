# Summary: 2026-08-09_16-18-41Z_DeferredAudioPruningwithLocalAudio_VisualDynamicsf.md
Saved: 2026-08-10 23:25
Source: 2026-08-09_16-18-41Z_DeferredAudioPruningwithLocalAudio_VisualDynamicsf.md
Model: None

---

## Summary  
Omni‑modal large language models (LLMs) must handle audio, video, and text simultaneously, yet long sequences cause prohibitive prefill and KV‑cache costs. The authors introduce A‑PACK, a two‑stage framework that postpones audio pruning until multimodal queries arise, thereby exploiting the higher information density of audio relative to video and using local audio‑visual dynamics as a more effective cue for token selection. By preserving audio and compressing video with these dynamics before feeding tokens into the LLM, A‑PACK progressively removes low‑relevance audio and visual tokens together with their KV‑cache entries during decoding.

## Key Contributions  
- [Finding 1] Audio exhibits higher task‑relevant information density and representational diversity per token than video.  
- [Finding 2] Local audio‑visual dynamics provide a more effective cue for visual selection than token‑wise matching.  
- [Finding 3] A‑PACK achieves the strongest average performance among evaluated prior methods while reducing prefill FLOPs by up to 78% and improving decoding throughput by up to 2.21×.

## Methodology  
A‑PACK is a two‑stage compression pipeline. In Stage 1, the model processes audio and video with local dynamics that capture short‑term interactions; visual tokens are compressed using these dynamics while raw audio is retained unchanged. In Stage 2, during query generation, the LLM receives only the compressed visual tokens and retains full audio. The framework then iteratively prunes low‑relevance audio and visual tokens together with their KV‑cache entries as they become less useful for answering queries, allowing a gradual reduction of memory footprint without sacrificing downstream performance.

## Results  
Experiments on four benchmarks using Qwen2.5‑Omni‑7B/3B demonstrate that A‑PACK outperforms all prior compression techniques in average task accuracy. The method cuts prefill FLOPs by up to 78% and boosts decoding throughput by a factor of 2.21, confirming both the theoretical savings and practical speed gains. Ablation studies show that preserving audio while compressing video yields the best trade‑off between quality and efficiency.

## Significance  
Long multimodal sequences dominate real‑world applications such as video captioning and speech‑driven dialogue, where memory constraints are critical. By decoupling modality‑specific compression from LLM inference, A‑PACK offers a scalable path to deployable omni‑modal systems that retain high quality while dramatically reducing compute costs.

## Related Concepts  
omni‑modal LLMs, multimodal compression, KV‑cache, token pruning, local dynamics, audio‑visual interaction, query‑conditioned processing.
