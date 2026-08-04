# Summary: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Saved: 2026-08-04 01:01
Source: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Model: None

---

## Summary  
A wearable assistant must both retrieve visual information from its past and decide when that history is relevant to the current situation. Existing video‑memory systems are limited to question‑conditioned recall, while proactive assistants rely on separate memory and control modules. GROVE bridges this gap by providing a single, training‑free memory that grows causally from a continuous video stream. The framework stores fine‑grained perceptual evidence, consolidates it into temporal strata (episodic episodes and recurring patterns), and equips each stratum with scale‑native retrieval skills for locating observations, replaying activities, or tracing long‑range regularities.

## Key Contributions  
- [Finding 1] Temporal stratification of memory from a streaming video enables fine‑grained evidence retention across multiple days.  
- [Finding 2] A unified retrieval interface supports both reactive QA (user‑initiated) and proactive assistance (situation‑driven).  
- [Finding 3] Ablations demonstrate that pattern strata deliver the greatest benefit when evidence spans several days, complementing other strata.

## Methodology  
The authors built GROVE as a training‑free system that continuously ingests video frames. Each frame is encoded into perceptual embeddings and stored at discrete time stamps, forming strata: (i) fine‑grained evidence for short‑term recall, (ii) episode‑level memories for coherent activities, and (iii) pattern memories for cross‑day regularities. Retrieval skills are scale‑native, meaning they operate directly on the memory’s temporal structure without additional decoding layers. Reactive queries trigger a lookup in the appropriate stratum, while proactive assistance scans strata to generate suggestions based on current context.

## Results  
On benchmark suites such as MM‑lifelong and EgoServe—challenging tasks requiring lifelong visual recall GROVE outperformed all competing methods, achieving state‑of‑the‑art scores. Controlled ablations confirm that the temporal strata are complementary: pattern memory yields the largest improvement when evidence covers multiple days, whereas short‑term evidence benefits from episodic consolidation.

## Significance  
GROVE enables wearables to maintain a rich multimodal visual history without heavy training, improving both reactive answer quality and proactive assistance relevance. By integrating long‑term patterns with recent episodes, it supports lifelong learning in devices that continuously stream video data, a capability critical for human‑centric AI assistants.

## Related Concepts  
- Temporal stratification of memory  
- Causal growth of visual evidence  
- Retrieval skills (scale‑native)  
- Reactive vs. proactive assistance  
- Lifelong video memory consolidation  
- Pattern recognition across days
