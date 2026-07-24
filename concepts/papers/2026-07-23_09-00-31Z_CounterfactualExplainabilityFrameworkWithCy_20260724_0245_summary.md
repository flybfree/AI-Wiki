# Summary: 2026-07-23_09-00-31Z_CounterfactualExplainabilityFrameworkWithCycleGANA.md
Saved: 2026-07-24 02:45
Source: 2026-07-23_09-00-31Z_CounterfactualExplainabilityFrameworkWithCycleGANA.md
Model: None

---

## Summary  
The paper proposes CounterFundus, a CycleGAN‑driven framework that generates clinically meaningful counterfactual healthy fundus images from pathological retinal disease cases and integrates this visual translation with an EfficientNet‑B5 detector for disease classification. To ensure the explanations are trustworthy, it introduces the Counterfactual‑Classifier Alignment Score (CCAS), which quantifies spatial agreement between the generated difference maps and the classifier’s saliency using Spearman correlation, binary IoU, and pointing accuracy.

## Key Contributions  
- CounterFUNDUS framework combines a CycleGAN generator with an EfficientNet‑B5 detector to produce visually plausible disease‑to‑normal fundus translations.  
- Introduction of CCAS metric that evaluates the alignment of counterfactual difference maps with classifier saliency across three dimensions (Spearman correlation, binary IoU, pointing accuracy).  
- Ablation study demonstrating that filtering counterfactuals by high CCAS improves downstream classification performance.

## Methodology  
The authors train a CycleGAN to map pathological fundus images into synthetic normal ones; the generator creates counterfactual healthy images. The difference between the original and generated images yields a difference map, which is then compared with the saliency map produced by the EfficientNet‑B5 classifier using CCAS. An ablation experiment removes all non‑CCAS‑aligned augmentations to assess impact on classification accuracy.

## Results  
Experiments on public retinal datasets show that generated counterfactuals align well with classifier‑relevant regions across all CCAS components (Spearman r≈0.78, IoU≈0.62, pointing accuracy≈0.59). When only CCAS‑filtered augmentations are used, classification accuracy is boosted by 3–4 % compared to using all generated counterfactuals.

## Significance  
CounterFUNDUS provides a clinically interpretable explainable AI (XAI) method that bridges deep learning predictions with visible retinal changes. This enables clinicians to trust model outputs and supports early disease detection without reliance on specialist‑only assessments, reducing diagnostic bottlenecks.

## Related Concepts  
CycleGAN, EfficientNet‑B5, counterfactual explanations, saliency maps, post‑hoc explainability, post‑hoc saliency, Counterfactual‑Classifier Alignment Score (CCAS), Spearman correlation, binary IoU, pointing accuracy, EigenCAM alignment.
