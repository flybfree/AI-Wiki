# Summary: 2026-08-10_10-22-10Z_FromObjectivestoWhatModelsLearn_ALandauTheoryofInv.md
Saved: 2026-08-11 00:01
Source: 2026-08-10_10-22-10Z_FromObjectivestoWhatModelsLearn_ALandauTheoryofInv.md
Model: None

---

## Summary  
The paper tackles the persistent “objective‑behavior gap” in invariant learning by treating representation learning as a form of magnetization and deriving a Landau‑type effective free energy from concrete regularization objectives. It shows that low‑order coefficients of this free energy act as objective signatures that dictate how models behave as regularization is increased. The framework predicts phase boundaries, finite‑strength mode elimination, and non‑monotone tails through quadratic and quartic corrections. By linking these theoretical signatures to empirical observations in ReLU networks, the authors close a long‑standing interpretability challenge in deep learning.

## Key Contributions  
- [Finding 1] The effective free energy’s low‑order coefficients encode objective signatures that uniquely determine regularization phenotypes such as mode elimination or amplitude regulation.  
- [Finding 2] Quadratic corrections shift phase boundaries and enable finite‑strength mode removal, while quartic terms control post‑onset amplitudes without leaving residual loading at zero strength.  
- [Finding 3] Controlled experiments on one‑ and two‑layer ReLU networks confirm the predicted phase boundaries, steady‑state loadings, and selective‑retention windows across different depths.

## Methodology  
The authors model representation learning as a multimode magnetization problem, where each mode corresponds to a latent variable. By constructing an effective free energy that includes quadratic and quartic terms, they analyze how regularization strength moves the system through distinct phases. The analysis yields closed‑form expressions for phase boundaries and steady‑state loadings, which are then compared with experimental results obtained on benchmark networks.

## Results  
Theoretically, the framework predicts sharp phase transitions where certain modes vanish at specific regularization strengths, leaving others with finite loading. Experiments show that these predictions hold across shallow and deep ReLU architectures: the same low‑order signatures reliably indicate whether a mode is eliminated or retained. A matrix extension further generalizes the results to coupled collective modes, providing a spectral criterion for phase boundaries.

## Significance  
This work bridges theory and practice by turning abstract regularization objectives into concrete, interpretable predictions about what models learn as training becomes more constrained. It offers a principled way to design regularizers that preserve useful representations while eliminating spurious ones, thereby improving generalization and model efficiency.

## Related Concepts  
invariant learning, Landau theory, magnetization analogy, regularization path, quadratic/quartic corrections, phase boundaries, mode elimination, selective‑retention window, spectral phase boundary.
