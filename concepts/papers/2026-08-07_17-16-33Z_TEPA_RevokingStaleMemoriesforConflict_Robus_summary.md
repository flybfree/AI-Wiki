# Summary: 2026-08-07_17-16-33Z_TEPA_RevokingStaleMemoriesforConflict_RobustLangua.md
Saved: 2026-08-09 23:11
Source: 2026-08-07_17-16-33Z_TEPA_RevokingStaleMemoriesforConflict_RobustLangua.md
Model: None

---

## Summary  
The paper identifies a critical failure mode in long‑term memory called *memory pollution*: stale, contradictory facts persist and corrupt retrieval when the world changes. To address this, TEPA proposes a revocable evidence‑memory mechanism that makes validity an explicit state of each observation. The authors show that by actively revoking conflicting memories under the same key, agents can retrieve only current, valid information while retaining an audit trail for later re‑promotion. Experiments across synthetic drift regimes and real file‑backed executable updates demonstrate a dramatic reduction in false recall compared with traditional append‑only or last‑write‑wins strategies.

## Key Contributions  
- [Finding 1] Memory pollution is formally characterized as the degradation caused by active memories that newer, conflicting evidence has superseded.  
- [Finding 2] TEPA introduces a revocable evidence‑memory mechanism where each observation is stored as a keyed precedent with an explicit validity state, and conflicts trigger immediate revocation.  
- [Finding 3] Empirically, TEPA achieves near‑perfect recall (0.95) on drift benchmarks, whereas append‑only or last‑write‑wins fall below 0.21, showing that current‑key replacement is decisive for single‑hop fact consolidation.

## Methodology  
The authors model memory as a collection of *active precedents* keyed by observation identifiers. When fresh evidence arrives with the same key and contradicts an active precedent, TEPA revokes the stale entry while preserving it in a separate audit log. Retrieval queries only draw from predicates whose validity flag is true. The system was evaluated on three streams: hidden‑regime drift (50 random seeds), real file‑backed executable drift, and preference‑update streams, using the MemoryAgentBench suite for both single‑hop SH‑6k and multi‑hop/long‑context tests.

## Results  
Over 50 seeds, TEPA’s recall score was 0.95, while append‑only and last‑write‑wins were 0.210 each and a “no memory” baseline was 0.309. In real file execution the pattern held: TEPA 0.950 vs. 0.203 (append‑only) and 0.298 (last‑write‑wins). On MemoryAgentBench SH‑6k, TEPA matched a strong last‑write‑wins cache, confirming that current‑key replacement is the key operation for fact consolidation. Boundary tests revealed retrieval‑chain and context‑selection bottlenecks in very long contexts, indicating that validity tracking alone does not solve all multi‑hop challenges.

## Significance  
TEPA establishes lifecycle revocation as a core memory operation for agents that must falsify outdated knowledge, maintain auditability, and later re‑promote evolving information. By treating memory validity as an explicit state, the framework enables robust, self‑correcting language agents capable of adapting to real‑world changes without accumulating harmful stale facts.

## Related Concepts  
Memory pollution, active precedents, revocation, validity state, retrieval chain, context selection, last‑write‑wins, append‑only memory.
