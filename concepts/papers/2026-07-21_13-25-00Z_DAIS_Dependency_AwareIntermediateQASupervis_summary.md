# Summary: 2026-07-21_13-25-00Z_DAIS_Dependency_AwareIntermediateQASupervisionforC.md
Saved: 2026-07-24 00:50
Source: 2026-07-21_13-25-00Z_DAIS_Dependency_AwareIntermediateQASupervisionforC.md
Model: None

---

## Summary  
Chain‑of‑thought (CoT) supervision typically presents a single, uninterrupted rationale that optimizes the whole reasoning path, leaving little guidance for how local conclusions should influence later decisions. DAIS addresses this limitation by converting filtered teacher rationales into stage‑level QA records, where each intermediate record predicts a local answer conditioned on the previous states required to make that decision. The final‑answer record retains the original task format, so evaluation uses only the input (and optional context). This framework provides a lightweight auxiliary supervision signal that can be applied during training without altering the downstream inference pipeline.

## Key Contributions  
- **DAIS framework**: Introduces Dependency‑Aware Intermediate QA Supervision, a training‑time method that transforms filtered teacher rationales into stage‑level QA records.  
- **Dependency‑conditioned predictions**: Each intermediate record predicts a local answer based on the valid previous states needed for that decision, rather than relying solely on longer targets or extra text.  
- **Empirical gains**: Demonstrates that DAIS improves average final‑answer accuracy across GDPR, AIACT, MedQA, and FOLIO with multiple Qwen backbones, achieving a largest gain of 5.6 % and an average gain of 4.2 % over the strongest non‑DAIS baselines.

## Methodology  
The authors adopt a training‑time framework that processes teacher rationales at the moment they are generated. Instead of feeding the entire rationale to a single model, DAIS splits it into discrete QA records: one for each intermediate reasoning step and one final record preserving the original task format. The intermediate records predict answers conditioned on the context that has already been processed (the “previous states”), while the final record remains unchanged. During evaluation, only the original input (and optionally a short context) is used to generate the answer, allowing DAIS to act as an auxiliary supervision signal without affecting inference.

## Results  
Across four benchmark suites—GDPR, AIACT, MedQA, and FOLIO—DAIS consistently outperformed answer‑only baselines, flat chain‑of‑thought baselines, and independent QA baselines. The improvement is quantified as an average gain of 4.2 % in final‑answer accuracy, with a maximum lift of 5.6 % on policy‑compliance tasks. Controlled ablations confirm that the benefit stems from valid previous‑state conditioning rather than simply longer targets or additional intermediate text.

## Significance  
DAIS reveals that conditioning intermediate supervision on legitimate prior states yields measurable gains beyond simple augmentation, offering a lightweight way to enrich standard final‑answer inference. By providing dependency‑aware guidance during training, it can improve reasoning performance without requiring costly model retraining or longer target generation.

## Related Concepts  
- Chain‑of‑thought (CoT) supervision  
- Flat rationale targets  
- Dependency‑conditioned intermediate QA  
- Stage‑level QA records  
- Auxiliary supervision signal
