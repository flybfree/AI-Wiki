# Summary: 2026-08-02_16-57-05Z_CraftAlign_Feature_GroundedEvaluationandRevisionGu.md
Saved: 2026-08-04 00:16
Source: 2026-08-02_16-57-05Z_CraftAlign_Feature_GroundedEvaluationandRevisionGu.md
Model: None

---

## Summary  
The paper introduces CraftAlign, a framework that aligns AI‑generated stories with the craft of human storytelling. It addresses limitations of current detection and revision methods which are either label‑based or static. CraftAlign uses learned modules to predict narrative features and score them against human patterns. The approach enables story‑wide revisions guided by feature alignment.

## Key Contributions  
- [Finding 1] CraftAlign distinguishes between Human and AI writing patterns with high accuracy using a class‑conditional energy model.  
- [Finding 2] The framework generates natural‑language revision guidance that outperforms baseline edits across editors.  
- [Finding 3] Feature‑grounded evaluation enables multiple plausible revision strategies beyond localized fixes.

## Methodology  
The authors built CraftAlign around two learned modules: a feature estimator based on Qwen3.5‑9B predicts 304 explicit writing features covering style and narrative; a class‑conditional energy model scores the configuration against Human/AI patterns, conditioning on the prompt. At inference time, the system applies schema‑valid structured perturbations that shift the feature vector toward human patterns and translates them into guidance for an editor.

## Results  
Experiments demonstrate that CraftAlign correctly identifies Human vs AI writing with >90% accuracy; its revision guidance improves story coherence scores by 15–20% compared to baselines such as simple edit‑and‑replace or rule‑based fixes. In a human study, editors rated the revised stories as more natural and less formulaic.

## Significance  
This work advances AI storytelling by moving beyond surface‑level detection to feature‑aware revision, allowing story‑wide improvements in causal organization, ending treatment, and style. It provides a scalable method for aligning synthetic narratives with human expectations, potentially reducing the “AI flavor” that deters readers.

## Related Concepts  
- Feature estimation  
- Energy modeling  
- Structured perturbations  
- Revision guidance  
- Human vs AI writing pattern detection
