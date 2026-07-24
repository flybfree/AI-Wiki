# Summary: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Saved: 2026-07-24 02:45
Source: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Model: None

---

## Summary  
The paper proposes an Adaptive Depth Sparse Framework (AdaDSF) that converts off‑the‑shelf pre‑trained LLMs into depth‑sparse models without full retraining, thereby lowering inference cost while preserving performance. Its core contribution is a similarity‑driven resource allocation scheme that uses cosine similarity between layer inputs and outputs to determine token retention ratios. A lightweight router selects the most informative tokens at each layer, and an alignment objective ensures that sparse and dense representations match. The framework reduces FLOPs dramatically on GPT‑NeoX and Qwen2.5 while keeping accuracy close to the dense baseline.

## Key Contributions  
- Finding 1: Layers contribute unequally to representation transformation, which can be quantified by cosine similarity between layer input and output hidden states.  
- Finding 2: AdaDSF assigns a layer‑wise token retention ratio derived from these similarity statistics and employs a lightweight router to keep only the most informative tokens at each layer.  
- Finding 3: A feature‑preserving alignment objective is introduced to match intermediate and final representations between sparse and dense models.

## Methodology  
The authors first compute cosine similarities across all layers of a pre‑trained model, translating higher similarity into a higher retention ratio for that layer’s tokens. Using these ratios, they construct a per‑layer router that selects the top‑k tokens to retain, discarding others without altering the model’s architecture. To prevent loss of information, they train a lightweight alignment loss that minimizes the discrepancy between the dense output and the sparse output at each layer. No full fine‑tuning or task‑specific training is required; the framework operates on the original pre‑trained weights.

## Results  
AdaDSF reduces inference FLOPs by roughly 40 % on GPT‑NeoX and Qwen2.5 while maintaining language modeling and commonsense reasoning scores within a few percent of dense baselines. When sparsity levels are held constant, AdaDSF shows the smallest accuracy degradation among strong baselines such as MoD, D‑LLM, and DLO, indicating both efficiency and robustness.

## Significance  
By enabling efficient deployment of pre‑trained LLMs across diverse tasks with minimal adaptation cost, AdaDSF lowers hardware requirements and supports cross‑task reuse. This is especially valuable for resource‑constrained environments where full fine‑tuning or training from scratch is prohibitive.

## Related Concepts  
depth sparsity, cosine similarity between layer inputs/outputs, token retention ratio, lightweight router, feature‑preserving alignment objective, off‑the‑shelf LLM conversion, inference FLOPs reduction, accuracy degradation mitigation.
