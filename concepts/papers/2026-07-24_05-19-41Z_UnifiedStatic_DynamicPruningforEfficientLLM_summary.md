# Summary: 2026-07-24_05-19-41Z_UnifiedStatic_DynamicPruningforEfficientLLMInferen.md
Saved: 2026-07-26 21:38
Source: 2026-07-24_05-19-41Z_UnifiedStatic_DynamicPruningforEfficientLLMInferen.md
Model: None

---

## Summary  
Large language models (LLMs) suffer from severe compute and memory bottlenecks during autoregressive decoding, where low‑intensity kernels dominate inference cost. Existing sparse‑inference techniques are either purely static or fully dynamic, each with trade‑offs in adaptivity and runtime regularity. This paper introduces SPDP—a unified static‑dynamic pruning framework that co‑designs a new memory format and two GPU kernels to jointly exploit unstructured sparsity and input‑adaptive sparsity. By integrating these components, SPDP maintains high compute intensity while allowing fine‑grained activation skipping at runtime.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 6 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- **Finding 1**: A unified static‑dynamic pruning framework (SPD​P) that merges permanent weight removal with input‑sensitive dynamic pruning for LLM inference.  
- **Finding 2**: The Tiled‑Column-wise Bitmap Compressed (Tiled‑CBC) format, which stores unstructured sparsity in a column‑wise bitmap and supports hybrid activation‑aware decoding.  
- **Finding 3**: Two complementary GPU kernels: the CUDA‑core spMspV kernel employing HAD‑SMBD for runtime activation skipping, and the Tensor‑Core SpMM kernel optimized for prefill computation.

## Methodology  
SPD​P tackles the problem by first designing a memory layout that preserves unstructured sparsity while enabling fast bitmap decoding. The authors then develop two kernels: spMspV runs on CUDA cores using HAD‑SMBD to skip activations only when they are zero, preserving compute intensity; Tensor‑Core SpMM processes prefill tensors with maximal sparsity support. The static pruning step removes redundant weights once, and the dynamic step adapts at inference time based on actual input patterns, all within a single fused pipeline.

## Results  
Experimental evaluations on inference‑optimized GPUs show that SPD​P achieves an average speedup of 1.24×–1.37× over state‑of‑the‑art sparse frameworks such as SpInfer, with peak gains up to 2.51×. Crucially, perplexity remains unchanged even when sparsity is increased by up to 25 %, indicating that quality loss is negligible. The framework also improves performance‑per‑watt metrics, demonstrating substantial efficiency gains for large‑scale LLM serving.

## Significance  
By harmonizing static and dynamic pruning, SPD​P addresses the core challenges of compute intensity and bandwidth in autoregressive decoding. It enables higher sparsity without sacrificing model quality, thereby reducing hardware requirements and operational costs while maintaining inference latency. This work pushes the efficiency‑quality Pareto frontier forward, offering a practical path toward scalable LLM deployment.

## Related Concepts  
- Static pruning (SP) – permanent removal of redundant weights.  
- Dynamic pruning (DP) – runtime adaptation to input sparsity patterns.  
- Sparse inference – techniques that exploit zero‑weight entries for speedup.  
- Tiled‑Column-wise Bitmap Compressed (Tiled‑CBC) format – column‑wise bitmap storage of unstructured sparsity.  
- Hybrid Activation‑aware Dynamic Shared‑Memory Bitmap Decoding (HAD‑SMBD).  
- spMspV kernel – CUDA‑core implementation for runtime activation skipping.  
- Tensor‑Core SpMM kernel – optimized prefill computation on GPU tensor cores.  
- Autoregressive decoding – the inference paradigm that dominates LLM serving.
