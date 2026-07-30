# Summary: 2026-07-29_15-55-31Z_VisualCreditAuditforMultimodalSpatialReasoning.md
Saved: 2026-07-29 20:39
Source: 2026-07-29_15-55-31Z_VisualCreditAuditforMultimodalSpatialReasoning.md
Model: None

---

## Summary  
The paper introduces Visual Credit Audit (VCA), a method for dissecting the performance of multimodal large language models on closed yes/no spatial benchmarks. VCA distinguishes two estimands: whether an image provides additional support beyond text‑only and blank controls, and whether the model’s decision is consistent with the visual evidence. By separating these components, VCA reveals that many correct answers are “uncredited,” meaning they lack visual justification. The authors also show that relation‑specific responses can be dramatically altered when images are reversed or absent, highlighting hidden biases in benchmark success.

## Key Contributions  
- [Finding 1] VCA separates two estimands—image‑supported correctness and text‑only correctness—using a training‑label‑free audit that does not require answer flipping.  
- [Finding 2] Applying labels yields dependence‑credited correctness (D‑CC); same‑split image permutations reduce D‑CC by 21.25–47.80 points with 95 % confidence intervals above zero, indicating strong visual influence.  
- [Finding 3] Response to relation reversal spans 81.57–100 %, while pooled answer changes are 32.11 %, showing that models often flip answers when visual evidence is altered.

## Methodology  
VCA employs a fixed forced‑choice interface where each spatial question presents an image, text description, and two control conditions (text‑only, blank). The model’s declared yes/no answer is compared to the controls to estimate whether the image adds support. When labels are added, D‑CC measures how much the correct answer aligns with gold‑aligned positive support. A fixed‑pixel relation contrast and a 3×3 evidence‑source factorial test null conditions to verify that null controls cannot identify genuine visual influence.

## Results  
Across four open MLLMs and two spatial benchmarks, 12.73–26.25 % of decisions are correct yet uncredited. D‑CC is reduced by 21.25–47.80 points after same‑split permutation (all 95 % intervals > 0). Among correctly answered but uncredited items, the model responds to relation reversal in 81.57–100 % of cases and changes pooled answers by 32.11 %. Independent audits on 108 geometry‑compatible edits provide a bounded natural‑image correspondence check.

## Significance  
VCA decomposes benchmark success into three distinct components: correctness, additional image support, and relation‑consistent response. This granular view uncovers hidden biases where visual evidence is ignored or misused, enabling more honest evaluation of multimodal spatial reasoning models and guiding improvements in benchmark design.

## Related Concepts  
visual credit audit, estimands, spatial reasoning benchmarks, multimodal large language models (MLLMs), forced‑choice interface, control conditions, dependence‑credited correctness (D‑CC), same‑split permutation, relation reversal, evidence‑source factorial, natural‑image correspondence.
