# Summary: 2026-07-14_02-08-33Z_SaturationMakesQuantizationErrorAdditive_ACoverage.md
Saved: 2026-07-23 23:42
Source: 2026-07-14_02-08-33Z_SaturationMakesQuantizationErrorAdditive_ACoverage.md
Model: None

---

## Summary  
The paper investigates how mixed‑precision quantization affects model loss and shows that, under saturation conditions, the error becomes additive. By treating the change in loss $f(S)$ from quantizing a layer set $S$ as a set function on the Boolean cube, the authors analyze it via two classical changes of basis (per‑layer and pairwise effects). They propose a coverage model with a certificate that reproduces measured variance profiles and yields an optimal additive predictor. The results demonstrate that per‑layer effects dominate variance, monotone transforms preserve ranking up to 2 % error, and memory allocations based on this model outperform gradient‑sensitivity methods across models from 30B to 355B parameters.

## Semantic links
- [[concepts/papers/2026-07-30_13-58-33Z_SecurityofWorld_Model_BasedEmbodiedAI_ALife_summary.md|Summary: 2026-07-30_13-58-33Z_SecurityofWorld_Model_BasedEmbodiedAI_ALifecycleof.md]] — 4 title terms overlap; 10 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 7 summary/topic terms overlap; semantic match 0.03

## Key Contributions  
- [Finding 1] Across configurations drawn from the deployment distribution, 85–93 % of the variance of $f$ is explained by per‑layer effects alone.  
- [Finding 2] A monotone transform of a sum of per‑layer terms reproduces $f$’s ranking of configurations, misordering at most 2 % of pairs.  
- [Finding 3] The coverage model $f(S)=c\bigl(1-\prod_{i\in S}(1-a_i)\bigr)$ reproduces the measured variance profile to within a few percent from its $L$ fitted break‑rates and serves as the second predictor with $L+1$ parameters.

## Methodology  
The authors view the loss change $f(S)$ as a set function on the Boolean cube of layer sets. They perform two changes of basis: one isolates per‑layer contributions, the other examines pairwise interactions. By fitting a parametric model to match observed variance across full lattices, they estimate the unexplained variance and report it as a certificate. This framework enables comparison of allocators that respect matched memory constraints.

## Results  
- 85–93 % of loss‑variance is accounted for by per‑layer effects.  
- The monotone transform misorders ≤2 % of configuration pairs.  
- The coverage model’s variance profile matches the fitted break‑rates within a few percent.  
- The additive model is optimal as a first‑order predictor; its mean‑squared error equals the unexplained variance, which is measured on full lattices and estimated out‑of‑sample at network scale.  
- Among allocators constrained by memory, the coverage model yields the lowest KL divergence for models ranging from 30B to 355B parameters; allocations below four bits continue to solve code and reasoning tasks where gradient sensitivities no longer terminate.

## Significance  
This work provides a theoretical foundation that quantization error becomes additive under saturation, enabling reliable allocation strategies. By delivering an optimal additive predictor and a certificate of its performance, the model improves task outcomes when gradient‑based sensitivity methods fail, especially in low‑bit regimes.

## Related Concepts  
- Mixed‑precision quantization  
- Sensitivity‑based methods (HAWQ, CoopQ)  
- Boolean cube analysis  
- Set functions on layer sets  
- Monotone transforms and ranking preservation  
- Parseval’s identity for variance decomposition  
- KL divergence in memory allocation  
- Code‑and‑reasoning tasks under low‑bit constraints
