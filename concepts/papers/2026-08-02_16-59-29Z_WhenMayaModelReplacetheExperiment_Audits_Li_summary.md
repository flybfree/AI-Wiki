# Summary: 2026-08-02_16-59-29Z_WhenMayaModelReplacetheExperiment_Audits_Licenses_.md
Saved: 2026-08-04 00:17
Source: 2026-08-02_16-59-29Z_WhenMayaModelReplacetheExperiment_Audits_Licenses_.md
Model: None

---

## Summary  
The paper investigates when machine‑learning surrogates can replace costly experiments in design campaigns, establishing safety criteria and cost implications. It proves that trust cannot be based solely on predictive accuracy, introduces a quantifiable “selection tax,” and derives minimal conditions for surrogate oracles that preserve rank order. The work provides theoretical bounds, optimal audit strategies, and empirical validation across multiple tasks.

## Key Contributions  
- [Finding 1] Predictive accuracy does not guarantee safe design selections; near‑perfect R² can still lead to worst‑case outcomes.  
- [Finding 2] Trust must be purchased via selection‑aware audits that are optimal in query complexity, and certifying without true experiments opens a deterministic self‑confirmation failure mode.  
- [Finding 3] Audited surrogates reduce certified oracle cost by roughly a factor of 25 while maintaining high Spearman rank correlation (0.80–0.99).

## Methodology  
The authors conduct mathematical analysis on three exhaustively ground‑truthed design tasks, deriving upper and lower bounds for the selection tax, establishing an architectural rule that certifications require true evaluations, and performing exhaustive surrogate fitting across six task‑regime conditions.

## Results  
Across 432 surrogate fits, audit statistics show Spearman rank correlation of deployed search performance between 0.80–0.99; R² correlates with regret at as low as 0.33. Audited screening cuts certified evaluation cost by a factor of 25 while preserving high rank preservation.

## Significance  
This work clarifies when surrogate‑driven design can be trusted, introduces rigorous audit protocols, and quantifies the trade‑off between computational savings and safety, influencing future AI‑assisted experimental planning.

## Related Concepts  
Surrogate models, oracle functions, selection tax, Spearman rank correlation, self‑confirmation failure mode, query complexity, certified evaluation cost.
