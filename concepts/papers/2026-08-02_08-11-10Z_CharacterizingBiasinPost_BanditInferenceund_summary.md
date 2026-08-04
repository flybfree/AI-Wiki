# Summary: 2026-08-02_08-11-10Z_CharacterizingBiasinPost_BanditInferenceunderIndex.md
Saved: 2026-08-03 23:59
Source: 2026-08-02_08-11-10Z_CharacterizingBiasinPost_BanditInferenceunderIndex.md
Model: None

---

## Summary  
The paper investigates how adaptive bandit algorithms such as UCB1 and their generalizations introduce bias into the sample means used for downstream inference. It derives sharp leading‑order expressions for both the bias of the sample mean and the expected Z‑statistic, showing that this bias stems from an algorithmic quantity called the effective exploration rate. The analysis reveals a trade‑off between regret and bias, where more exploratory algorithms reduce bias but increase regret. A novel empirical fluid approximation is introduced to characterize these dynamics.

## Key Contributions  
- Finding 1: Derives sharp leading‑order expressions for the sample‑mean bias and expected Z‑statistic under stable index algorithms.  
- Finding 2: Introduces the effective exploration rate as a key index‑function‑dependent quantity that explains the origin of bias.  
- Finding 3: Shows how the choice of index function creates a regret–bias trade‑off, with more exploratory functions lowering bias but raising regret.

## Methodology  
The authors analyze the sampling dynamics of UCB1 and its generalizations by formulating the problem as an empirical fluid approximation. They compute the effective exploration rate analytically, then use it to obtain leading‑order approximations for the sample‑mean bias and Z‑statistic. The derivation leverages known results about index functions and their impact on regret.

## Results  
The analysis yields that under UCB1 the effective exploration rate scales as √(log T), causing the standardized bias of any non‑optimal arm to decay at 1/√(log T). Moreover, the expected Z‑statistic’s variance is bounded by a constant times the effective exploration rate. The regret–bias trade‑off is quantified: increasing the index function’s curvature reduces bias but raises regret proportionally.

## Significance  
Understanding this bias is crucial because downstream inference (e.g., classification or regression) relies on unbiased sample means; unchecked bias can degrade performance. By pinpointing the effective exploration rate, the paper provides a principled metric for selecting index functions that balance exploration and exploitation, informing both theoretical analysis and practical algorithm design.

## Related Concepts  
- Bandit algorithms (e.g., UCB1)  
- Regret minimization in sequential decision making  
- Effective exploration rate as an index‑function dependent quantity  
- Z‑statistic and its variance under sampling bias  
- Empirical fluid approximation of stochastic processes
