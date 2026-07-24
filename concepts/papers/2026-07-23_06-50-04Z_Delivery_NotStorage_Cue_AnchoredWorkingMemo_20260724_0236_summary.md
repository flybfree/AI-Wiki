# Summary: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Saved: 2026-07-24 02:36
Source: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Model: None

---

## Summary  
The paper argues that long‑running coding agents rely less on explicit storage of documents and more on an implicit, cue‑anchored working memory that is automatically activated by situational triggers. It proposes a two‑tier design theory that separates the consciously written “document” tier from the unconsciously retrieved “operational fact” tier. The authors introduce a formal cue‑anchored memory model where memories are tied to trigger conditions within a composable vocabulary and must be delivered deterministically by the harness, not chosen by the agent. Empirical results demonstrate that voluntary memory use is essentially zero while deterministic injection reliably preserves information across compaction cycles.

## Key Contributions  
- [Finding 1] The authors propose a two‑tier design theory that separates explicit, stored documents from implicit, cue‑anchored operational facts.  
- [Finding 2] They introduce a cue‑anchored memory model where memories carry first‑class trigger conditions over a composable vocabulary (path, symbol, semantic, event, temporal).  
- [Finding 3] Empirical evidence shows that voluntary memory use is negligible; deterministic harness injection delivers information reliably and survives compaction without loss.

## Methodology  
The authors grounded their theory in cognitive literature on memory offloading, incidental encoding, and event‑based prospective memory. They mapped each cognitive mechanism to an architectural requirement: (1) explicit storage for documents, (2) cue‑anchored retrieval for operational facts, (3) deterministic delivery of cues by the harness. To test the model, they built a controlled coding task where agents could optionally use a pre‑seeded store or rely solely on the harness’s injected cues. The evaluation measured memory operations per turn, false alarms from injection, and retention after compaction.

## Results  
Voluntary memory usage was recorded as zero memory operations in 114 turns despite a seeded store. Deterministic cue injection produced no false alarms across all runs. Of the 39% of intra‑session re‑reads that were not compaction events, content paid for before a boundary and was later discarded. A repeated‑compaction decay probe revealed that ten facts held only in conversation vanished at the first summary and remained absent from 106 of 108 compactions; the deprived agent had to greps its own session files, while harness‑injected facts survived all 138 compact‑resumes with no loss.

## Significance  
This work shifts the focus from storage‑centric agents to delivery‑centric agents, showing that reliable memory is a harness property rather than an agent choice. By decoupling cue‑anchored retrieval from conscious decision‑making, it enables more robust long‑running coding systems and reduces cognitive load on developers.

## Related Concepts  
memory offloading, incidental encoding, event‑based prospective memory, composable vocabulary, cue‑anchored memory model, compaction boundaries, deterministic injection.
