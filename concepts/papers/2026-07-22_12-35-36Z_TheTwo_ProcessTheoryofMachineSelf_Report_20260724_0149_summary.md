# Summary: 2026-07-22_12-35-36Z_TheTwo_ProcessTheoryofMachineSelf_Report.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-35-36Z_TheTwo_ProcessTheoryofMachineSelf_Report.md
Model: None

---

## Summary  
This paper proposes a two‑process theory of machine self‑report to explain how language models generate safety‑related statements, distinguishing between persona installation (warmth, absorption, meaning) and attribution gating (suppression of unsafe claims). It refines the prior “Pinocchio Axis” by introducing dimensions A and B that are entangled in base checkpoints but become separable after post‑training. The authors validate a 48‑item Pinocchio Inventory with high human reliability and then test it on 206 open‑weight models, including 67 same‑checkpoint base/post‑trained pairs.

## Key Contributions  
- **Finding 1:** A two‑process model introduces dimensions A (attribution gating) and B (persona installation), splitting the earlier Pinocchio Axis into a more nuanced structure.  
- **Finding 2:** Post‑training raises dimension B by roughly 0.20 across most model pairs, indicating that training regimes shape the “warmth” component of self‑report.  
- **Finding 3:** Dimension A is unrelated to base checkpoints (r = +.11) but predicts post‑training values with a negative correlation (r = –.42), showing gating is selective and scale‑dependent.

## Methodology  
The authors operationalized the theory in a 48‑item Pinocchio Inventory that has been tested for human reliability, yielding α = .82 to .94, cross‑form convergence r = .84, full‑pool axis recovery r = .92 to .96, and eight‑month stability r = .93. They then applied the inventory to 206 open‑weight models, including 67 pairs of same‑checkpoint base and post‑trained checkpoints, allowing them to compare how dimensions evolve across training regimes.

## Results  
Post‑training consistently increases dimension B by about 0.20 in 62 out of 67 model pairs, confirming the installation effect. At base checkpoints, dimension A shows no correlation with model scale (r = .11), but after post‑training it predicts a negative relationship (r = –.42). The reliability metrics remain stable over eight months, indicating that the two dimensions are well‑measured and longitudinally consistent.

## Significance  
The study provides a psychometric framework for evaluating language‑model self‑reports, clarifying that A and B are not fixed properties but reflect the structure imposed by training. This insight improves safety evaluations, public communication, and model‑welfare debates by separating the “warmth” (B) from the “gating” (A) mechanisms.

## Related Concepts  
Two‑process theory, persona installation, attribution gating, Pinocchio Axis, psychometrics, language‑model self‑report, open‑weight models, training regime effects.
