# Summary: 2026-07-26_17-55-40Z_ScaleWeightDecayandTrainBetter.md
Saved: 2026-07-27 23:59
Source: 2026-07-26_17-55-40Z_ScaleWeightDecayandTrainBetter.md
Model: None

---

## Summary  
The paper investigates the effect of scaling weight decay during deep‑learning training and shows that a simple, theoretically grounded modification—multiplying the weight‑decay term by the fraction of the peak learning rate \(η/η_{\max}\)—preserves the asymptotic optimality guarantees of unregularized methods while eliminating the steady shrinkage bias introduced by constant decoupled decay. By applying this “scaled weight decay” (SW) to the non‑Euclidean optimizer Muon, the authors demonstrate that training mixture‑of‑experts models reaches comparable validation loss 30 % faster across a wide range of model sizes and token budgets. The work therefore offers a lightweight, code‑free way to accelerate pre‑training without sacrificing stability.

## Key Contributions  
- [Finding 1] Scaled weight decay defined as \(λ_{SW}=λ·(η/η_{\max})\) maintains the same asymptotic stationarity properties of unregularized SGD and Muon, removing the extra bias caused by constant decoupled decay.  
- [Finding 2] A steady‑state analysis explains why constant decay forces a monotonic decrease in the weight norm, whereas SW yields a roughly constant norm that stabilizes training dynamics.  
- [Finding 3] Empirically, Muon‑SW consistently outperforms Muon with identical hyperparameters on mixture‑of‑experts models from 72 M to 930 M parameters trained at ~600 tokens per active parameter, achieving a 30 % faster convergence.

## Methodology  
The authors start from the Robbins–Monro conditions that characterize optimal learning rates for SGD and Muon. They derive a weight‑decay schedule proportional to the current learning rate relative to its maximum value, ensuring that the regularization term scales with the optimizer’s activity level. Theoretical proofs are provided showing that this schedule preserves asymptotic stationarity guarantees while avoiding the bias of constant decay. The proposed schedule is then implemented in Muon and evaluated on a suite of mixture‑of‑experts models across varying parameter counts and token budgets.

## Results  
Across all experiments, Muon trained with scaled weight decay achieved validation loss reductions 30 % faster than Muon using the same hyperparameters. The improvement is observed from small (72 M) to very large (930 M) models, each trained at roughly 600 tokens per active parameter. Theoretical analysis confirms that the norm of the weight vector stabilizes under SW, eliminating the systematic shrinkage that constant decay induces.

## Significance  
By decoupling weight‑decay from the learning‑rate schedule, the method enables faster convergence without compromising stability—a critical issue for large‑scale pre‑training where time is scarce. The approach requires only a few lines of code to implement and can be adopted across any optimizer that supports custom regularization terms.

## Related Concepts  
- Weight decay (L2 regularization)  
- Stochastic gradient descent (SGD)  
- Non‑Euclidean optimizers such as Muon  
- Robbins–Monro conditions  
- Asymptotic stationarity guarantees
