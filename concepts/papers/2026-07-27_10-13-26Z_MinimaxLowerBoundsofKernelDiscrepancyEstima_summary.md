# Summary: 2026-07-27_10-13-26Z_MinimaxLowerBoundsofKernelDiscrepancyEstimation_MM.md
Saved: 2026-07-27 21:35
Source: 2026-07-27_10-13-26Z_MinimaxLowerBoundsofKernelDiscrepancyEstimation_MM.md
Model: None

---

## Summary  
The paper investigates the minimax lower bounds for estimating three widely used kernel discrepancy measures—maximum mean discrepancy (MMD), Hilbert‑Schmidt independence criterion (HSIC) and kernel Stein discrepancy (KSD)—on arbitrary topological spaces. It shows that, under mild assumptions on the kernel, the optimal estimation rate is \(n^{-1/2}\), matching the parametric convergence speed of fast estimators. By proving these lower bounds as corollaries for the mean embedding and centered cross‑covariance operator, the authors settle longstanding questions about the optimality of these discrepancy metrics beyond finite‑dimensional Euclidean settings.

## Key Contributions  
- **Finding 1:** The minimax lower bound of \(n^{-1/2}\) is established for MMD, HSIC, and KSD estimation on any topological space with bounded kernels or mild regularity.  
- **Finding 2:** The same \(n^{-1/2}\) rate holds as corollaries for the mean embedding and centered cross‑covariance operator, confirming optimality across related estimators.  
- **Finding 3:** The results generalize beyond strict finite‑dimensional assumptions to broader topological contexts while preserving the parametric lower bound.

## Methodology  
The authors employ information‑theoretic techniques, specifically entropy concentration inequalities and data processing arguments, to derive minimax lower bounds. They start from known upper bounds achieved by fast estimators that converge at \(n^{-1/2}\) under parametric conditions, then use these as a baseline for constructing lower bounds via adversarial distributions. The proof framework works simultaneously in both parametric (bounded kernel) and non‑parametric regimes, leveraging the universality of the discrepancy measures.

## Results  
The main theoretical result is that the minimax rate for estimating MMD, HSIC, and KSD is \(n^{-1/2}\) on any topological space provided the kernel satisfies mild conditions (e.g., boundedness or sub‑exponential tails). Consequently, the mean embedding and centered cross‑covariance operator also enjoy this optimal rate as corollaries. These findings demonstrate that the parametric convergence speed cannot be improved beyond \(n^{-1/2}\) in general settings.

## Significance  
Establishing these minimax lower bounds clarifies the limits of fast kernel discrepancy estimators, confirming that their \(n^{-1/2}\) convergence is indeed optimal when only mild assumptions are imposed. This result prevents over‑optimistic expectations about faster rates and guides future research toward more informative approximations or alternative metrics.

## Related Concepts  
- Kernel discrepancy measures (MMD, HSIC, KSD)  
- Mean embedding and centered cross‑covariance operator  
- Minimax estimation theory  
- Parametric versus non‑parametric convergence rates  
- Topological spaces and kernel regularity assumptions  
- Information‑theoretic lower bounds via entropy concentration
