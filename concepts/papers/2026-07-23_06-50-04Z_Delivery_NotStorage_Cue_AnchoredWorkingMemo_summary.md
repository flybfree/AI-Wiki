# Summary: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Saved: 2026-07-24 02:33
Source: 2026-07-23_06-50-04Z_Delivery_NotStorage_Cue_AnchoredWorkingMemoryasaHa.md
Model: None

---

## Summary  
The paper argues that coding agents should rely on cue‑anchored working memory as a harness property rather than storing data in their own memory, because human expertise is situational and offloaded automatically. It proposes a two‑tier design theory that maps cognitive memory mechanisms to architectural requirements. The authors introduce a composable vocabulary of trigger conditions (path, symbol, semantic, event, temporal) that the harness injects deterministically into the agent’s session files. Evaluation shows that voluntary memory use vanishes while deterministic injection succeeds across sessions.

## Key Contributions  
- A two‑tier design theory grounded in cognitive literature on memory offloading, incidental encoding, and event‑based prospective memory, each mapped to an architectural requirement.  
- A cue‑anchored memory model where memories carry first‑class trigger conditions over a composable vocabulary (path, symbol, semantic, event, temporal), evaluated deterministically by the harness—a composition no surveyed academic or shipped system provides.  
- Controlled experimental results on a real coding task: voluntary memory use is near zero (0/114 turns); deterministic injection delivered in every seeded run with zero false alarms; 39 % of intra‑session re‑reads repurchase content before a compaction boundary.

## Methodology  
The authors grounded their theory in the cognitive literature on memory offloading, incidental encoding, and event‑based prospective memory. They built a harness that injects cues deterministically into the agent’s session files using a vocabulary of trigger types (path, symbol, semantic, event, temporal). Experiments were conducted with a real coding task over 114 turns, measuring memory operations, re‑read rates, and compaction effects.

## Results  
Voluntary memory use was zero (0/114 turns), indicating the agent never chooses to write or read its own memory. Deterministic injection succeeded in every seeded run with no false alarms. Of 39 % of intra‑session re‑reads, content repurchased before a compaction boundary suggests that the harness’s store is the source of repeated retrievals. A repeat‑compaction decay probe held ten facts only in conversation; after the first summary, all ten vanished and survived only in two of 108 compactions, while facts injected from a harness‑owned store remained intact across 138 compact‑resumes.

## Significance  
Shifting focus from storage to delivery aligns with human‑like memory offloading, enabling more reliable long‑running agents without burdening them. The work demonstrates that the reliable memory channel is one the agent never has to think about, improving consistency and reducing cognitive load in coding environments.

## Related Concepts  
Cue‑anchored working memory, two‑tier design theory, event‑based prospective memory, incidental encoding, composable vocabulary, compaction decay, harness property.
