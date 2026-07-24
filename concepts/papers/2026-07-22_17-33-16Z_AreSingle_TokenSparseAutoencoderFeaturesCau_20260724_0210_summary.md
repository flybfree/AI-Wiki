# Summary: 2026-07-22_17-33-16Z_AreSingle_TokenSparseAutoencoderFeaturesCausallyNe.md
Saved: 2026-07-24 02:10
Source: 2026-07-22_17-33-16Z_AreSingle_TokenSparseAutoencoderFeaturesCausallyNe.md
Model: None

---

## Summary  
The paper investigates whether single‑token sparse autoencoder (SAE) features are causally necessary across SAE families and layer depths in large language models. It performs zero‑ablation experiments on 3.9 million features from six models to determine how removing these features affects logits, token activation ranks, and downstream predictions.

## Key Contributions  
- Single‑token SAE features cluster tightly in the decoder space and concentrate early (Layer 0 for GPT2‑Small; L0–L4 for Gemma), indicating a layer‑specific causal role.  
- Ablating them yields Benjamini‑Hochberg‑significant logit reductions in 178 of 208 full‑layer conditions, with depth controlling whether damage cascades downstream or shapes the output directly.  
- Cross‑family interpretability differences exceed within‑family scale effects: GemmaScope and BatchTopK features remain causally anchored while LlamaScope features become locally redundant.

## Methodology  
The authors use zero‑ablation at full layer depth across six models (GPT2‑Small, Gemma, Llama) to examine the impact of removing single‑token sparse autoencoder features. They evaluate logit reductions via Benjamini‑Hochberg significance testing and track token rank recovery after ablation. A controlled activation‑function comparison within each model isolates training‑recipe effects from feature importance.

## Results  
- Single‑token features are 4.7× tighter in decoder space than multi‑token ones, concentrating early (L0 for GPT2‑Small; L0–L4 for Gemma).  
- Ablation produces BH‑significant logit reductions in 178/208 conditions; depth determines whether downstream effects propagate or the output is directly altered.  
- After ablation, target token rank recovers to within 2× baseline 96–98% of the original.  
- Controlled activation‑function comparison reverses sign within the same model, leaving training recipe as the residual candidate.

## Significance  
This work clarifies that causal interpretability claims about SAE features are not universal but depend on training methodology and layer depth. It highlights early‑layer features have stronger causal impact and that cross‑family differences reflect methodological variance rather than activation function alone.

## Related Concepts  
- Sparse autoencoder (SAE) features  
- Single‑token features  
- Causal role of features in LLMs  
- Layer‑depth effects on feature importance  
- Benjamini‑Hochberg significance testing  
- Decoder space clustering
