# Summary: 2026-07-22_09-29-49Z_AMulti_DimensionalEvaluationofExplainabilityinMedi.md
Saved: 2026-07-24 01:45
Source: 2026-07-22_09-29-49Z_AMulti_DimensionalEvaluationofExplainabilityinMedi.md
Model: None

---

## Summary  
This paper proposes a multi‑dimensional framework to evaluate explainability in encoder‑based media bias detection models such as BERT and RoBERTa. By measuring predictive performance, explanation plausibility (token‑level alignment with expert rationales), and mechanistic faithfulness (recovery of signal from compact attention heads under counterfactual masking), the authors reveal that these three axes capture distinct aspects of model behavior rather than a single “explainability” metric. Their work demonstrates that improving one axis does not automatically improve the others, even when using the same underlying architecture.

## Key Contributions  
- [Finding 1] Predictive performance, explanation plausibility, and mechanistic faithfulness characterize different dimensions of explainability in media bias detection.  
- [Finding 2] Attention‑supervised finetuning enhances token‑level plausibility but yields heterogeneous gains across model sizes and architectures.  
- [Finding 3] Circuit analysis shows that the ability to recover predictive signals from a small set of attention heads varies widely, indicating that model scale alone does not determine circuit compressibility.

## Methodology  
The authors employ the Bias Annotations By Experts (BABE) dataset as their benchmark. They train both BERT and RoBERTa in base and large variants as classifiers for bias detection. Evaluation proceeds along three complementary axes: predictive performance is measured by standard F1 scores; explanation plausibility is assessed via token‑level alignment between model outputs and expert rationales; mechanistic faithfulness is tested by masking counterfactual rationales and checking whether a compact set of attention heads can still reproduce the original prediction. To explore plausibility, they introduce attention‑supervised finetuning, which treats expert annotations as an auxiliary training signal.

## Results  
Baseline models achieve moderate F1 scores but exhibit low token‑level alignment and poor recovery from masked attention heads. Introducing attention supervision lifts plausibility for RoBERTa‑large but yields modest gains for BERT‑base, highlighting architecture differences. Circuit analysis reveals that only a subset of heads remain functional after rationales are masked; this subset is larger in RoBERTa‑large than in BERT‑base, yet still far smaller than the full head set. Thus, mechanistic faithfulness does not scale monotonically with model size.

## Significance  
These findings underscore that explainability cannot be reduced to a single quantitative measure and that different stakeholders may care about distinct dimensions—accuracy versus interpretability versus internal consistency. The study provides a methodological template for future work on bias detection where transparent reasoning must be evaluated independently of raw performance.

## Related Concepts  
- Media bias detection, encoder‑based classifiers (BERT, RoBERTa)  
- Attention mechanisms and attention supervision  
- Token‑level alignment with human rationales  
- Mechanistic interpretability via circuit analysis  
- Counterfactual masking for faithfulness testing
