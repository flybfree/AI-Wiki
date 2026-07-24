# Summary: 2026-07-22_15-25-05Z_Self_supervisiondrivesrepresentationalconvergencei.md
Saved: 2026-07-24 02:06
Source: 2026-07-22_15-25-05Z_Self_supervisiondrivesrepresentationalconvergencei.md
Model: None

---

## Summary  
The authors investigate whether the self‑supervised objective that drives training of medical foundation models produces more convergence in representation space than clinical supervision does. Using a controlled experiment across image and text encoders with varying objectives but fixed data, architecture, and scale, they show that representations converge modestly above random chance, primarily because of the self‑supervised loss rather than label‑based training. The convergence is limited to within‑modality embeddings, does not align with radiologist judgments, and cannot be extrapolated across modalities or language. Nevertheless, a simple linear classifier retains about 85 % of its performance when transferred between encoders and hospitals, suggesting limited interoperability that can be engineered.

## Key Contributions  
- [Finding 1] Self‑supervised objectives drive representation convergence more than clinical supervision in medical foundation models.  
- [Finding 2] Convergence is modest but above a random floor, confined to within‑modality embeddings and does not improve with model size or capability.  
- [Finding 3] Linear classifiers can transfer across encoders and hospitals, preserving roughly 85 % of original performance despite limited shared geometry.

## Methodology  
The study dissects 18 image encoders and 7 text encoders (open‑weight, runnable locally) spanning 7 M to 27 B parameters across five imaging modalities. All models are trained on the same chest‑radiograph dataset (650,982 images from six sources). To isolate cause, the authors vary only the pretraining objective while keeping data, architecture, and scale constant; they also reproduce the effect in a synthetic model to verify that convergence stems from the self‑supervised loss rather than clinical labels.

## Results  
Matched self‑supervised encoders achieved 40.4 % similarity on chest radiography, compared with 21.1 % for label‑supervised and 3.3 % for image‑text models (Spearman ρ = 0.302, p = 0.223). Convergence does not grow with model size or capability. Within‑modality similarity is the highest; cross‑modal and clinical language alignment are negligible. A linear classifier trained on one encoder retains ~85 % of its accuracy when applied to five held‑out hospitals, indicating limited but usable interoperability.

## Significance  
Understanding that self‑supervision—not scale or clinical supervision—drives convergence informs the design of medical foundation models: objectives should be chosen to maximize useful shared geometry, and validation must target modalities where representation overlap is weak. The finding that simple classifiers can transfer across hospitals suggests that interoperability can be engineered around objective‑induced alignment rather than relying on raw model similarity.

## Related Concepts  
- Self‑supervision  
- Representation convergence  
- Medical foundation models  
- Clinical supervision (label‑based training)  
- Linear classifier transfer  
- Modality‑specific alignment  
- Synthetic training for causal analysis
