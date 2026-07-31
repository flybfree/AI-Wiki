# Summary: 2026-07-30_14-52-36Z_OneHuman__N_Agents_Audit_BudgetAllocationforLLMAge.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-52-36Z_OneHuman__N_Agents_Audit_BudgetAllocationforLLMAge.md
Model: None

---

## Summary  
The paper addresses the problem of auditing a fleet of N large language model agents under a limited budget B ≪ N, where each agent reports a confidence score that is adversarially miscalibrated and correlated across agents. It shows that when confidence‑ranked inspection is used beyond a certain threshold δ*, the strategy can become worse than random sampling. The authors derive this threshold analytically under a two‑level Gaussian copula model and provide empirical evidence from five open‑weight LLMs and one proprietary model. Their work also introduces a quantitative criterion for vacuous oversight.

## Key Contributions  
- Finding 1: Derivation of the miscalibration threshold δ* beyond which confidence‑ranked auditing is inferior to random sampling.  
- Finding 2: Empirical observation that δ* rises as the budget B shrinks and that cross‑family correlation is high, with shared difficulty dominating lineage.  
- Finding 3: Introduction of a quantitative criterion for vacuous oversight and validation via replaying policies on recorded traces.

## Methodology  
The authors model the auditing problem as a budgeted noisy inspection over a two‑level Gaussian copula, where each agent’s confidence is assumed to follow a Gaussian distribution with unknown mean shift δ. They assume adversarial miscalibration up to threshold δ* and correlated errors via the copula structure. The analysis proceeds by comparing expected audit cost under random versus confidence‑ranked strategies, deriving conditions for when the latter dominates. Experiments are conducted on five open‑weight LLMs (GPT‑2, LLaMA‑13B, etc.) and a proprietary model, recording confidence scores per round to validate the theoretical ordering.

## Results  
Theoretical analysis predicts that δ* increases as B decreases and that correlation is high, leading to vacuous oversight. Empirically, five open models produce near‑constant confidence at or beyond δ*, while the proprietary model remains below it, confirming the predicted ranking. Replaying policies on recorded traces reproduces the same ordering, supporting the criterion for vacuous oversight.

## Significance  
This work clarifies when relying on self‑reported confidence can degrade audit quality, especially in large AI fleets where budgets are tight and errors are correlated. It provides a decision rule to avoid vacuous oversight and highlights that shared difficulty often outweighs individual model differences.

## Related Concepts  
- Two‑level Gaussian copula  
- Auditing with budget constraints  
- Miscalibrated confidence  
- Adversarial calibration  
- Cross‑family correlation  
- Vacuous oversight  
- AI audit budgets
