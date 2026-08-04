# Summary: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Saved: 2026-08-04 00:05
Source: 2026-08-03_15-35-28Z_GROVE_GrowingandReasoningoverTemporallyStratifiedM.md
Model: None

---

## Summary  
GROVE is a training‑free framework that enables a wearable assistant to both answer questions about its visual history and proactively recognize when that history is relevant. It grows a temporally stratified memory from a continuous video stream, preserving fine‑grained perceptual evidence while consolidating it into time‑stamped moments, coherent episodes, and recurring cross‑day patterns. Each stratum is equipped with scale‑native retrieval skills for locating observations, replaying activities, or traversing long‑range regularities. The system supports both reactive QA and proactive assistance through a unified memory interface.

## Key Contributions  
- [Finding 1] GROVE creates multiple temporal strata that capture fine‑grained visual evidence across days without any explicit training.  
- [Finding 2] It provides complementary retrieval skills per stratum, allowing precise access to observations, activity replay, or pattern traversal.  
- [Finding 3] The framework integrates reactive and proactive modes using a single memory interface, improving both QA accuracy and proactive usefulness.

## Methodology  
The authors treat the video stream as a causal source that continuously feeds into a hierarchical memory structure. First‑level strata store raw frames with timestamps; higher‑level strata aggregate these into episodes and cross‑day patterns. Retrieval skills are generated scale‑natively, meaning they adapt to the amount of evidence available in each stratum. The system is trained only by exposing it to streaming video; no supervised fine‑tuning is required.

## Results  
Across benchmarks such as MM‑lifelong and EgoServe, GROVE outperforms all competing methods, achieving state‑of‑the‑art scores on both question‑conditioned recall and proactive assistance tasks. Controlled ablations confirm that the temporal strata are essential: patterns spanning multiple days deliver the largest benefit, while single‑day evidence is less useful for long‑range reasoning.

## Significance  
GROVE bridges the gap between reactive QA and proactive assistance in wearable assistants by providing a unified memory that grows naturally from streaming video. Its training‑free design reduces deployment complexity, enabling real‑time personalization without offline fine‑tuning. This advances lifelong learning systems toward truly adaptive, context‑aware agents.

## Related Concepts  
- Temporal stratification  
- Scale‑native retrieval  
- Causal memory growth  
- Reactive vs. proactive assistance  
- Lifelong video learning
