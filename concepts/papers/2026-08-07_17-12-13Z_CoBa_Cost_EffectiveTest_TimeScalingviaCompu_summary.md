# Summary: 2026-08-07_17-12-13Z_CoBa_Cost_EffectiveTest_TimeScalingviaCompute_Bala.md
Saved: 2026-08-09 23:11
Source: 2026-08-07_17-12-13Z_CoBa_Cost_EffectiveTest_TimeScalingviaCompute_Bala.md
Model: None

---

## Summary  
Test‑time scaling is a constrained optimization problem: under a fixed inference budget the system must decide whether to allocate compute to generation, verification, or stopping. The authors introduce CoBa, a compute‑balanced routing policy that first generates a small candidate set, applies cheap verification broadly, and then routes uncertain or high‑value candidates to stronger verification. By balancing these allocation decisions, CoBa achieves state‑of‑the‑art macro accuracy while dramatically reducing parameter‑weighted token usage compared with strong self‑evaluation weighted voting.

## Key Contributions  
- [Finding 1] CoBa reaches a macro accuracy of 85.13% on diverse reasoning benchmarks (MATH‑500, AIME 2024/2025, AMC 2023, procedural symbolic) while using only 49.1 % fewer parameter‑weighted tokens than the best strong self‑evaluation weighted‑voting proxy (85.20%).  
- [Finding 2] CoBa’s performance matches the best‑of‑16 majority voting scheme within a 0.01 macro‑accuracy point, yet it consumes 58.9 % fewer parameter‑weighted tokens, demonstrating superior cost efficiency.  
- [Finding 3] Paired tests retain a small advantage over single‑sample decoding at substantially higher computational cost, indicating that strategic pairing amplifies CoBa’s gains.

## Methodology  
The authors treat test‑time scaling as a compute‑allocation problem where each unit of compute must be assigned to one of three stages: generation, verification, or stopping. CoBa first produces a compact candidate set, then applies inexpensive verification uniformly across all candidates. Candidates that are uncertain or carry high expected value are subsequently routed to more expensive, stronger verification modules. This two‑stage routing strategy balances the trade‑off between breadth (cheap verification) and depth (strong verification), ensuring compute is spent where it yields the greatest accuracy improvement.

## Results  
On 3,129 example‑generator evaluations spanning MATH‑500, AIME 2024/2025, AMC 2023, and procedural symbolic reasoning, CoBa‑Routed‑Strong attains 85.13 % macro accuracy. This matches the self‑evaluation weighted‑voting proxy at 85.20 % while using 49.1 % fewer parameter‑weighted tokens. Moreover, it aligns with best‑of‑16 majority voting within a 0.01 macro‑accuracy point and reduces token usage by 58.9 %. Paired tests show a modest edge over single‑sample decoding, though the remaining gap to the pool oracle suggests additional headroom for refined routing.

## Significance  
CoBa provides a principled, cost‑effective framework for test‑time scaling that directly addresses the competition among generation, verification, and stopping. By minimizing parameter‑weighted token consumption without sacrificing accuracy, it enables more sustainable inference budgets—particularly valuable for local reasoning systems where compute is limited. The results demonstrate that intelligent routing can close the gap between high‑accuracy benchmarks and practical deployment constraints.

## Related Concepts  
- Test‑time scaling  
- Compute‑allocation problem  
- Compute‑balanced routing  
- Candidate selection  
- Verification (cheap vs. strong)  
- Parameter‑weighted tokens  
- Macro accuracy  
- Best‑of‑16 majority voting  
- Self‑evaluation weighted‑voting proxy  
- Headroom for sharper routing
