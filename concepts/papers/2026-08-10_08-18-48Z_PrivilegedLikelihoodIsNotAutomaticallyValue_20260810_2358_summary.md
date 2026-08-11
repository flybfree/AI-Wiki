# Summary: 2026-08-10_08-18-48Z_PrivilegedLikelihoodIsNotAutomaticallyValue_ThreeC.md
Saved: 2026-08-10 23:58
Source: 2026-08-10_08-18-48Z_PrivilegedLikelihoodIsNotAutomaticallyValue_ThreeC.md
Model: None

---

## Summary  
The paper argues that token likelihood changes in on‑policy self‑distillation do not automatically translate into better reasoning or creditworthiness; they must be examined through three distinct lenses. It introduces a formal framework separating (i) whether the score tracks improved actions, (ii) how feedback construction alters what is compared, and (iii) what behavior the training loss reinforces. Experiments on a 20 B model with AIME 2025 data demonstrate that additive token scores are near chance and can even penalize correct traces after length adjustment, underscoring the need for careful validation.

## Key Contributions  
- **Finding 1:** Token likelihood changes do not guarantee better action tracking; a score may be independent of actual performance.  
- **Finding 2:** Feedback construction (using hindsight feedback versus another rollout) creates either self‑dependence or removes it, affecting the validity of the comparison.  
- **Finding 3:** The training loss reinforces specific behaviors that may not align with desired credit allocation.

## Methodology  
The authors formalize three questions: (1) does the token score correlate with improved actions? (2) does the feedback used to compute scores change the set of tokens being compared? (3) what behavior is reinforced by the training objective? They evaluate these via matched experiments, comparing an additive token‑score variant against an outcome‑only control and five other token‑score variants.

## Results  
In AIME 2025, the additive token score achieves an AUC of 0.505, essentially random guessing. Paired comparisons show that the outcome‑only control reaches 64.2 % success, whereas the five token‑score variants perform between 24.2 % and 33.9 %. Length adjustment slightly favors incorrect traces, indicating that the score can be misaligned with correct reasoning.

## Significance  
These findings reveal that self‑distillation credit assignment is not automatic; researchers must validate the meaning of scores, ensure feedback independence, and confirm training behavior alignment before trusting token‑based signals. The work provides a systematic checklist for evaluating on‑policy distillation methods.

## Related Concepts  
- On‑policy self‑distillation  
- Hindsight feedback  
- Token credit  
- Likelihood change  
- Outcome verification  
- AUC (area under the curve)  
- AIME benchmark
