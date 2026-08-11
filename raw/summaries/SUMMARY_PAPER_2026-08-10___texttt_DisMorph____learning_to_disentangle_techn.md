---
title: $\texttt{DisMorph}$: learning to disentangle technical distortions from true biological change
url: http://arxiv.org/abs/2608.08173v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_15-04-55Z_texttt_DisMorph___learningtodisentangletechnicaldi.md
generated_at: 2026-08-10 22:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DisMorph, a registration framework that separates MRI‑induced geometric distortions from true biological changes in longitudinal scans. By training on synthetic data with explicit technical and anatomical components, the method predicts two separate deformation fields and outperforms conventional approaches both in simulated and real datasets.

## Key Takeaways
- The framework disentangles gradient non-linearity distortion from anatomical change by predicting two independent dense deformations during training.
- On image pairs affected only by GNL distortion, most geometric differences are assigned to the technical field, showing high specificity without biological signal.
- In longitudinal Alzheimer’s disease data, DisMorph accurately detects true structural atrophy while identifying residual scanner‑specific errors left after standard correction.

## Context
This work advances AI‑driven neuroimaging analysis by providing a principled method for separating confounded measurement artifacts from genuine pathology. It leverages generative models to create supervision that is rare in clinical pipelines, highlighting the potential of synthetic data to improve robustness across heterogeneous acquisition protocols.

## Implications
Clinicians and researchers can rely on more accurate longitudinal morphometric measurements even when scanner settings vary, reducing bias in disease progression assessments. The approach also offers a template for future AI tools that must handle both biological signals and technical noise in medical imaging.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08173v1)
