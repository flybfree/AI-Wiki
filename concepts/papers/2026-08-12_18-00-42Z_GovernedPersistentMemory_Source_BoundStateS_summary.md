**Original paper:** [https://arxiv.org/abs/2608.12476v1](https://arxiv.org/abs/2608.12476v1)

# Summary: 2026-08-12_18-00-42Z_GovernedPersistentMemory_Source_BoundStateSemantic.md
Saved: 2026-08-13 22:25
Source: 2026-08-12_18-00-42Z_GovernedPersistentMemory_Source_BoundStateSemantic.md
Model: None

---

## Summary  
Governed Persistent Memory (GPM) is introduced as an auditable bitemporal state‑transition model designed to solve the long‑horizon agent memory problem of select‑store‑retrieve, where retrieval must respect source‑bound semantics and fail‑closed release. The paper defines five executable clauses that guarantee ledger integrity, source binding, conflict isolation, non‑revival after retraction or deletion, and exact claim closure at a verified head. Experiments on the GPM‑ReleaseBench show perfect matching of outcomes for complete policies and 100 % correctness in a sealed end‑to‑end service evaluation, while a finite model explores millions of semantic states with zero mismatches.

## Key Contributions  
- Introduce Governed Persistent Memory (GPM) as an auditable bitemporal state‑transition model with source‑bound admission, derived lifecycle states, public barriers, and fail‑closed structured release.  
- Demonstrate that GPM matches all 3,600 outcomes on the GPM‑ReleaseBench benchmark; a simple policy achieves 1,800/3,600 correct results and makes unmatched releases on 50 % of violation cases, while baseline Qwen2.5‑7B scores 600/2,400 with regression.  
- Provide rigorous finite model exploration covering 331,776 semantic states and 1,990,656 query states, producing zero mismatches across a 100,000‑trace differential.

## Methodology  
The authors modeled agent memory as a contract between ingestion (source‑bound state admission) and release phases. Each transition is recorded with lifecycle metadata, public barriers enforce ordering, and any violation triggers fail‑closed release—no data is released if the contract is broken. Five executable clauses implement ledger integrity, source binding, conflict isolation, non‑revival after retraction/deletion, and exact claim closure at a fresh view anchored to one verified head.

## Results  
GPM matches all 3,600 complete outcomes on GPM‑ReleaseBench; the strongest simple policy reaches 1,800/3,600 correct results and fails on 50 % of violation cases. A sealed end‑to‑end service evaluation yields deterministic outputs with 2,400/2,400 correct clusters per arm versus 600/2,400 for ungoverned Qwen2.5‑7B. The finite model explores 331,776 semantic and 1,990,656 query states without counterexamples. A 100,000‑trace differential yields zero mismatches.

## Significance  
This bounded contract ensures reliable long‑horizon agent memory by preventing stale or contradictory claims, providing provable correctness and auditability. It outperforms ungoverned models such as Qwen2.5‑7B, repairs all baseline failures without regression, and offers a foundation for trustworthy AI systems where memory integrity is critical.

## Related Concepts  
bitemporal state transition model; source‑bound admission; lifecycle states; public barriers; fail‑closed release; ledger integrity; conflict isolation; exact claim closure; GPM‑ReleaseBench benchmark; sealed end‑to‑end service evaluation; finite model verification; differential trace analysis.
