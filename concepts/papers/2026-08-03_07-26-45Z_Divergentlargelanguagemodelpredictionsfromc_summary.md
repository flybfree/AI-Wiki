# Summary: 2026-08-03_07-26-45Z_Divergentlargelanguagemodelpredictionsfromconverge.md
Saved: 2026-08-03 23:43
Source: 2026-08-03_07-26-45Z_Divergentlargelanguagemodelpredictionsfromconverge.md
Model: None

---

## Summary  
The paper investigates how decoder‑only transformers resolve lexical ambiguity by analysing layer‑wise representations across three large models (GPT‑2‑Small, Llama‑3.2‑3B, Qwen2.5‑32B). It shows that while the embeddings converge, next‑token predictions diverge in later layers, revealing a mechanism where semantic distinctions become invisible to similarity measures. This work bridges the gap between internal representation and observable behaviour for ambiguous word pairs. The authors propose that embedding‑based tasks may be misled by apparent similarity despite true disambiguation.  

## Key Contributions  
- Finding 1: Representations of homonyms/polysemes diverge maximally in middle layers then partially reconverge, with maximum KL divergence between next‑token predictions occurring in final layers.  
- Finding 2: Causal activation patching demonstrates that late‑layer representational differences directly drive outputs despite low cosine similarity in embedding space.  
- Finding 3: Single‑layer ablation shows models achieve equivalent disambiguation through qualitatively different layer‑wise vulnerabilities.  

## Methodology  
The authors performed a three‑model, three‑parameter‑size study on both homonym and polysemantic word pairs. They extracted activation patches from each transformer layer, computed pairwise cosine similarity of embeddings, measured KL divergence between next‑token probability distributions, and conducted ablation experiments where only a single layer’s activations were altered to test causal impact.  

## Results  
Middle layers exhibited the greatest embedding dissimilarity (high cosine distance) while late layers showed reduced similarity. However, the final layers produced the highest prediction divergence, as reflected by peak KL divergence between model outputs. Activation patching confirmed that altering late‑layer representations changed predictions, whereas single‑layer ablation revealed that each layer contributes uniquely to disambiguation despite overall convergence.  

## Significance  
These results explain why large language models can produce correct disambiguated responses while embedding similarity metrics suggest otherwise, challenging the assumption that low cosine similarity implies lack of semantic difference. This has practical implications for semantic search, retrieval, and clustering pipelines that rely on late‑layer embeddings.  

## Related Concepts  
- Decoder‑only transformers  
- Lexical ambiguity (homonyms/polysemes)  
- Layer‑wise representation analysis  
- Causal activation patching  
- KL divergence between probability distributions  
- Cosine similarity in embedding space
