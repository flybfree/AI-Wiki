# Summary: 2026-07-28_12-04-46Z_QuotientDynamics_EffectiveCurvature_andImplicitBia.md
Saved: 2026-07-28 22:47
Source: 2026-07-28_12-04-46Z_QuotientDynamics_EffectiveCurvature_andImplicitBia.md
Model: None

---

## Summary  
The paper investigates how the quotient structure of positive quadratic networks governs training dynamics, curvature, recovery, and interpolation bias for low‑rank PSD matrices. By exploiting the fact that the Euclidean factor gradient is horizontal on the rank‑r manifold, it shows that factor gradient flow projects exactly to a Riemannian gradient flow on the quotient space. The authors also derive an effective Hessian at interpolators via the empirical Gram form restricted to the tangent space and resolve nonuniqueness through weighted entropy in the invariant joint spectral algebra.

## Semantic links
- [[concepts/papers/2026-08-02_22-37-34Z_Gram_Space_Structure_PreservingCodebookComp_summary.md|Summary: 2026-08-02_22-37-34Z_Gram_Space_Structure_PreservingCodebookCompression.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.03
- [[concepts/papers/2026-07-21_17-17-35Z_RiemannianDeepLearning_Modules_Networks_and_summary.md|Summary: 2026-07-21_17-17-35Z_RiemannianDeepLearning_Modules_Networks_andGeometr.md]] — 3 title terms overlap; 11 summary/topic terms overlap; semantic match 0.11

## Key Contributions  
- **Exact congruence recursion**: Finite‑step gradient descent predictor satisfies a precise recurrence that mirrors the continuous‑time flow on the PSD manifold.  
- **Population curvature bounds**: Under Gaussian rank‑one measurements, uniform deviation bounds are proved for the empirical normal operator, yielding explicit curvature estimates.  
- **Interpolation bias resolution**: Predictors converge to the minimum‑trace solution set as ε→0, using weighted entropy within the joint spectral algebra to break nonuniqueness.

## Methodology  
The authors analyze the quotient Riemannian geometry of the rank‑r PSD manifold \( \mathbb{R}^{d\times r}_*/O(r) \). They compute the Euclidean factor gradient for a smooth objective \( L(U)=ell(UU^\top) \), observe that it is horizontal, and project it onto the quotient metric. This yields an exact congruence recursion for finite‑step descent. Curvature is obtained by restricting the empirical Gram form to the tangent space at interpolators. A spectral initializer is constructed, and convergence rates are proved: exponential for gradient flow and linear for small‑step descent. Underdetermined commuting regimes are treated as entropy mirror flows, while strict positivity ensures Bregman projections.

## Results  
Theoretical proofs provide uniform deviation bounds on the empirical normal operator under Gaussian measurements, establishing population curvature. Local exponential convergence of gradient flow and linear convergence of finite‑step descent are established. Recovery guarantees are explicit but conservative due to reliance on full‑space second‑moment control. Numerical experiments verify the congruence recursion, curvature predictions, recovery behavior, and selection laws; predictors approach Bregman projections with an error \(O(\eta)\).

## Significance  
This work provides a rigorous bridge between quotient dynamics and effective geometry for low‑rank PSD matrices, delivering precise training analysis that goes beyond standard factorization methods. It resolves interpolation bias via entropy‑based selection, offers convergence guarantees unattainable in conventional settings, and clarifies the role of curvature in recovery.

## Related Concepts  
Quotient Riemannian geometry, PSD manifold \( \mathbb{R}^{d\times r}_*/O(r) \), congruence recursion, effective Hessian, Gram form restricted to tangent space, Bregman projection, weighted entropy, joint spectral algebra, entropy mirror flow.
