# Summary: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md
Saved: 2026-08-04 00:31
Source: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md
Model: None

---

## Summary  
The authors extend the attention‑only dynamical model of Transformer residual directions by treating the feed‑forward network (FFN) as a local steering field that acts on each token state. Their theory predicts which component of this FFN field—tangential versus radial—drives motion in the residual‑direction space and how commutator defects between attention and FFN determine whether a block can be approximated by a parallel additive flow. By analyzing several large language models, they show that retaining only the tangential FFN component preserves model quality, while keeping only the radial component collapses performance. The work thus bridges dynamical systems theory with practical model‑level interventions.

## Key Contributions  
- Extend the attention‑only dynamical framework to include an FFN steering field and predict its effect on residual‑direction motion.  
- Show that tangential FFN components are necessary for motion, while radial components do not contribute, and that critical directions correspond to nonlinear projective equilibria.  
- Demonstrate that commutator defects (the mismatch between attention and FFN) decide whether a block can be approximated by a parallel additive flow; small defects incur modest loss increase, large defects cause rapid degradation.

## Methodology  
The authors model token states as particles aggregating on a unit sphere representing residual directions. The FFN is interpreted as a vector field that produces both tangential and radial components at each point. They compute the commutator between attention and FFN to quantify defect size, then perform ablation experiments across GPT‑2, Pythia, Mistral, and Llama models. By comparing predictions of angular motion with and without the FFN component, they assess how different model architectures behave under intervention.

## Results  
The extended theory improves one‑step angular prediction relative to an attention‑only baseline, with the FFN contribution growing from GPT‑2 to Llama‑3‑8B. Ablation shows that keeping only the tangential FFN retains most quality and diversity; retaining only the radial component collapses performance. Small commutator defects allow approximate parallelization with a modest loss increase, whereas large defects cause rapid degradation.

## Significance  
These findings explain FFN layers as directional steering fields that shape the geometry of Transformer residual dynamics, providing a theoretical basis for block‑level interventions and guiding more efficient training strategies. By linking model architecture to dynamical behavior, the work offers new insights into optimization landscapes and potential shortcuts in large language models.

## Related Concepts  
- Attention‑only dynamical theory  
- Spherical particle aggregation on a unit sphere  
- Feed‑forward network steering field (tangential/radial components)  
- Nonlinear projective equilibria in residual directions  
- Commutator defect between attention and FFN  
- Parallel additive flow approximation for block parallelization
