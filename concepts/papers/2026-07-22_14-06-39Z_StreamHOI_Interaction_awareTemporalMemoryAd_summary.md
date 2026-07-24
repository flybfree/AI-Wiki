# Summary: 2026-07-22_14-06-39Z_StreamHOI_Interaction_awareTemporalMemoryAdaptatio.md
Saved: 2026-07-24 01:56
Source: 2026-07-22_14-06-39Z_StreamHOI_Interaction_awareTemporalMemoryAdaptatio.md
Model: None

---

## Summary  
The paper introduces StreamHOI, a low‑latency streaming framework for generating human‑object interaction (HOI) videos in real time. It addresses the challenge of preserving interactions across long video streams while meeting bounded latency constraints. Unlike prior methods that treat conditioning as static, StreamHOI designs memory organization to match transformer block behavior and enables interactive generation. The system achieves 17.6 FPS with a first‑chunk latency of 0.75 seconds.

## Key Contributions  
- Finding 1: Standard sink‑local memory design suffers from a trade‑off between interaction preservation and streaming efficiency in HOI video generation.  
- Finding 2: Different transformer blocks exhibit distinct historical‑memory preferences for interaction regions versus surrounding regions, necessitating block‑specific memory layouts.  
- Finding 3: Offline profiling of HOI‑aware blocks combined with bias‑guided training yields a memory‑specialized generator that improves long‑range access.

## Methodology  
The authors first map the interaction pipeline to streaming components, then conduct offline profiling to identify which transformer blocks dominate early and late interaction regions. They apply bias‑guided fine‑tuning so each block learns a tailored memory layout, inserting a distance scaling module that boosts retrieval of distant interaction states. The resulting generator streams video frames while maintaining interaction plausibility.

## Results  
Experimental evaluation shows StreamHOI outperforms long‑video baselines and recent HOI methods in interaction plausibility, object fidelity, human quality, and efficiency. It reaches 17.6 FPS with a first‑chunk latency of 0.75 seconds, confirming real‑time capability.

## Significance  
This work bridges the gap between offline high‑quality HOI generation and interactive streaming, enabling applications such as virtual assistants and augmented reality where low latency is critical. By decoupling memory design from conditioning complexity, StreamHOI offers a scalable template for other conditional video tasks.

## Related Concepts  
- Human‑object interaction (HOI) video generation  
- Streaming video synthesis  
- Temporal memory adaptation  
- Sink‑local memory design  
- Transformer block profiling  
- Bias‑guided fine‑tuning  
- Memory distance scaling
