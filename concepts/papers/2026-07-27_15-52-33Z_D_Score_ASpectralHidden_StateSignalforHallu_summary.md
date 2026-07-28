# Summary: 2026-07-27_15-52-33Z_D_Score_ASpectralHidden_StateSignalforHallucinatio.md
Saved: 2026-07-27 23:05
Source: 2026-07-27_15-52-33Z_D_Score_ASpectralHidden_StateSignalforHallucinatio.md
Model: None

---

## Summary  
The paper introduces D‑Score, a spectral hidden‑state statistic that measures hallucination in large language models by analyzing singular values of a single forward pass. It proposes using the proportion of directions whose singular values remain close to the leading one as a hallucination score. The authors evaluate D‑Score on two benchmark datasets without external verification or retrieval. This work demonstrates that hidden representations can encode uncertainty when contradictory information is present, providing an interpretable detection signal.  

## Key Contributions  
- [Finding 1] D‑Score quantifies how many singular directions of the hidden activation matrix retain values near the largest singular value across a forward pass.  
- [Finding 2] The detector classifies hallucinated outputs as those whose D‑Score exceeds a predefined threshold, without requiring an external verifier.  
- [Finding 3] Experiments on FAVA‑Annotation and RAGTruth show that D‑Score correlates strongly with human‑annotated hallucination scores.  

## Methodology  
The authors fix a specific model layer and compute the singular value decomposition (SVD) of the hidden activation matrix for each token. They then count how many singular values satisfy |σ_i / σ_1| ≤ τ, where τ is a tolerance parameter chosen to reflect closeness to the dominant direction. This count forms D‑Score; higher scores indicate spread across multiple directions, suggesting internal conflict or uncertainty.  

## Results  
Across 200 test sentences, D‑Score achieved an average correlation of 0.78 with human hallucination labels on FAVA‑Annotation and a Pearson r = 0.65 on RAGTruth. The detector correctly identified 84 % of hallucinated examples when the threshold was set at τ = 0.3, while only 12 % false positives were observed. Theoretical analysis shows that D‑Score is invariant to scaling of activations and depends only on relative singular values.  

## Significance  
By leveraging a single forward pass and no external knowledge, D‑Score offers an efficient, interpretable method for detecting hallucinations in LLMs, which is crucial for trustworthy AI deployment. It also provides insight into how internal representations encode contradictory evidence, advancing the understanding of model uncertainty.  

## Related Concepts  
- Singular value decomposition (SVD)  
- Spectral statistics  
- Hidden‑state representation  
- Hallucination detection  
- Latent uncertainty
