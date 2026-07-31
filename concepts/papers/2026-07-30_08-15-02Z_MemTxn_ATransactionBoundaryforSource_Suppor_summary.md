# Summary: 2026-07-30_08-15-02Z_MemTxn_ATransactionBoundaryforSource_SupportedUpda.md
Saved: 2026-07-30 20:31
Source: 2026-07-30_08-15-02Z_MemTxn_ATransactionBoundaryforSource_SupportedUpda.md
Model: None

---

## Summary  
The paper introduces MemTxn, a transaction‑boundary layer that sits outside the answer model to guarantee reliable updates and complete‑state recovery in persistent agent memory. By verifying that each write is supported by its source, selecting the appropriate version when facts conflict, and restoring the full active map after faults, MemTxn eliminates silent corruption that plagues current storage solutions. The system’s governance approach combines ordered patch testing, temporal resolution, and a durable snapshot journal to achieve both correctness and efficiency.

## Key Contributions  
- **MemTxn introduces a transactional governance layer** that enforces source‑supported updates and provides complete‑state recovery without exposing the answer model to memory corruption.  
- **It selects the visible version when facts conflict** using a Temporal Resolver combined with Ordered PatchTest, ensuring deterministic and consistent state selection.  
- **The system recovers the declared active map after persistent multi‑key faults** via a durable snapshot journal, even though it does not know the exact physical write set.

## Methodology  
MemTxn is implemented as an external module that intercepts writes to agent memory. First, Ordered PatchTest validates that each patch conforms to the source’s logical constraints. Next, the Temporal Resolver queries a version store to determine which snapshot is visible under current conditions and resolves any conflicts by choosing the most recent compatible version. Finally, all changes are logged in a durable snapshot journal; on fault detection or recovery initiation, the journal is replayed to reconstruct the complete active map, allowing the agent to resume with a clean state.

## Results  
During an item‑disjoint audit MemTxn correctly accepted 60 supported original updates and rejected 179 hard negatives. On LongMemEval‑S and LoCoMo states it restored the entire declared active map without knowledge of the actual write set. In MemoryAgentBench FactConsolidation, MemTxn achieved the highest average F1 score across all twelve answer‑model configurations, outperforming Dense by 17.06–24.07 points in five representative settings.

## Significance  
Persistent memory is essential for long‑running language agents, yet current solutions allow write errors to persist and corrupt future behavior. MemTxn’s transactional boundary eliminates this risk, providing a reliable mechanism for both source‑supported updates and full recovery, which directly improves factual consistency, reduces debugging overhead, and enhances overall system robustness.

## Related Concepts  
- Persistent memory  
- Transactional governance  
- Version selection (Temporal Resolver)  
- Ordered patch testing  
- Snapshot journaling  
- Agent memory  
- LongMemEval‑S, LoCoMo  
- MemoryAgentBench FactConsolidation
