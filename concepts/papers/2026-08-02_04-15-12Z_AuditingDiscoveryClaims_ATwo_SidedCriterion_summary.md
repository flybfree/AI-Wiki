# Summary: 2026-08-02_04-15-12Z_AuditingDiscoveryClaims_ATwo_SidedCriterionforAgen.md
Saved: 2026-08-03 20:37
Source: 2026-08-02_04-15-12Z_AuditingDiscoveryClaims_ATwo_SidedCriterionforAgen.md
Model: None

---

## Summary  
The paper proposes a two‑sided audit framework for self‑improving AI‑for‑science systems that can objectively verify whether reported capability gains are genuine or artifacts of oracle manipulation, search bias, or verifier changes. It introduces a formal negative criterion based on a provably bounded range of a pseudoknot‑free oracle, making the “negative side” decidable before any run. The audit compares a single fallible oracle’s performance against its own prior self and an external judge, exposing inflation without relying on statistical noise. Finally, it demonstrates that agent‑written procedures can outperform human ones with far fewer oracle calls, challenging assumptions about compute efficiency.

## Key Contributions
- [Finding 1] A solver‑free operator solves 43/60 crossing RNA targets under the predictor it optimizes, exceeding a context‑free floor of 0/60; when paired on the same targets, a predictor never seen confirms two designs against 26 for a minimum‑free‑energy solver (p = 8e‑7), showing that an oracle can inflate capability claims beyond its own prior knowledge.  
- [Finding 2] Among six frontier models, two whose operators ran without timeouts outperformed our baseline at 0.293 versus 0.095 (n = 951 paired units) with a p‑value of 5e‑5 while using only 4.6–10× fewer oracle calls, proving that agentic procedures can beat human ones under an objective judge.  
- [Finding 3] The audit’s ceiling is the panel itself: three predictors share nearest‑neighbour thermodynamic parameters with κ = 0.673, indicating that the maximum achievable difference is limited by shared assumptions rather than compute or oracle capacity.

## Methodology  
The authors construct a two‑sided audit where the negative side is a formal fact: a pseudoknot‑free oracle cannot represent a crossing base pair, so its range is bounded offline before any run. They evaluate how far a single fallible oracle can inflate a capability claim by comparing a solver‑free operator’s performance on 43/60 crossing RNA targets to the context‑free floor of 0/60 and to predictions from an unseen predictor. They also perform paired experiments between agent‑written procedures and human‑written ones under an external adjudicator, measuring differences in success rates while tracking oracle call counts.

## Results  
The solver‑free operator achieves 43 correct predictions on 60 crossing targets (72 % success), far above the context‑free floor of 0/60. The unseen predictor confirms two designs against 26 for a minimum‑free‑energy solver with p = 8e‑7, indicating genuine improvement beyond prior knowledge. Paired model comparisons show a mean difference of +0.108 (p = 5e‑5) between the two top models and our baseline, while using only 4.6–10× fewer oracle calls. The panel’s κ value of 0.673 caps the achievable separation.

## Significance  
This audit provides a decidable negative criterion that prevents self‑improving AI systems from overstating gains by exploiting oracles or search bias, offering a rigorous baseline for evaluating capability claims. It also reveals that observed improvements can stem from shared assumptions among predictors rather than compute efficiency, guiding more honest benchmarking practices.

## Related Concepts  
pseudoknot‑free oracle, crossing base pair, context‑free floor, minimum‑free‑energy solver, κ (Cohen’s kappa), benchmark delta, p‑value, oracle calls, self‑improving AI‑for‑science, two‑sided audit.
