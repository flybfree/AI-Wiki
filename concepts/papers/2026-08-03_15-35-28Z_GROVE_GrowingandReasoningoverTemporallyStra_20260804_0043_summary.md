# Summary: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Saved: 2026-08-04 00:43
Source: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Model: None

---

## Summary  
GROVE is a training‑free framework that enables a wearable assistant to both retrieve visual information from its streaming video history and proactively generate useful insights without explicit user queries. By growing a temporally stratified memory directly from the continuous stream, GROVE creates layered evidence (perceptual moments), coherent episodes, and recurring cross‑day patterns, each paired with native retrieval skills for locating observations, replaying activities, or traversing long‑range regularities. The system unifies reactive question‑answering and proactive assistance through a single memory interface, achieving state‑of‑the‑art performance on lifelong video benchmarks.

## Key Contributions  
- [Finding 1] GROVE is a training‑free framework that grows its memory causally from a continuous video stream, eliminating the need for pre‑training or external datasets.  
- [Finding 2] The system organises this growth into temporally stratified strata—fine‑grained perceptual evidence, coherent episodes, and recurring cross‑day patterns—each serving distinct retrieval purposes.  
- [Finding 3] Every stratum is equipped with a scale‑native retrieval skill that can locate observations, replay activities, or traverse long‑range regularities without additional training.

## Methodology  
The authors treat the video stream as an ongoing input signal and continuously feed it into a memory‑growth pipeline. At each time step, perceptual evidence is stored as discrete, time‑stamped moments; these moments are grouped into episodes that share temporal coherence; over days, patterns emerge that recur across sessions. The framework couples this memory with a control module: reactive QA initiates retrieval via user queries, while proactive assistance triggers it when the current situation suggests relevance. Because all components are built incrementally from raw video, no separate training phases or external models are required.

## Results  
On the MM‑lifelong and EgoServe benchmarks, GROVE outperforms all competing methods in both reactive QA and proactive assistance tasks, achieving the best reported scores across multiple evaluation criteria. Controlled ablations confirm that the temporal strata are complementary: patterns spanning multiple days provide the largest benefit, indicating that long‑range regularities amplify recall quality. The ablation also shows that each stratum’s retrieval skill is correctly aligned with its purpose—perceptual evidence supports fine‑grained lookup, episodes enable activity replay, and cross‑day patterns support traversal.

## Significance  
GROVE addresses a critical gap in wearable assistants: the need for a single memory that serves both reactive user queries and proactive suggestions. By integrating these functions through temporally stratified growth, it enables richer, context‑aware assistance without sacrificing efficiency or requiring extensive training data. This unified approach could lead to more natural, persistent interactions between humans and their devices.

## Related Concepts  
- Streaming video experience  
- Temporal stratification of memory  
- Causal growth of episodic evidence  
- Scale‑native retrieval skills  
- Lifelong learning from continuous streams  
- Cross‑day pattern detection
