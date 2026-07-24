# Summary: 2026-07-22_14-06-39Z_StreamHOI_Interaction_awareTemporalMemoryAdaptatio.md
Saved: 2026-07-24 01:59
Source: 2026-07-22_14-06-39Z_StreamHOI_Interaction_awareTemporalMemoryAdaptatio.md
Model: None

---

## Summary  
The paper proposes StreamHOI, a low‑latency streaming framework for generating long‑duration human‑object interaction (HOI) videos that can be used in real‑time interactive applications. Unlike existing offline pipelines that require complex driving conditions, StreamHOI focuses on organizing the generator’s historical memory to keep interactions coherent while respecting bounded latency. The authors demonstrate that conventional sink‑local memory designs create trade‑offs between early and later interaction regions, prompting a block‑specific memory adaptation strategy. Their solution combines offline profiling of transformer blocks with bias‑guided training and a novel distance‑scaling module, achieving real‑time performance comparable to long‑video baselines.

## Key Contributions  
- [Finding 1] The standard sink‑local memory design exhibits a trade‑off in streaming HOI generation, where different transformer blocks preferentially retain either early interaction states or later ones.  
- [Finding 2] Offline HOI‑aware block profiling combined with bias‑guided memory‑specialized training enables the generator to adopt block‑specific memory layouts that match their historical preferences.  
- [Finding 3] A memory distance scaling module is introduced to enhance long‑range access to early interaction states, improving temporal coherence.

## Methodology  
The authors approach the problem by first analyzing how each transformer block in an image‑to‑video generator stores and retrieves past frames during streaming. They conduct offline profiling to map these preferences onto a memory layout that prioritizes relevant historical content for each block. Using this mapping, they apply bias‑guided training so the model learns to weight certain memory slots more heavily. Finally, they augment the architecture with a distance scaling module that adjusts attention weights based on temporal distance, ensuring early interactions remain salient even when many frames have been generated.

## Results  
Experimental evaluation shows that StreamHOI outperforms both long‑video baselines and recent HOI generation methods in interaction plausibility, object fidelity, human quality, and efficiency. The system reaches 17.6 FPS with a first‑chunk latency of only 0.75 seconds, demonstrating strong real‑time performance while preserving high visual realism.

## Significance  
StreamHOI bridges the gap between offline HOI video generation and interactive streaming applications by providing a memory‑adaptation strategy that reduces latency without sacrificing quality. This makes it feasible to generate long‑duration human‑object interaction videos in real time, opening possibilities for live avatar control, immersive AR/VR experiences, and other low‑latency interactive media.

## Related Concepts  
- Streaming video generation  
- Human‑Object Interaction (HOI) video generation  
- Transformer blocks and memory layout  
- Sink‑local memory design  
- Bias‑guided training  
- Memory distance scaling module
