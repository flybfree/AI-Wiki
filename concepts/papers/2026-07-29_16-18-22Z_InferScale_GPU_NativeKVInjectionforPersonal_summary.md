# Summary: 2026-07-29_16-18-22Z_InferScale_GPU_NativeKVInjectionforPersonalizedLLM.md
Saved: 2026-07-29 20:43
Source: 2026-07-29_16-18-22Z_InferScale_GPU_NativeKVInjectionforPersonalizedLLM.md
Model: None

---

## Summary  
The paper proposes InferScale, a GPU‑native memory system that injects precomputed key‑value (KV) states into the vLLM serving pipeline to replace repeated prompt prefilling with long‑term user memories. By storing KV representations alongside semantic embeddings on the GPU and using rotary‑position aware storage, the method reduces time‑to‑first‑token latency as retrieval budgets grow while keeping model output quality high. The authors introduce two novel techniques: Chunked RoPE for handling dynamic memory under rotary embeddings and Context‑Window Encoding to preserve cross‑fact context without re‑encoding KV states. These contributions enable a scalable, low‑latency LLM serving architecture that decouples memory size from serving performance.

## Key Contributions  
- [Finding 1] InferScale replaces prompt prefilling with reusable KV state stored on the GPU, eliminating redundant computation and preserving latency across increasing retrieval budgets.  
- [Finding 2] Chunked RoPE stores keys before rotation and applies their serving‑time positions during injection, enabling correct rotary embedding handling for dynamically assembled memories.  
- [Finding 3] Context‑Window Encoding captures a small window of preceding conversation context with each fact while caching only the target fact’s KV, mitigating loss of cross‑fact interaction.

## Methodology  
The authors built InferScale as an extension to vLLM’s KV‑connector interface, requiring no changes to the serving engine or model fine‑tuning. They precompute each memory fact’s KV representation and embed it with a semantic vector on the GPU. At serving time, they retrieve relevant facts using a similarity search, apply Chunked RoPE to obtain correct rotary positions, and inject the resulting KV pairs directly into vLLM’s paged cache via Context‑Window Encoding. This pipeline decouples memory retrieval from model inference.

## Results  
Experiments on three open‑weight models evaluated with LoCoMo show that at a retrieval budget of k=50, InferScale reduces time‑to‑first‑token by 72–79% (3.6–4.8× improvement) compared to Mem0 without recomputing serving positions. Accuracy remains high: 60.3 % versus 63.3 % for Mem0. Throughput under concurrent load is boosted 3.7–4.5×, confirming that reusable KV state decouples latency from retrieved‑context size.

## Significance  
InferScale addresses a critical bottleneck in personalized LLM serving: growing memory budgets increase latency without improving user experience. By leveraging GPU resources for precomputation and direct KV injection, the system offers scalable, low‑latency personalization that can be deployed across diverse models with minimal engineering effort.

## Related Concepts  
- vLLM (GPU‑native LLM serving engine)  
- Key‑Value (KV) representation of model states  
- Rotary Position Embedding (RoPE) and its variants  
- Chunked RoPE for dynamic memory handling  
- Context‑Window Encoding for preserving local interaction context
