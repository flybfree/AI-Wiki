# Summary: 2026-08-07_02-44-11Z_bioMoR_Biology_GuidedMixture_of_RecursionsforEffec.md
Saved: 2026-08-09 22:35
Source: 2026-08-07_02-44-11Z_bioMoR_Biology_GuidedMixture_of_RecursionsforEffec.md
Model: None

---

## Summary  
The paper introduces bioMoR, a biology‑guided Mixture‑of‑Recursions framework that learns from high‑dimensional omics data by allocating computation to only the most biologically relevant genes or pathways. By integrating structured biological knowledge into three specific locations within an MoR backbone—graph‑based embedding refinement, structural bias for self‑attention, and a graph‑aware router that selects recursion depth—the authors enable more efficient and interpretable genomic learning. The framework achieves substantial improvements over state‑of‑the‑art biology‑agnostic MoR baselines while using far fewer parameters and FLOPs than non‑recursive Transformers.

## Key Contributions  
- [Finding 1] bioMoR is the first model to apply Mixture‑of‑Recursions at both gene‑level and pathway‑level, demonstrating that recursive token selection can be guided by biological interaction graphs.  
- [Finding 2] The framework introduces three integrated knowledge points: (i) graph‑based information sharing that refines token embeddings, (ii) a structural bias that steers self‑attention toward biologically related tokens, and (iii) a router that uses neighborhood information to decide each token’s recursion depth.  
- [Finding 3] The method provides biological interpretability through selected marker genes/pathways and reveals how computation is allocated per token.

## Methodology  
The authors start with an MoR backbone that randomly routes tokens among expert sub‑networks, then replace the standard routing mechanism with a router that consults a pre‑computed gene interaction graph. This graph supplies neighborhood information to the router, which decides whether a token should be processed deeper (more recursions) or shallowly. The structural bias is enforced by modifying self‑attention scores so that attention weights are higher for tokens sharing edges in the graph. Finally, the embedding refinement step uses the same graph to update token vectors before routing, ensuring that biological context shapes both representation and computation depth.

## Results  
Across eight benchmarks covering diverse omics modalities—gene expression, methylation, proteomics, etc.—bioMoR achieved an average macro‑F1 increase of 8.2 percentage points and a balanced accuracy gain of 7.1 points compared with the strongest biology‑agnostic MoR baseline. It used only 75 % as many parameters and up to 58 % fewer FLOPs than a comparable non‑recursive Transformer, while maintaining a unified five‑fold cross‑validation protocol for evaluation.

## Significance  
bioMoR demonstrates that biologically informed routing can dramatically improve learning efficiency in high‑dimensional omics tasks, offering both computational savings and transparent insight into which genes or pathways receive deeper processing. This bridges the gap between black‑box deep models and the need for interpretable biological explanations, paving the way for more sustainable AI applications in genomics.

## Related Concepts  
Mixture‑of‑Recursions, token recursion depth, graph‑based embedding refinement, structural bias in self‑attention, graph‑aware router, biology‑guided learning, cross‑validation protocol.
