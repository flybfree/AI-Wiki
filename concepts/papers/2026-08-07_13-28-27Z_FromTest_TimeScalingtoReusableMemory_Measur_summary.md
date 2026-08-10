# Summary: 2026-08-07_13-28-27Z_FromTest_TimeScalingtoReusableMemory_MeasuringCrys.md
Saved: 2026-08-09 22:57
Source: 2026-08-07_13-28-27Z_FromTest_TimeScalingtoReusableMemory_MeasuringCrys.md
Model: None

---

## Summary  
The paper tackles the “crystallization problem” in text‑to‑SQL (T2S) memory systems, where test‑time scaling improvements are discarded after each answer despite being verified. It proposes a controlled evaluation that isolates the effect of storing corrected queries while keeping the solver fixed and varying only one memory choice at a time. By measuring replay, cross‑question retention, and held‑out same‑database transfer, the study quantifies how retaining verified corrections improves accuracy on unseen questions.  

## Key Contributions  
- [Finding 1] Storing verified corrected queries yields a 4.34 percentage‑point absolute improvement in first‑attempt accuracy on BIRD’s held‑out set.  
- [Finding 2] This gain captures roughly 44.4 % of the total accuracy headroom that would be obtained via on‑demand repair for those queries, showing a substantial residual value.  
- [Finding 3] Database‑specific content is identified as the primary driver of these improvements; richer retrieval formats or elaborate retrievers provide no additional benefit.  

## Methodology  
The authors fix a single‑shot text‑to‑SQL solver and systematically vary only one memory choice—whether to store a verified corrected query—across experiments. They evaluate three metrics: replay (reusing the same correction), cross‑question retention (keeping corrections across different queries), and held‑out same‑database transfer (applying stored corrections to unseen test questions). This controlled design isolates the effect of memory storage from other system components.  

## Results  
On BIRD, enabling verified query storage boosts held‑out first‑attempt accuracy by 4.34 percentage points. The study also reports that this improvement captures about 44.4 % of the overall accuracy gain achievable through on‑demand repair for those queries. Experiments across multiple databases confirm that database‑specific content is the main operating ingredient, while richer retrieval formats or more complex retrievers do not enhance gains.  

## Significance  
The findings demonstrate that memory systems can retain valuable correction episodes, turning test‑time scaling into a reusable resource rather than a one‑off cost. This insight challenges the assumption that all repair benefits are expended per query and opens avenues for designing memory strategies that maximize long‑term utility in T2S applications.  

## Related Concepts  
- Test‑time scaling  
- Text‑to‑SQL (T2S)  
- Memory in T2S systems  
- Crystallization problem  
- On‑demand repair  
- Replay, cross‑question retention, held‑out transfer
