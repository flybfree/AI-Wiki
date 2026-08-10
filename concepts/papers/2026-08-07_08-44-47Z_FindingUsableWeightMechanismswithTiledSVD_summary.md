# Summary: 2026-08-07_08-44-47Z_FindingUsableWeightMechanismswithTiledSVD.md
Saved: 2026-08-09 22:51
Source: 2026-08-07_08-44-47Z_FindingUsableWeightMechanismswithTiledSVD.md
Model: None

---

## Summary  
The paper tackles the challenge of extracting interpretable weight mechanisms directly from the linear layers of large language models, moving beyond proxy‑dictionary methods that label concepts after training. By applying column‑tiled SVD to the model’s weight matrices, the authors obtain a set of “mounts” that encode trigger (v), write (u) and strength (σ) triples, thereby revealing identity as a learned weight rule. Their approach is evaluated on the Gemma‑2‑2B model with WikiText‑2 data using a pre‑registered suite that measures full‑write energy lift rather than tile‑local lift, yielding quantitative scores for each linear site. The results demonstrate that several residual and attention maps achieve high performance across all site layers, while others score only partially, providing a granular view of mechanistic behavior.

## Key Contributions  
- [Finding 1] A systematic method for extracting usable weight mechanisms directly from SVD‑tiled linear sites, producing (v,u,σ) triples that represent trigger, write and strength.  
- [Finding 2] An evaluation framework based on full‑write energy lift across the entire model, which outperforms tile‑local lift metrics in capturing global impact.  
- [Finding 3] A comprehensive suite of linear maps (residual writes, attention outputs) that achieve perfect scores on all site layers for certain modules, indicating strong mechanistic utility.

## Methodology  
The authors decompose each linear weight matrix into tiled SVD components, where each tile corresponds to a “mount” defined by the column vector v (trigger), row vector u (write) and singular value σ (strength). By iterating over all tiles they construct a set of candidate mechanisms. The identity rule is inferred when the product v·u equals the original weight pattern. To assess usefulness, they run the model on WikiText‑2 subsamples, measuring how much the output energy changes when the identified write vector is activated versus baseline conditions. This full‑write lift metric evaluates whether a mechanism contributes meaningfully across the whole network rather than just locally.

## Results  
On the Gemma‑2‑2B model with a 16 384‑token WikiText‑2 subset, all seven linear maps are scored: residual writes (mlp.down, attn.o) receive full A/B/C scores and pass after post‑sublayer RMSNorm; other maps (mlp.gate/attn.q/attn.k/effective mlp.up/attn.v) achieve A/B only with 26/26 site‑layer passes. The aggregate GO score is 182/182, indicating high interpretability. Unit tests and a library codebase are released to facilitate reproducibility.

## Significance  
This work bridges mechanistic interpretability and weight engineering by providing an automated way to discover actionable mechanisms directly from model internals. By focusing on full‑write energy lift, it offers a more reliable metric for assessing whether identified rules truly drive behavior, which is crucial for debugging, alignment research, and building trustworthy AI systems.

## Related Concepts  
- SVD (Singular Value Decomposition)  
- Column‑tiled decomposition of linear layers  
- Mechanistic interpretability  
- Proxy dictionaries (sparse autoencoders, max‑activating text)  
- Energy lift metrics (full vs. tile‑local)  
- GO (Goal-Oriented) scoring for evaluation
