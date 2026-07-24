# Summary: 2026-07-21_19-43-54Z_RELTA_SGLD_Relative_GrowthLocalizedTamingforNoncon.md
Saved: 2026-07-24 01:14
Source: 2026-07-21_19-43-54Z_RELTA_SGLD_Relative_GrowthLocalizedTamingforNoncon.md
Model: None

---

## Summary  
The paper addresses the challenge of stabilizing superlinear stochastic‑gradient updates in nonconvex SGLD when the gradient oracle grows superlinearly. It proposes RELTA‑SGLD, a relative‑growth localized tamer that activates only after a threshold and whose strength follows a one‑step Lyapunov stability condition. The scheme uses a lighter λ denominator to preserve far‑tail return of the original dynamics. As a result, polynomial moment stability and first‑order stationary accuracy are achieved in both W1 and W2.  

## Key Contributions  
- Finding 1: RELTA‑SGLD guarantees polynomial moment stability and first‑order stationary accuracy for nonconvex SGLD with superlinearly growing stochastic gradients in both L1 and L2 norms.  
- Finding 2: The method improves the half‑order and quarter‑order convergence bounds compared to other comparable tamed schemes.  
- Finding 3: Experiments on Fashion‑MNIST under active stabilization pressure show RELTA‑SGLD outperforms untamed SGLD and TUSLA, while remaining competitive with a tuned AdamW baseline.  

## Methodology  
The authors derived a threshold that determines when the taming takes effect and formulated a relative‑growth principle based on the one‑step Lyapunov stability condition to compute the required tamer strength. This yields a localized denominator λ that is lighter than uniform tamer scales, minimizing unnecessary perturbation of the original update. They validated the theory through analytical proofs and empirical evaluation under active stabilization pressure.  

## Results  
Theoretical analysis shows polynomial moment stability and first‑order stationarity in both W1 and W2 for RELTA‑SGLD with superlinear stochastic gradients. Experimental results on Fashion‑MNIST demonstrate that RELTA improves mean learning metrics relative to untamed SGLD, TUSLA, and a tuned AdamW reference. The lighter denominator reduces unnecessary perturbation, preserving near‑untamed dynamics in ordinary training regimes.  

## Significance  
This work matters because it enables stable training of deep nonconvex models under superlinear gradient growth without excessive damping, thereby preserving the original learning drift. By providing tighter theoretical guarantees (polynomial moments, first‑order accuracy) and better practical performance than prior tamer approaches, RELTA‑SGLD advances both theory and practice in stochastic‑gradient Langevin optimization.  

## Related Concepts  
stochastic gradient Langebin dynamics (SGLD), tamer, Lyapunov stability condition, relative growth principle, threshold‑based taming, localized denominator λ, half‑order/quarter‑order convergence bounds, AdamW.
