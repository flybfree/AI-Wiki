# Summary: 2026-08-01_10-11-20Z_FairnessAuditing_LowerBoundsonCompanyManipulation.md
Saved: 2026-08-03 21:26
Source: 2026-08-01_10-11-20Z_FairnessAuditing_LowerBoundsonCompanyManipulation.md
Model: None

---

## Summary  
Fairness auditing is a critical concern for high‑stakes domains such as hiring and lending, where companies may attempt to evade certification by manipulating their models. The paper formalizes this scenario as a min‑max optimization problem between an adversarial company and a budget‑constrained auditor, analyzing two audit regimes: (i) a fixed‑size audit set that certifies fairness exactly, and (ii) an α‑tolerant auditor that also requires the audit to provide an approximation guarantee. By deriving explicit lower bounds on post‑audit demographic parity deviation, the authors quantify how much manipulation remains unavoidable given limited resources.

## Key Contributions  
- [Finding 1] The authors formalize fairness auditing as a min‑max optimization and derive tight theoretical lower bounds for the worst‑case demographic parity deviation under both audit regimes.  
- [Finding 2] They explicitly express these bounds as functions of the audit budget, group imbalance, and fairness tolerance, showing that manipulation persists even when resources increase.  
- [Finding 3] Empirical experiments with simple linear and neural network classifiers confirm that increasing audit budgets reduces deviation but asymptotically approaches the derived lower bounds.

## Methodology  
The company is modeled as a black‑box classifier whose decisions are subject to demographic parity constraints. The auditor selects an audit set of limited size, either aiming for exact certification or for an α‑approximation guarantee. The analysis proceeds by solving a combinatorial min‑max problem that maximizes the post‑audit deviation while respecting budget and tolerance constraints. To validate the bounds, the authors construct heuristic audit sets—random sampling and learned representations from linear and neural network models—and evaluate their performance on simulated data.

## Results  
For the fixed‑size auditor, the lower bound is Θ(√(Imbalance/Budget)), indicating that deviation shrinks with budget but never vanishes. For the α‑tolerant auditor, the bound is α + O(√(Imbalance/Budget)), showing that approximation guarantees can only be marginally improved by larger budgets. Experiments on synthetic datasets demonstrate that these theoretical limits are tight: as audit resources grow, post‑audit demographic parity deviation approaches the derived bounds.

## Significance  
These results reveal a fundamental trade‑off in fairness certification: finite budget cannot eliminate manipulation entirely, and the achievable reduction is bounded by group imbalance and tolerance. The work guides policymakers and practitioners to allocate audit resources wisely while acknowledging that perfect fairness may remain out of reach with limited data.

## Related Concepts  
- Demographic parity  
- Black‑box auditing  
- Min‑max optimization  
- Approximation guarantees (α‑tolerant)  
- Audit set construction  
- Post‑audit manipulation
