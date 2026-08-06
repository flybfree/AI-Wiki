# Summary: 2026-08-05_17-26-47Z_MALT_LightweightCurvature_AwareMuonviaDiagonalPrec.md
Saved: 2026-08-05 22:33
Source: 2026-08-05_17-26-47Z_MALT_LightweightCurvature_AwareMuonviaDiagonalPrec.md
Model: None

---

## Summary  
Muon is a lightweight alternative to AdamW that orthogonalizes momentum matrices using Newton‑Schulz iterations to reduce gradient anisotropy. The paper shows that Muon remains vulnerable to the hidden curvature of the loss landscape, which can degrade training stability. MALT solves this by introducing lightweight diagonal preconditioners that capture local curvature geometry without increasing memory or compute cost. By applying two‑sided preconditioning and norm‑grafted updates, MALT achieves orthogonal momentum while preserving the original update magnitude. The authors further extend the framework with MALTER to adapt step sizes in stochastic settings.

## Key Contributions  
- [Finding 1] MALT introduces diagonal two‑sided preconditioners that approximate curvature geometry, reducing Muon’s sensitivity to anisotropy.  
- [Finding 2] The method uses norm‑grafted updates and Newton‑Schulz iterations to orthogonalize the preconditioned momentum while controlling update magnitude.  
- [Finding 3] MALTER adds adaptive step rescaling for stochastic gradient noise, providing convergence guarantees in non‑convex settings.

## Methodology  
The authors propose a lightweight diagonal preconditioner that is computed once per layer and stored as a sparse matrix, enabling O(1) memory overhead. This preconditioner is applied to the raw gradients on both forward and backward passes (two‑sided), producing an approximate curvature map. The preprocessed gradient is then orthogonalized using Newton‑Schulz iterations, which converge in a fixed number of steps independent of problem size. A norm‑grafting step rescales the orthogonal vector so that its magnitude matches the original gradient’s L2 norm, ensuring consistent learning rates. The resulting update direction replaces Muon’s momentum, and MALTER further adapts the step size based on variance estimates to improve robustness.

## Results  
Experiments on GPT‑2 Small, Medium, and Large pretraining demonstrate that MALT achieves higher perplexity than Muon while keeping memory usage and wall‑clock time within 5 % of baseline AdamW. The adaptive version MALTER further reduces training instability under stochastic gradients, with convergence rates comparable to the best Adam variants. All methods require only a single diagonal matrix per layer, preserving the lightweight nature of Muon.

## Significance  
By explicitly modeling curvature geometry through cheap diagonal preconditioners, MALT mitigates a long‑standing weakness of momentum‑based optimizers in non‑convex landscapes. The approach offers theoretical convergence guarantees for stochastic non‑convex optimization and improves practical training stability without sacrificing efficiency. This work bridges theory and practice, providing a scalable solution to curvature‑anisotropy issues that affect many large‑scale language models.

## Related Concepts  
- Muon (Muon momentum orthogonalization)  
- AdamW (Adam with weight decay)  
- Newton‑Schulz iteration (gradient orthogonalization)  
- Diagonal preconditioning (low‑memory matrix approximation)  
- Curvature geometry of loss landscapes  
- Stochastic non‑convex optimization and convergence guarantees
