# Summary: 2026-07-27_06-16-28Z_BeyondLocalInspection_Global_Guideline_GroundedEva.md
Saved: 2026-07-27 21:30
Source: 2026-07-27_06-16-28Z_BeyondLocalInspection_Global_Guideline_GroundedEva.md
Model: None

---

## Summary  
The paper tackles the problem that post‑hoc explainability tools often generate locally plausible but globally misleading explanations in medical AI, especially when they ignore clinically relevant ECG patterns such as low‑amplitude segments or ST‑segment changes. By leveraging explicit clinical guidelines that define diagnostically important regions, the authors propose a global, guideline‑grounded framework to evaluate these explanations across heartbeats rather than on isolated samples. Their work demonstrates that many gradient‑based XAI methods—trained primarily for computer‑vision tasks—systematically misattribute importance to signal amplitude over disease‑specific morphology. This reveals a critical gap in current XAI research that could lead clinicians to trust inaccurate model behavior.

## Key Contributions  
- **Systematic failure of CV‑trained methods**: The authors find that explanations often follow raw signal amplitude rather than clinically meaningful patterns, with Spearman correlations reaching up to 0.69.  
- **Global guideline‑grounded evaluation**: By aggregating explanations across heartbeats and comparing them to ECG clinical regions (e.g., ST segment), they uncover systematic errors not visible in single‑sample heatmaps.  
- **Method performance below chance**: Nine of the thirteen gradient‑based methods perform worse than random for at least one condition, such as LRP‑ε assigning only 4.6 % relevance to the ST segment versus 63.8 % for LRP‑SIGN.

## Methodology  
The study uses ECG data from PTB‑XL and four binary classifiers trained on this dataset. Gradient‑based post‑hoc XAI methods are applied to generate explanations for each prediction. The authors aggregate these explanations across consecutive heartbeats, creating a global view of model behavior. They then evaluate the aggregated outputs against two clinically defined regions: low‑amplitude segments (representing subtle disease signals) and high‑amplitude QRS morphology (more obvious). The evaluation is quantified using Spearman correlation to measure alignment between explanation importance scores and guideline‑defined relevance.

## Results  
The mean Spearman correlations across all methods range up to 0.69, indicating moderate but still poor alignment with clinical relevance. For the ST segment, LRP‑ε contributes only 4.6 % of its importance, whereas LRP‑SIGN correctly assigns 63.8 %. Moreover, nine out of thirteen gradient‑based methods fall below chance for at least one condition, showing inconsistent reliability when evaluated globally.

## Significance  
These findings underscore that global, domain‑specific evaluation is essential for trustworthy medical AI. Local explanations can hide systematic biases, and without a framework that respects clinical guidelines, XAI tools may mislead clinicians by emphasizing irrelevant signal features. The work provides a template for evaluating post‑hoc XAI methods in regulated domains where clinical knowledge is explicit.

## Related Concepts  
Explainable AI (XAI), post‑hoc explanations, gradient‑based methods, ECG classification, clinical guidelines, low‑amplitude segments, high‑amplitude QRS morphology, ST segment, LRP‑SIGN, LRP‑ε, Spearman correlation.
