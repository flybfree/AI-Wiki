# Summary: 2026-07-28_18-52-47Z_MoreData_WorseDecisions_PreferenceReversalsinNeura.md
Saved: 2026-07-30 23:05
Source: 2026-07-28_18-52-47Z_MoreData_WorseDecisions_PreferenceReversalsinNeura.md
Model: None

---

## Summary  
The paper investigates whether neural networks that pool data from multiple sources preserve consistent preference orderings, a requirement formalized by CBDT composition axiom. It shows that refitting on pooled data can reverse shared preferences due to recomputed inverse‑Gram geometry. The authors derive exact and approximate conditions for preservation and propose solutions.

## Key Contributions  
- [Finding 1] The paper proves that pooled OLS refitting recomputes the inverse‑Gram geometry, which can cause preference reversals when source evidence is incompatible.  
- [Finding 2] It introduces a scale‑invariant Gram mismatch measure to prioritize candidate pools and a geometry‑oriented regularization term to shape source geometry during training.  
- [Finding 3] A three‑stage audit framework traces strict pairwise reversals through decision changes, linking them to task‑defined utility loss.

## Methodology  
The authors formalize the reliability requirement using CBDT’s composition axiom. They analyze fixed‑representation neural networks with OLS output heads by examining how source evidence is weighted via inverse‑Gram geometry. To identify problematic pools, they compute a Gram mismatch metric that scales invariantly across domains. During training, they add a regularization term that encourages the network to maintain compatible geometries between sources. The audit pipeline consists of (1) identifying pairwise preference reversals, (2) mapping those to decision changes in each proxy task, and (3) aggregating them into a utility‑based loss.

## Results  
Theoretical analysis yields exact preservation conditions: source preferences survive union iff the Gram matrices remain congruent under pooling. Approximate conditions are derived via eigenvalue bounds. Experiments on load‑based bidding, medical diagnosis, and financial trading data show that comparable Gram mismatches lead to vastly different reversal rates across domains. Geometry‑oriented training reduces reversals by up to 40% while maintaining accuracy. The audit pipeline quantifies harmful decisions relative to utility loss.

## Significance  
This work makes compositional reliability measurable: it provides analytic certification, a geometric regularization strategy, and an auditing protocol that can be applied before deployment. It bridges theory (CBDT) with practical model training, offering tools to prevent hidden preference reversals in high‑stakes decision systems.

## Related Concepts  
- CBDT composition axiom  
- Gram matrix geometry  
- Inverse‑Gram weighting of evidence  
- Scale‑invariant mismatch measure  
- Geometry‑oriented regularization  
- Decision‑consequence auditing
