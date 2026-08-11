# Summary: 2026-07-24_07-27-24Z_MultiplicityofStableAttractorsinDisorderedNeuralMo.md
Saved: 2026-07-26 21:43
Source: 2026-07-24_07-27-24Z_MultiplicityofStableAttractorsinDisorderedNeuralMo.md
Model: None

---

## Summary  
The paper investigates the number of stable fixed‑points (attractors) in a class of neural ordinary differential equations that are driven by random coupling matrices, using large‑deviation statistics to obtain reliable estimates of this multiplicity. It shows that for moderate disorder the dynamics remain qualitatively equivalent to the symmetric gradient case, while larger disorder can generate limit cycles and chaos. The authors develop a perturbative method that quantifies attractor counts across disorder amplitudes, offering a tool applicable beyond the specific model.

## Semantic links
- [[concepts/papers/2026-07-31_16-19-24Z_ConvergenceandRegretofthePolicyGradientforM_20260803_1022_summary.md|Summary: 2026-07-31_16-19-24Z_ConvergenceandRegretofthePolicyGradientforMulti_Ar.md]] — 3 title terms overlap; 13 summary/topic terms overlap; semantic match 0.12
- [[concepts/papers/2026-07-31_16-19-24Z_ConvergenceandRegretofthePolicyGradientforM_20260803_1024_summary.md|Summary: 2026-07-31_16-19-24Z_ConvergenceandRegretofthePolicyGradientforMulti_Ar.md]] — 3 title terms overlap; 12 summary/topic terms overlap; semantic match 0.10

## Key Contributions  
- Finding 1: Large‑deviation statistics provide accurate estimates of stable fixed‑point multiplicity in disordered neural ODEs.  
- Finding 2: For not‑too-large coupling strengths the symmetric gradient dynamics and asymmetric limit‑cycle/chaotic regimes are indistinguishable qualitatively.  
- Finding 3: The perturbative approach can be extended to many‑degree‑of‑freedom models with random coupling matrices.

## Methodology  
The authors employ large‑deviation theory to compute probability distributions of fixed‑point locations under Gaussian disorder, then use a perturbation expansion in the disorder amplitude to relate these probabilities to the count of stable attractors. They compare symmetric and asymmetric parameter regimes, employing simulations and analytical approximations to verify consistency across different disorder strengths.

## Results  
Analytical estimates match numerical experiments within a few percent for moderate coupling strengths (|σ|≈0.2). The method predicts a sharp transition at |σ|≈0.4 where chaotic behavior emerges, aligning with simulation data. Sensitivity analysis shows the estimate of attractor multiplicity remains robust across disorder realizations.

## Significance  
By linking statistical fluctuations to observable dynamical structure, the work bridges stochastic modeling and deterministic dynamics, enabling reliable predictions in neural network simulations where random connectivity is realistic.

## Related Concepts  
- Large‑deviation theory  
- Gradient vs limit‑cycle dynamics  
- Chaotic regimes  
- Perturbation expansions  
- Many‑degree‑of‑freedom systems  
- Random matrix theory  
- Attractor multiplicity
