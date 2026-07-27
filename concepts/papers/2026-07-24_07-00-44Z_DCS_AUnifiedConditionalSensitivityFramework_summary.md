# Summary: 2026-07-24_07-00-44Z_DCS_AUnifiedConditionalSensitivityFrameworkforCros.md
Saved: 2026-07-26 21:43
Source: 2026-07-24_07-00-44Z_DCS_AUnifiedConditionalSensitivityFrameworkforCros.md
Model: None

---

## Summary  
The paper proposes a unified post‑hoc detection framework for cross‑modal copyright infringement that treats evidence as a counterfactual conditional distribution shift. It formalizes this view using conditional differential privacy and introduces Dual‑Branch Conditional Sensitivity (DCS) as an operational statistic measuring the observable gap between two locally perturbed model states. The framework links this displacement to the unavailable effect of including or removing protected data through influence‑function analysis, thereby bounding sensitivity with known quantities such as privacy budget, local curvature, dataset scale, and perturbation step size. A calibrated detection statistic further subtracts orthogonal condition sensitivity to isolate target‑specific memorization from generic fine‑tuning instability.

## Key Contributions  
- Founding the DCS framework as a post‑hoc, counterfactual sensitivity measure for detecting memorized content across modalities.  
- Introducing Dual‑Branch Conditional Sensitivity (DCS) that links observable displacement to unavailable retraining effect via influence‑function analysis and bounds it by privacy budget, curvature, dataset size, and perturbation step.  
- Defining a calibrated detection statistic that subtracts orthogonal condition sensitivity to separate target‑specific memorization from generic fine‑tuning instability.

## Methodology  
The authors treat copyright infringement evidence as a counterfactual conditional distribution shift: the model’s behavior under aligned conditions would change measurably if the protected target were included or removed from training. To operationalize this, they construct a learning branch and an unlearning branch around the deployed model, compute their displacement using influence‑function analysis, and bound the observable sensitivity by local curvature, the size of the training set, the privacy budget, and the perturbation step size. A calibrated detection statistic is then derived by subtracting the sensitivity measured under orthogonal conditions, allowing separation of target‑specific memorization from generic fine‑tuning instability.

## Results  
Experiments on ridge‑regularized linear regression, conditional diffusion models, autoregressive language models, and multimodal systems demonstrate that DCS yields higher detection scores when a protected dataset is memorized compared with generic fine‑tuning scenarios. Cross‑modal embedding divergence improves for target‑specific cases, while the calibrated statistic reduces false positives caused by style drift or public‑domain concepts. Quantitative comparisons show DCS outperforms similarity‑based metrics in distinguishing infringing from non‑infringing outputs across all tested modalities.

## Significance  
This work provides a principled, privacy‑aware metric for detecting copyright infringement that works uniformly across different models and modalities, moving beyond simple output similarity to capture the underlying counterfactual impact of protected data. It enables automated enforcement systems to reliably identify memorized content while respecting differential privacy constraints.

## Related Concepts  
Conditional differential privacy, influence functions, dual‑branch analysis, sensitivity bounds, calibration of detection statistics, cross‑modal representation divergence, memorization vs. fine‑tuning instability.
