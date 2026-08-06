# Summary: 2026-08-05_09-16-29Z_TheOrderIstheGuarantee_Verifier_BudgetedCodeDeleti.md
Saved: 2026-08-05 20:32
Source: 2026-08-05_09-16-29Z_TheOrderIstheGuarantee_Verifier_BudgetedCodeDeleti.md
Model: None

---

## Summary  
The paper tackles the inverse problem of removing redundant code when a verification system has limited execution‑capacity, arguing that the order in which deletion candidates are tested matters more than model confidence. It proposes a proposal‑scheduling framework where a ranker orders single‑statement deletion candidates and an execution suite accepts the first candidate that passes, bounded by a fixed budget. The core contribution is an auditable division of labor: models generate proposals, ordering limits the damage of mis‑ranked suggestions, and execution decides which deletions are actually applied. This approach improves verified‑deletion coverage while keeping verifier calls manageable.

## Key Contributions  
- [Finding 1] Candidate order is the control surface a deployment can reason about; scheduling determines both what code is removed and how much verification effort is spent.  
- [Finding 2] A five‑slot budget that first tests deterministic shortest‑first candidates and then appends learned proposals raises verified‑deletion coverage by 9.5% (≈ 6.7 additional tasks accepted) while using slightly fewer verifier calls than a static baseline.  
- [Finding 3] Without explicit validation the same rankers can lose coverage under shift; enforcing a deterministic prefix first guarantees non‑decreasing coverage and character reduction, increasing verifier calls by up to 62.5%.

## Methodology  
The authors model redundant‑code reduction as proposal scheduling: a ranker ranks single‑statement deletion candidates, an execution suite evaluates them sequentially until one passes, and a budget caps the number of tests. They instantiate two schedules—one mixing deterministic and learned proposals, another that always runs static candidates first. Representative target‑domain validation is used to compare performance across nine MBPP replications with rankers of 0.5B, 0.6B, and 8B parameters.

## Results  
Across the nine replications, the mixed schedule improves verified‑deletion coverage by 9.5% relative to a static baseline (≈ 6.7 more tasks accepted) while consuming marginally fewer verifier calls. The deterministic‑prefix‑first schedule ensures that coverage and character reduction never decrease; it raises verifier call volume between 4.8% and 62.5%. However, the in‑domain advantage of MBPP+ disappears when only the test suite is considered, confirming that scheduling governs search while the suite alone defines “preserving behavior”.

## Significance  
This work provides a practical method for maintaining software as code accumulates, turning verification capacity into an explicit budget rather than an implicit resource. By separating model‑generated proposals from execution‑controlled ordering, it offers an auditable pipeline that balances efficiency with safety, enabling AI systems to delete obsolete logic without compromising correctness.

## Related Concepts  
- Redundant‑code reduction  
- Proposal scheduling  
- Ranker ordering  
- Deterministic shortest‑first candidates  
- Learned proposals  
- Verifier‑budgeted deletion  
- Static prefix first  
- MBPP+ (Machine Benchmark Programming Platform)  
- Shift invariance  
- Verification capacity  
- Maintainable software
