# Summary: 2026-08-06_19-23-32Z_LostinInterpolation_WhyPredictiveFeedbackFailsinDi.md
Saved: 2026-08-09 22:24
Source: 2026-08-06_19-23-32Z_LostinInterpolation_WhyPredictiveFeedbackFailsinDi.md
Model: None

---

## Summary  
The paper investigates why linear interpolation (LERP) fails as a feedback mechanism in Masked Diffusion Language Models, revealing that the embedding space is hyperspherical rather than Euclidean. It proposes Spherical Soft‑Masking (S‑SM), which uses spherical linear interpolation (SLERP) and a Fr’echet mean to blend predictions with the mask direction while preserving native norm. The method improves convergence and generation quality without affecting output entropy or training dynamics.

## Key Contributions  
- Finding 1: Embedding space of MDLMs exhibits a near‑constant angle (~73°) between mask and predicted‑token embeddings, indicating hyperspherical geometry.  
- Finding 2: Norms remain essentially flat across vocabulary‑frequency rank, supporting the hyperspherical model.  
- Finding 3: S‑SM using spherical interpolation outperforms LERP in generation perplexity (16.9–19.6% lower) and delivers MAUVE gains up to 2× over vanilla MDLM.

## Methodology  
The authors analyze training embeddings by computing cosine similarity and norm plots, confirming the constant angle and flat norms that imply a hyperspherical geometry. They replace linear interpolation with spherical linear interpolation (SLERP), which preserves angular relationships on the unit sphere, and compute the Fr’echet mean of the top‑k predictions to blend them into a single direction before applying SLERP.

## Results  
Experiments show S‑SM yields MAUVE improvements ranging from 2× over vanilla MDLM to 56.1% over TopK/LERP across various inference step budgets. Generative perplexity drops by 16.9–19.6% relative to the baseline, while output entropy and training convergence remain unchanged.

## Significance  
This work resolves a fundamental flaw in diffusion language model training: using Euclidean interpolation on a hyperspherical embedding space degrades performance. By adopting spherical interpolation, S‑SM provides a more faithful representation of embeddings, leading to faster convergence and better generation quality without trade‑offs in entropy or speed.

## Related Concepts  
- Masked Diffusion Language Models (MDLMs)  
- Linear Interpolation (LERP) vs Spherical Linear Interpolation (SLERP)  
- Fr’echet mean on the hypersphere  
- Hyperbolic geometry of embedding spaces
