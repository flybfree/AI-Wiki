# Summary: 2026-07-25_23-29-23Z_WhenCanDepthReplacePrecision_AResourceTheoryofQuan.md
Saved: 2026-07-27 23:51
Source: 2026-07-25_23-29-23Z_WhenCanDepthReplacePrecision_AResourceTheoryofQuan.md
Model: None

---

## Summary  
The paper asks when additional low‑bit residual computation can substitute for missing numerical precision in a fixed input‑output map, deriving a resource theory that bounds how depth improves accuracy. It models quantized neural computation as selecting operations from a library over a horizon and uses relaxed controls to compute an infinite‑depth limit, showing the distance to this reachable set is a structural floor preventing deeper improvements. The analysis distinguishes execution semantics (write‑back vs increment feedback) and routing models, revealing precise trade‑offs between depth and precision.  

## Key Contributions  
- [Finding 1] A resource‑theoretic bound on how depth D replaces precision D for a given low‑bit operation library, with asymptotic rates O(D⁻¹) under bounded‑variation time dependence.  
- [Finding 2] Execution semantics affect the bound; full‑state write‑back incurs a Dρ_z penalty freezing residual updates, while increment error feedback yields a bounded carry term and obeys an exact common‑lattice conservation law.  
- [Finding 3] A fixed‑teacher converse shows that for high‑precision comparators, achieving accuracy requires D = Θ(L), making the depth‑replacement claim sharp.  

## Methodology  
The authors formulate the problem as a pure schedule selecting fields from a declared low‑bit operation library over a fixed horizon. They treat residual updates as relaxed control variables and compute the reachable set in infinite depth, analyzing time dependence via bounded‑variation or Holder spaces to derive asymptotic error rates. Concrete execution models (write‑back vs increment feedback) and routing strategies are then compared to these theoretical limits.  

## Results  
Theoretical results include an exact structural floor distance, O(D⁻¹) and O(D^{-θ}+D^{-1}) bounds for Holder dependence exponent θ, a converse proving D = Θ(L) for coherent depth‑L first‑order high‑precision comparators, and the effect of learned codebooks as metadata resources. Verified primal and dual bounds are provided; companion software implements the workflow, and Lean 4 machine‑checks the discrete core.  

## Significance  
The work bridges resource theory with quantized neural computation, offering precise conditions when depth can replace precision for specific libraries, horizons, execution semantics, and routing models. This informs hardware design, algorithmic trade‑offs, and theoretical understanding of residual networks under low‑bit constraints.  

## Related Concepts  
- Resource theory  
- Quantized residual networks  
- Relaxed control  
- Infinite‑depth limit  
- Execution semantics (write‑back vs increment feedback)  
- Common‑lattice conservation law  
- Fixed‑teacher converse  
- Learned codebooks (metadata resource)  
- State‑dependent routing (hybrid event conditions)  
- Bounded‑variation/Holder spaces  
- Structured floor  
- Depth‑precision trade‑off
