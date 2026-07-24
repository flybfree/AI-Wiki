# Summary: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Saved: 2026-07-24 03:00
Source: 2026-07-23_13-13-04Z_AdaptiveDepthSparseFramework_Similarity_DrivenReso.md
Model: None

---

## Summary  
The paper introduces Adaptive Depth Sparse Framework (AdaDSF), which reduces the inference cost of pre‑trained large language models by sparsifying individual layers without requiring full retraining or task‑specific fine‑tuning. It leverages cosine similarity between layer input and output hidden states to quantify each layer’s contribution, then assigns token retention ratios that reflect how much information should be preserved. A lightweight router selects only the most informative tokens at each layer, producing a depth‑sparse model. Finally, an alignment objective ensures the sparse representation matches the dense one, minimizing accuracy loss.  

## Key Contributions  
- Finding 1: Layer contribution is measured by cosine similarity between input and output hidden states, enabling efficient sparsity design.  
- Finding 2: A lightweight router selects tokens based on retention ratios, achieving depth‑sparse models with minimal overhead.  
- Finding 3: A feature‑preserving alignment objective aligns sparse and dense representations, minimizing accuracy degradation.  

## Methodology  
The authors first compute similarity statistics for each layer of a pre‑trained LLM by calculating the cosine similarity between its input and output hidden states. From these statistics they derive token retention ratios that indicate how much information should be retained at each layer. These ratios guide a lightweight router that keeps only the most informative tokens, generating a depth‑sparse model. To maintain representation fidelity, an alignment loss is introduced that minimizes the difference between dense and sparse outputs across all layers, ensuring the sparse model reproduces the same behavior as the original dense network.  

## Results  
AdaDSF reduces inference FLOPs by up to 60 % compared with dense models on GPT‑NeoX and Qwen2.5 while achieving only a 1–3 % drop in perplexity or commonsense reasoning scores, outperforming strong baselines such as MoD, D‑LLM, and DLO under comparable sparsity levels.  

## Significance  
This work demonstrates that sparsity can be applied adaptively to pre‑trained LLMs without retraining, lowering computational cost for deployment. By aligning sparse representations with dense ones, it preserves performance across diverse tasks, enabling efficient inference on edge devices or low‑power hardware.  

## Related Concepts  
- Pre‑trained large language models (LLMs)  
- Depth sparsity / depth‑wise token pruning  
- Cosine similarity between hidden states  
- Lightweight router mechanisms  
- Feature‑preserving alignment loss
