# Summary: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Saved: 2026-07-24 02:52
Source: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Model: None

---

## Summary  
The paper proposes the Adaptive Depth Sparse Framework (AdaDSF), a method that reduces inference cost of large language models by converting them into depth‑sparse architectures without full retraining. By exploiting cosine similarity between layer inputs and outputs, AdaDSF learns to retain only the most informative tokens at each level, thereby cutting FLOPs while keeping performance near that of dense models. The framework also introduces a lightweight router and an alignment objective to ensure feature preservation across sparse and dense representations.

## Key Contributions  
- [Finding 1] Layer‑wise token retention ratios are derived from cosine similarity statistics between input and output hidden states, identifying which layers contribute most to representation transformation.  
- [Finding 2] A lightweight router selects the retained tokens at each layer, enabling depth sparsity without retraining or task‑specific fine‑tuning.  
- [Finding 3] An alignment loss is introduced to match intermediate representations of sparse and dense models, preserving feature fidelity.

## Methodology  
AdaDSF first computes cosine similarity across all layers, normalizing it into a token retention ratio that indicates how many tokens should be kept per layer. These ratios are used by a simple router to zero‑out the least informative tokens during forward pass. During training, an alignment objective penalizes mismatches between sparse and dense hidden states, encouraging the sparse model to retain essential information. The process is fully online; no full retraining or task adaptation is required.

## Results  
Experiments on GPT‑NeoX and Qwen2.5 for language modeling and commonsense reasoning show that AdaDSF reduces inference FLOPs by up to 40 % while maintaining performance within 1–2 % of the dense baseline. Under comparable sparsity levels, AdaDSF yields smaller accuracy degradation than strong baselines such as MoD, D‑LLM, and DLO.

## Significance  
AdaDSF demonstrates that pre‑trained LLMs can be efficiently deployed across diverse tasks with minimal adaptation cost, offering a scalable path to lower‑cost inference in real‑world applications. By preserving performance through similarity‑driven sparsity, the method addresses a key bottleneck in LLM scaling.

## Related Concepts  
- Depth sparsity: selective removal of tokens at specific layers.  
- Cosine similarity: measure of alignment between vectors.  
- Token retention ratio: proportion of tokens kept per layer.  
- Feature alignment loss: optimization to match sparse and dense representations.  
- Lightweight router: algorithm that selects retained tokens during inference.
