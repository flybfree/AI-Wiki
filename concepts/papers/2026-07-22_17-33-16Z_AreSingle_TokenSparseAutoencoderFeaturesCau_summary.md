# Summary: 2026-07-22_17-33-16Z_AreSingle_TokenSparseAutoencoderFeaturesCausallyNe.md
Saved: 2026-07-24 02:09
Source: 2026-07-22_17-33-16Z_AreSingle_TokenSparseAutoencoderFeaturesCausallyNe.md
Model: None

---

## Summary  
This paper investigates whether single‑token sparse autoencoder (SAE) features play a causal role that is stable across different SAE families and model architectures. By zero‑ablating these features at full layer depth in six large language models, the authors test how their activation patterns affect downstream token ranking and logit scores. The study reveals that early‑layer features are especially dense in decoder space, that cross‑family causal effects outpace within‑family scale differences, and that the same feature can be interpreted differently depending on training recipe rather than merely its activation function or scale.

## Key Contributions  
- [Finding 1] Single‑token SAE features cluster 4.7× tighter in decoder space and concentrate primarily in early layers (Layer 0 for GPT2‑Small, L0–L4 for Gemma), and zero‑ablating them yields Benjamini‑Hochberg‑significant logit reductions in 178 of 208 full‑layer conditions.  
- [Finding 2] Cross‑family causal differences exceed within‑family scale effects: GemmaScope and BatchTopK features retain their causal anchoring, whereas LlamaScope features become locally redundant under the same training setup.  
- [Finding 3] After ablating a feature, the target token’s rank recovers to 96–98 % of the baseline value; moreover, comparing activation functions within the same model reverses sign, indicating that training recipe—not just activation or scale—remains the primary driver.

## Methodology  
The authors performed zero‑ablation experiments at full layer depth across six language models and three SAE families (GemmaScope, BatchTopK, LlamaScope). They generated 3.9 million features, measured logit reductions under each ablation condition, and applied Benjamini‑Hochberg significance testing to identify robust effects. Depth was controlled by keeping all layers active while removing only the targeted SAE feature, allowing them to observe whether damage cascades downstream or directly shapes output.

## Results  
The analysis shows that single‑token features are tightly clustered in decoder space and dominate early layers, suggesting a hierarchical organization of interpretability signals. Ablation experiments reveal 178 significant logit reductions across the full layer set, confirming functional impact. Cross‑family comparisons demonstrate that GemmaScope and BatchTopK features maintain causal relevance, while LlamaScope features lose their unique contribution under identical training conditions. The target token’s rank recovers to within two standard deviations of baseline after ablation (96–98 % recovery). A controlled comparison of activation functions reverses sign within the same model, indicating that training recipe is the residual explanation for observed differences.

## Significance  
These findings challenge the assumption that SAE interpretability is stable across families and highlight that causal roles are sensitive to experimental design rather than merely to activation function or scale. By quantifying how early‑layer features dominate and how ablation cascades, the work provides a rigorous framework for evaluating feature importance in large language models.

## Related Concepts  
- Sparse autoencoder (SAE) features  
- Causal role of features  
- Decoder space clustering  
- Layer depth effects  
- SAE families: GemmaScope, BatchTopK, LlamaScope  
- Zero‑ablation experiments  
- Benjamini‑Hochberg significance testing  
- Activation function comparisons  
- Training recipe influence on interpretability
