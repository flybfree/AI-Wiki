# Summary: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Saved: 2026-07-24 02:42
Source: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Model: None

---

## Summary  
The paper argues that coding agents should rely on cue‑anchored working memory as a harness property rather than storing data voluntarily, because human expertise is maintained by incidental, situationally bound facts that are retrieved automatically when cues appear. It proposes a two‑tier design theory that maps cognitive memory mechanisms to architectural requirements and introduces a composable vocabulary of trigger conditions for memories. The authors demonstrate experimentally that agents rarely use voluntary memory while deterministic injection yields reliable recall across compaction cycles.  

## Key Contributions  
- A two‑tier design theory linking incidental encoding, prospective memory, and event‑based prospective memory to architectural requirements.  
- A cue‑anchored memory model where memories carry first‑class trigger conditions over a composable vocabulary (path, symbol, semantic, event, temporal).  
- Empirical evidence that voluntary memory use is negligible (0/114 turns) whereas deterministic injection preserves facts across 138 compact‑resumes with zero false alarms.  

## Methodology  
The authors grounded their theory in cognitive literature on memory offloading and incidental encoding, mapping each mechanism to a concrete architectural requirement. They built the cue‑anchored model as a deterministic harness component that injects trigger conditions into a composable vocabulary, then evaluated it on a real coding task with controlled runs comparing voluntary versus injected memory usage.  

## Results  
Voluntary memory operations were recorded as zero out of 114 turns, indicating near‑complete reliance on the harness. Deterministic injection delivered every seeded run with no false alarms. Approximately 39 % of intra‑session re‑reads repurchased content before a compaction boundary. A repeated‑compaction decay probe showed that ten facts held only in conversation vanished at the first summary and were absent from 106 of 108 compactions; however, facts injected into a harness‑owned store survived all 138 compact‑resumes, with the final summary containing none.  

## Significance  
This work shifts memory handling from agent‑driven storage to a reliable harness channel that never requires the agent to think about retrieval, aligning long‑running agents with human expertise and improving system robustness without increasing cognitive load.  

## Related Concepts  
- Cue‑anchored memory  
- Incidental encoding  
- Prospective memory  
- Two‑tier design theory  
- Composable vocabulary (path, symbol, semantic, event, temporal)  
- Compaction boundary  
- Session files  
- Retrieval triggers  
- Working‑memory offloading
