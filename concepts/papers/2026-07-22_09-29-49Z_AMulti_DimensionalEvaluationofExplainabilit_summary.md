# Summary: 2026-07-22_09-29-49Z_AMulti_DimensionalEvaluationofExplainabilityinMedi.md
Saved: 2026-07-24 01:38
Source: 2026-07-22_09-29-49Z_AMulti_DimensionalEvaluationofExplainabilityinMedi.md
Model: None

---

## Summary  
The paper proposes a multi‑dimensional evaluation framework for explainability in encoder‑based media bias detection, arguing that automatic predictions alone are insufficient without explanations that reflect the model’s reasoning. It evaluates BERT and RoBERTa (both base and large variants) on three complementary axes: predictive performance, explanation plausibility (token‑level alignment with expert rationales), and mechanistic faithfulness (recovery of signal when counterfactual rationales are masked). The authors also introduce attention‑supervised finetuning as an intervention that boosts plausibility but does not guarantee faithfulness. Their study demonstrates that these axes capture distinct aspects of model behavior, each requiring separate assessment.

## Key Contributions  
- [Finding 1] Predictive performance and explanation plausibility are often at odds; improving one can degrade the other without necessarily enhancing mechanistic faithfulness.  
- [Finding 2] Attention‑supervised finetuning improves token‑level alignment with expert rationales, yet does not guarantee that compact attention heads retain predictive power under counterfactual masking.  
- [Finding 3] Circuit analysis reveals that mechanistic recoverability varies widely across architectures and is not solely determined by model size.

## Methodology  
The authors use the Bias Annotations By Experts (BABE) dataset, which provides human‑annotated bias labels for news articles. They train BERT and RoBERTa in two configurations: standard classification and attention‑supervised finetuning where expert rationales serve as an auxiliary signal. For each model they compute predictive accuracy on the test set, evaluate plausibility by measuring token‑level overlap between predicted attention heads and human rationales, and assess mechanistic faithfulness via counterfactual rationale masking—i.e., whether a small subset of attention heads still predicts bias when most rationales are hidden. This three‑axis approach allows systematic comparison across architectures.

## Results  
Predictive accuracy is comparable among BERT (base/large) and RoBERTa (base/large), confirming that model scale alone does not dominate performance. Explanation plausibility, however, varies: attention‑supervised finetuned models show higher token‑level alignment with expert rationales than unsupervised counterparts. Mechanistic faithfulness is low across all models when counterfactual masking is applied, except for the fine‑tuned RoBERTa large variant, which retains a modest predictive signal from a compact set of heads. Overall, the study shows that attention supervision can boost plausibility but does not universally improve faithfulness.

## Significance  
These findings underscore that explainability in media bias detection cannot be captured by a single metric; instead, predictive accuracy, attribution plausibility, and mechanistic recoverability each reflect different facets of model behavior. By evaluating them separately, researchers and practitioners can identify which aspects of a model’s reasoning are trustworthy and which may need further refinement.

## Related Concepts  
- Encoder‑based classifiers (BERT, RoBERTa)  
- Attention mechanisms and attention heads  
- Attribution methods (token‑level alignment)  
- Mechanistic interpretability  
- Counterfactual rationale masking  
- Multi‑dimensional evaluation frameworks  
- BABE dataset for human‑annotated bias labels
