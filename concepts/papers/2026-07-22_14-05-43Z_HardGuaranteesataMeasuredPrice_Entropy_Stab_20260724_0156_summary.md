# Summary: 2026-07-22_14-05-43Z_HardGuaranteesataMeasuredPrice_Entropy_StableLearn.md
Saved: 2026-07-24 01:56
Source: 2026-07-22_14-05-43Z_HardGuaranteesataMeasuredPrice_Entropy_StableLearn.md
Model: None

---

## Summary  
The paper introduces a learned finite‑volume scheme for the two‑dimensional Euler equations that guarantees physical admissibility through an entropy‑stable interior flux, evaluated under fixed protocols rather than equal mesh resolution. It demonstrates that the unlearned skeleton provides the strongest guarantee on periodic domains, while learning can only improve performance in specific wall‑boundary cases where the boundary condition is unseen (≈10 % gain). The method achieves zero negativity events across 36 rollouts and delivers iso‑cost gains without sacrificing the hard guarantees. This work bridges learned solvers with rigorous stability analysis, showing that a modest overhead of 1.74× per step can yield robust performance.

## Key Contributions  
- [Finding 1] The learned finite volume scheme provides entropy‑stable interior fluxes that guarantee physical admissibility of solutions on unstructured meshes.  
- [Finding 2] At equal mesh resolution, the unlearned skeleton outperforms both learned and constrained variants in periodic cases; learning only benefits wall‑boundary problems with unseen boundary conditions (10.8 % gain).  
- [Finding 3] A spatial gate that activates learned heads near walls improves performance on both the skeleton and the corrected arm, maintaining guarantees across different geometries.

## Methodology  
The authors constructed a neural network approximating the finite‑volume discretization of the Euler equations using frozen thresholds, falsification clauses, negative controls, factor decomposition, and an iso‑cost comparison framework. They trained the network to produce flux updates that preserve entropy stability, then evaluated it under fixed protocols including Mach number extrapolation and unseen wall conditions.

## Results  
Experimental rollouts show 36/36 completions with zero negativity events; iso‑cost gains vary: periodic cases see +10 % or -12 %, the wall case shows a +10.8 % gain; the corrected arm improves on one Mach case, reduces its deficit on another, passes the unseen wall, and keeps the guarantee. A spatial gate that activates heads only near walls yields consistent improvement across two distinct wall geometries.

## Significance  
This work establishes that learned solvers can be made physically reliable with minimal overhead (1.74× per step) and offers a principled way to compare neural approximations to classical methods under computational‑cost constraints, ensuring that guarantees are not compromised by learning.

## Related Concepts  
- Finite volume discretization  
- Entropy stability  
- Learned PDE solvers  
- Iso‑cost comparison  
- Frozen thresholds  
- Falsification clauses  
- Negative controls  
- Factor decomposition  
- Mach number extrapolation  
- Spatial gating
