# Summary: 2026-07-25_21-17-57Z_ExplainingBiomedCLIPwithWeightedBanzhafInteraction.md
Saved: 2026-07-27 23:50
Source: 2026-07-25_21-17-57Z_ExplainingBiomedCLIPwithWeightedBanzhafInteraction.md
Model: None

---

## Summary  
Vision‑Language Models (VLMs) such as BiomedCLIP excel at medical image classification, yet their explanations are often fragmented because tokenizers break multi‑word clinical terms into meaningless subwords. This fragmentation inflates the combinatorial space of possible interactions and produces noisy cross‑modal attributions that clinicians cannot interpret. The authors propose ParseFIxLIP, an extension of FIxLIP that uses Tree‑Gram parsing to group tokens into semantically coherent units, thereby restoring the model’s reasoning structure. By integrating a smart depth strategy based on spaCy dependency trees, they achieve more interpretable and stable explanations without sacrificing performance.

## Key Contributions  
- **Semantic Token Grouping via Dependency Parsing:** ParseFIxLIP leverages Tree‑Gram parsing to cluster tokens that belong to the same medical concept (e.g., “saddle embolus”) into a single player, eliminating fragmentation.  
- **Weighted Banzhaf Interaction Game with Smart Depth:** The method refines the classic Banzhaf game by assigning weights proportional to token depth in the parse tree, ensuring only locally related tokens influence each other’s attribution scores.  
- **Quantitative Robustness and Semantic Parsimony:** Experiments show that ParseFIxLIP maintains high accuracy on long captions while reducing the number of salient cross‑modal interactions compared with baseline FIxLIP.

## Methodology  
The authors start from the Banzhaf interaction framework, which treats each token as a player whose influence is defined by pairwise comparisons. Instead of using raw tokens, they first parse the caption with spaCy to obtain a dependency tree. Tokens are then grouped according to their syntactic depth, creating “explanation players” that represent whole medical phrases. The weighted Banzhaf game is solved on these groups, and attribution scores are back‑propagated to the original model. This approach replaces noisy subword tokens with coherent units, preserving the model’s internal reasoning while providing human‑readable explanations.

## Results  
On a held‑out set of ROCOv2 medical images paired with clinical captions, ParseFIxLIP achieves an average top‑1 accuracy of 84.3 %—only 0.7 % lower than the best FIxLIP baseline (85.0 %). More importantly, the number of high‑weight interactions drops by 62 %, and the distribution of attribution scores becomes more concentrated around a few semantically meaningful tokens rather than spreading across many subwords. Qualitative inspection reveals that explanations now correctly attribute predictions to whole phrases such as “saddle embolus” instead of isolated fragments like “saddle” or “embolus”. The method also outperforms on general English captions, confirming robustness beyond the medical domain.

## Significance  
Providing interpretable, clinically relevant explanations is essential for trustworthy deployment of VLMs in healthcare. ParseFIxLIP bridges the gap between high‑level reasoning and token‑level attribution by respecting syntactic structure, offering a scalable solution that can be applied to any model employing FIxLIP’s interaction game.

## Related Concepts  
- BiomedCLIP: a multimodal model for medical image classification.  
- FIxLIP: an existing explanation framework based on the Banzhaf interaction game.  
- Tree‑Gram parsing: a technique that groups tokens according to their depth in a dependency parse tree.  
- spaCy dependency tree: provides syntactic hierarchy used for grouping tokens.  
- Weighted Banzhaf interaction: modifies the classic Banzhaf model with token‑depth weights.
