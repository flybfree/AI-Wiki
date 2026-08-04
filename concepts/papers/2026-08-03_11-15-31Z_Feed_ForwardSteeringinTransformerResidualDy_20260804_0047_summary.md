# Summary: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md
Saved: 2026-08-04 00:47
Source: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md
Model: None

---

## Summary  
The paper extends the attention‑only dynamical framework for Transformer residual directions by treating the feed‑forward network (FFN) as a local steering field that acts on each token state. It predicts that only the tangential component of this FFN field drives motion in residual‑direction space, that critical residual directions correspond to nonlinear projective equilibria, and that a commutator defect determines when a block can be approximated by an additive flow. The authors validate these predictions across GPT‑2, Pythia, Mistral, and Llama models.

## Key Contributions  
- Finding 1: The tangential component of the FFN field is necessary for motion; retaining only the radial component collapses performance.  
- Finding 2: Critical residual directions correspond to nonlinear projective equilibria, and the magnitude of a commutator defect decides whether a block can be approximated by a parallel additive flow.  
- Finding 3: Small commutator defects (< 0.05) allow near‑parallelization with only a modest loss increase, whereas large defects (> 0.1) cause rapid degradation.

## Methodology  
The authors model token states as particles on a unit sphere representing residual directions and introduce the FFN term as a vector field split into radial and tangential components acting locally on each particle. They compute the commutator of successive block operations to quantify defect magnitude. Experiments consist of one‑step angular prediction on GPT‑2, Pythia, Mistral, and Llama models, comparing the full model against an attention‑only baseline and performing ablations that retain only the tangential or radial FFN component.

## Results  
Theoretical analysis predicts a reduction in one‑step angular error from ~0.12 to ~0.08 when the FFN is included. Ablation experiments confirm that the tangential‑only model retains most of the original quality, while the radial‑only model collapses dramatically. Small commutator defects (< 0.05) permit parallelization with a loss increase below 0.3 %, whereas large defects (> 0.1) lead to losses exceeding 5 %.

## Significance  
Interpreting the FFN as a directional steering field clarifies why certain layers are amenable to block‑level interventions and hardware acceleration, providing a theoretical basis for optimizing model compression and inference efficiency.

## Related Concepts  
- Residual dynamics in Transformers  
- Attention‑only dynamical theories  
- Feed‑forward network as vector field  
- Projective equilibria  
- Commutator defect
