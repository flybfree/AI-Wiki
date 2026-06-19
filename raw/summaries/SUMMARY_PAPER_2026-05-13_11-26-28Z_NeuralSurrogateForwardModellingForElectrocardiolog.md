---

title: Neural Surrogate Forward Modelling For Electrocardiology Without Explicit Intracellular Conductivity Tensor
url: http://arxiv.org/abs/2605.13366v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_11-26-28Z_NeuralSurrogateForwardModellingForElectrocardiolog.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces a deep learning model that predicts far‑field electrocardiograms from left atrial intracellular potentials without requiring explicit intracellular conductivity tensors at inference time. The model was trained on data from 74 subjects and achieved an R2 of 0.949 ± 0.037, demonstrating strong predictive performance.

## Key Takeaways
- The neural surrogate learns a direct mapping between intracellular electrical potentials and ECG signals, eliminating the need to explicitly input conductivity tensors during prediction.
- Despite limited training data (only 74 subjects), the model reaches an R2 of 0.949 ± 0.037, indicating high explanatory power for forward modelling.
- The approach reduces structural uncertainty in non‑invasive AF assessment by providing a reliable surrogate that does not depend on unmeasurable tissue properties.

## Context
Current cardiac electrophysiology relies heavily on physics‑based models that require detailed intracellular conductivity tensors, which are difficult to obtain clinically. Deep learning offers an alternative by learning complex mappings from observable potentials, but such approaches often need large datasets and extensive validation.

## Implications
This work could streamline clinical assessment of atrial fibrillation by enabling rapid, accurate forward modelling without invasive measurements. Practitioners may integrate the model into existing ECG pipelines, improving diagnostic confidence and reducing reliance on uncertain structural assumptions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13366v1)
