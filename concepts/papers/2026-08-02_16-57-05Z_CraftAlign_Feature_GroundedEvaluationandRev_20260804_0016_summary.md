# Summary: 2026-08-02_16-57-05Z_CraftAlign_Feature_GroundedEvaluationandRevisionGu.md
Saved: 2026-08-04 00:16
Source: 2026-08-02_16-57-05Z_CraftAlign_Feature_GroundedEvaluationandRevisionGu.md
Model: None

---

## Summary  
CraftAlign is a framework that aligns AI‑generated stories with the craft of human storytelling by both assessing writing patterns and providing revision guidance. It predicts 304 explicit narrative features, scores their configuration against human or AI writing styles, and then applies structured perturbations to move the story toward the desired pattern. The inferred changes are converted into natural‑language instructions for a separate editor to rewrite the full text. Experiments demonstrate that CraftAlign reliably distinguishes human from AI patterns and yields superior revision results compared with existing baselines.

## Key Contributions  
- [Finding 1] A feature estimator predicts 304 explicit writing features spanning style and narrative, enabling fine‑grained analysis of AI story generation.  
- [Finding 2] A class‑conditional energy model scores the resulting feature configuration against human and AI writing patterns while conditioning on the original prompt, providing a quantitative alignment metric.  
- [Finding 3] The inference pipeline applies schema‑valid structured perturbations that convert into natural‑language guidance for editors, enabling story‑wide revisions rather than isolated edits.

## Methodology  
The authors designed two learned modules: (1) a feature estimator trained on paired human and AI stories to output a vector of 304 features; (2) an energy model that takes the feature vector and prompt as input and outputs a score indicating how close the story is to human or AI patterns. During inference, CraftAlign selects perturbations from a schema‑valid set—changes that reduce the energy toward the human pattern—and rewrites those changes into concise, editor‑friendly guidance sentences.

## Results  
Experiments on a held‑out dataset show that CraftAlign’s feature estimator and energy scorer achieve high accuracy in distinguishing human versus AI writing patterns. When used to generate revision guides, CraftAlign outperforms baseline methods across multiple editors and in a controlled human study where participants preferred the revised stories produced with CraftAlign guidance over those edited by baselines.

## Significance  
CraftAlign bridges the gap between automated story generation and human‑like storytelling craft, offering a systematic way to evaluate and improve AI narratives. By providing structured, feature‑grounded revision guidance, it supports multiple plausible revision strategies and can guide large‑scale content revisions beyond simple token edits.

## Related Concepts  
- Feature estimation  
- Energy modeling  
- Schema‑valid perturbations  
- Natural‑language editing  
- Human vs AI writing pattern detection  
- Revision guidance
