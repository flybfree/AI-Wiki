# Summary: 2026-07-28_12-55-29Z_DynaBridge_DynamicSummary_GuidedCross_TaskMultimod.md
Saved: 2026-07-28 22:49
Source: 2026-07-28_12-55-29Z_DynaBridge_DynamicSummary_GuidedCross_TaskMultimod.md
Model: None

---

## Summary  
The paper introduces DynaBridge, a dynamic summary‑guided cross‑task multimodal framework designed to predict depression, anxiety, and stress risk from the DASS‑21 questionnaire while respecting its psychometric structure. By encoding acoustic, visual, and textual cues across sessions and augmenting them with frozen LLM‑generated DASS‑aware summaries that encode participant‑level semantic evidence, DynaBridge learns to reconstruct ordinal item distributions and fuse this evidence with direct multimodal risk predictions. The approach employs a confidence‑aware refinement strategy that conservatively incorporates high‑confidence semantic cues. On the official AdoDAS validation split, DynaBridge achieves 0.5012 mean F1 for overall risk prediction and 0.3216 mean QWK for individual DASS‑21 item predictions, outperforming both the baseline and representative multimodal methods.

## Key Contributions  
- [Finding 1] DynaBridge integrates frozen LLM‑generated DASS‑aware summaries as participant‑level semantic evidence to bridge multimodal cues with psychometric structure.  
- [Finding 2] The framework reconstructs ordinal item distributions from soft scores and fuses them with direct multimodal risk predictions, yielding a unified risk estimate.  
- [Finding 3] A confidence‑aware refinement mechanism selectively incorporates high‑confidence semantic cues to improve robustness without overfitting.

## Methodology  
DynaBridge first encodes acoustic, visual, and textual inputs from multiple sessions using separate modality encoders. These embeddings are concatenated with LLM‑generated DASS summaries that capture the ordered symptom mapping of the questionnaire. The model then predicts soft scores for each DASS subscale (depression, anxiety, stress) by modeling the conditional distribution of item responses given the multimodal and semantic evidence. A confidence‑aware refinement step evaluates the reliability of high‑confidence semantic cues and adjusts the final risk prediction accordingly, ensuring conservative integration.

## Results  
On the official AdoDAS validation split, DynaBridge outperforms the baseline and representative multimodal methods, achieving a mean F1 of 0.5012 for overall depression/anxiety/stress risk prediction and a mean QWK (Quantitative Weighted K‑Weight) of 0.3216 for DASS‑21 item predictions. These gains demonstrate that the dynamic summary‑guided fusion effectively leverages both multimodal cues and psychometric structure.

## Significance  
The contribution matters because existing generic fusion models ignore the ordered nature of DASS items, leading to suboptimal risk estimates. DynaBridge addresses this gap by respecting the questionnaire’s psychometric design, thereby providing more accurate, clinically relevant mental‑health assessments that can be deployed in real‑world settings.

## Related Concepts  
- Multimodal fusion  
- Cross‑task learning  
- Psychometric structure preservation  
- LLM‑generated summaries  
- Confidence‑aware refinement
