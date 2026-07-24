# Summary: 2026-07-22_02-46-57Z_Data_PoisoningAuditsforCausalEffectEstimation.md
Saved: 2026-07-24 01:31
Source: 2026-07-22_02-46-57Z_Data_PoisoningAuditsforCausalEffectEstimation.md
Model: None

---

## Summary  
The paper introduces a data‑poisoning audit for augmented inverse‑probability‑weighted (AIPW) causal effect estimation, addressing the risk that adversaries can insert plausible records to bias treatment estimates when records are pooled across sites or vendors. By treating each record as a potential “append” and defining a finite catalog of feasible records with an append budget, the authors develop a greedy scan that computes the exact worst‑case movement of the AIPW estimate at every possible budget level. The framework also provides a total‑influence score that captures both direct and indirect contributions of each record to the estimated effect, yielding a conservative bound for fully refitted analyses. Extensive simulations confirm the exactness of the movement curves and demonstrate material sensitivity in small budgets, while real‑world multisite and public‑data studies illustrate practical vulnerability.

## Key Contributions  
- [Finding 1] A greedy algorithm that computes the exact finite‑sample worst‑case movement of an AIPW estimate for any append budget.  
- [Finding 2] A total‑influence score that combines direct record contribution with indirect effects through propensity and outcome models, enabling precise local refit prediction.  
- [Finding 3] A conservative finite‑budget bound on the fully refitted estimate that accounts for nuisance refitting.

## Methodology  
The authors model an append‑only attack where a malicious actor selects a feasible subset of records from a catalog, respecting nested source capacities and a specified budget. They fix preprocessing steps and nuisance fits, then apply a greedy scan that iteratively adds the most damaging record to maximize movement in a direction chosen by the analyst. The total‑influence score is derived analytically, weighting each record’s direct impact plus its influence via the propensity and outcome models. Finally, they bound the maximum possible shift of the fully refitted AIPW estimate under any budget using the total‑influence metric.

## Results  
Simulations validate that the greedy scan yields exact worst‑case movement curves across all budgets, confirming theoretical predictions. The total‑influence score improves local refit prediction accuracy compared with standard influence measures. In multisite and public‑data analyses, small append budgets (e.g., ≤5 records) produce substantial shifts in treatment effects, highlighting practical sensitivity. The conservative bound shows that even modest budget increases can materially alter the final estimate when total influence is high.

## Significance  
By translating adversarial data‑composition risk into quantifiable movement curves and critical budgets, this framework equips causal analysts with a rigorous audit tool to detect and mitigate poisoning attacks. It supports more reliable reporting of treatment effects across heterogeneous data sources and informs the design of source‑level safeguards that limit the impact of malicious record insertions.

## Related Concepts  
- AIPW (augmented inverse‑probability‑weighted) estimation  
- Append‑only attacks on observational data  
- Total influence in causal inference  
- Greedy optimization for worst‑case scenarios  
- Conservative finite‑budget bounds
