# Summary: 2026-08-05_09-14-22Z_OnMUONoptimization_Fromnon_convergencetoanerrorana.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_09-14-22Z_OnMUONoptimization_Fromnon_convergencetoanerrorana.md
Model: None

---

## Summary  
The paper investigates the failure of the MUON optimizer to converge in stochastic optimization problems despite many gradient steps and proposes a generalized version that allows an arbitrary number of Newton‑Schulz polynomial steps. It shows that, for almost every mini‑batch size, the error does not vanish as the number of iterations tends to infinity. The authors also introduce Polar Express as a special case of this generalized scheme and perform a detailed error analysis that quantifies convergence in terms of both iteration count and batch size. These findings aim to clarify why MUON is ineffective for large‑scale AI training and to guide the design of more robust accelerated optimizers.

## Key Contributions  
- **Finding 1:** MUON does not converge for almost all mini‑batch sizes as the number of gradient steps converges to infinity, indicating a fundamental instability in its convergence properties.  
- **Finding 2:** The authors derive an explicit error bound for the generalized MUON optimizer that depends on both the polynomial degree and the batch size, providing a theoretical framework for predicting performance.  
- **Finding 3:** Polar Express is identified as a special case of the generalized MUON with specific polynomial degrees, demonstrating how recent methods can be embedded within this broader analysis.

## Methodology  
The authors treat stochastic optimization problems (SOPs) as the testbed for their analysis. They first formulate the error dynamics of the generalized MUON algorithm using matrix‑polynomial approximations and then derive convergence rates analytically. To validate these predictions, they implement the optimizer in Python and run experiments on several concrete SOPs: quadratic stochastic optimization problems and ℓ₂‑regularized logistic regression for binary classification. The implementation includes both the original five‑step NS version of MUON and the Polar Express variant.

## Results  
Theoretical analysis shows that error decays at least as O(1/√n) when the batch size is fixed, but the rate can be slower if the mini‑batch is too large. Experiments confirm that the generalized MUON converges more slowly than plain SGD for small batches yet faster than standard SGD for larger batches, while Polar Express yields modest improvements over both. The results illustrate a trade‑off between polynomial degree and convergence speed.

## Significance  
This work uncovers a critical flaw in MUON’s application to real‑world AI training, where non‑convergence can lead to poor model performance or divergence. By offering a principled error analysis and highlighting Polar Express as a viable alternative, the authors provide a roadmap for designing accelerated optimizers that respect stochasticity constraints.

## Related Concepts  
- Stochastic gradient descent (SGD)  
- Momentum optimizer (MUON)  
- Newton‑Schulz polynomial  
- Polar Express method  
- Quadratic stochastic optimization problems (SOPs)  
- ℓ₂ regularization in logistic regression  
- Mini‑batch size effects on convergence  
- Error analysis for accelerated optimizers
