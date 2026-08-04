# Summary: 2026-08-03_17-28-12Z_InteractionIsNotNecessaryforOrder_Optimal1_BitMean.md
Saved: 2026-08-04 00:52
Source: 2026-08-03_17-28-12Z_InteractionIsNotNecessaryforOrder_Optimal1_BitMean.md
Model: None

---

## Summary  
The paper addresses the problem of estimating a real‑valued mean from one‑bit messages under bounded central moments, showing that an interaction between a localization stage and a refinement stage is unnecessary to achieve order‑optimal sample complexity. By constructing a fully non‑adaptive protocol that fixes all queries in advance, the authors match the optimal adaptive complexity for target accuracy ε and confidence 1–δ. Their analysis yields a minimax rate that aligns with known lower bounds across three regimes of the central moment exponent k. This work provides a negative answer to an open COLT 2026 problem concerning interaction necessity in one‑bit mean estimation.

## Key Contributions  
- [Finding 1] A fully non‑adaptive protocol achieving order‑optimal sample complexity for one‑bit mean estimation with general queries.  
- [Finding 2] Exact minimax rate formulas: log(λ/σ) plus a term depending on k, ε, and δ across the regimes k>2, k=2, and 1<k<2.  
- [Finding 3] Demonstration that interaction between localization and refinement stages is not required to meet optimal complexity.

## Methodology  
The authors consider distributions with mean in [-λ, λ] and absolute k‑th central moment ≤σᵏ (k>1 fixed). They first review the standard two‑stage adaptive protocol: a localizing phase that decodes the mean within an interval of size O(ε) and a refining phase that uses subsequent queries to narrow down the estimate. To eliminate interaction, they design a randomized fully non‑adaptive scheme where all query vectors are predetermined before any data is observed. The analysis proceeds via information‑theoretic arguments, comparing the expected number of bits needed under both adaptive and non‑adaptive settings and showing equivalence up to constant factors that depend only on k.

## Results  
For target accuracy ε and confidence 1–δ, the sample complexity scales as  
\[
\log\frac{λ}{σ} + 
\begin{cases}
(σ/ε)^2 \log(1/δ), & k>2,\\
(σ/ε)^2 \log(σ/ε)\log(1/δ), & k=2,\\
(σ/ε)^{k/(k-1)} \log(1/δ), & 1<k<2,
\end{cases}
\]  
up to constants independent of ε, δ, λ, and σ. This rate matches the known lower bound for general queries, confirming minimax optimality even among fully adaptive protocols.

## Significance  
By proving that interaction can be omitted without sacrificing optimality, the paper resolves a longstanding open problem in COLT theory and demonstrates that non‑interactive communication strategies are sufficient for one‑bit mean estimation. The result broadens the applicability of non‑adaptive protocols to other statistical inference problems where adaptivity is traditionally assumed necessary.

## Related Concepts  
- One‑bit message complexity  
- Order‑optimal sample complexity  
- Localization and refinement stages in adaptive protocols  
- Minimax rate analysis for bounded moment distributions  
- Fully non‑adaptive communication protocols
