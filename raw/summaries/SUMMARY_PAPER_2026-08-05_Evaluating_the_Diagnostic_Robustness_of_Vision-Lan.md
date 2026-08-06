---
title: Evaluating the Diagnostic Robustness of Vision-Language Models Under Visual and Textual Perturbations
url: http://arxiv.org/abs/2608.04885v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_14-09-55Z_EvaluatingtheDiagnosticRobustnessofVision_Language.md
generated_at: 2026-08-05 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates the diagnostic robustness of vision-language models using a histopathology‑validated brain MRI dataset. It tests four VLM families under evidence‑preserving perturbations such as slice reordering and label swapping, showing that high accuracy can hide reliability failures. The study finds prediction flips up to 48.9% after simple sequence reversals.

## Key Takeaways
- Presentation order stability is compromised: models produce different predictions in up to 48.9% of cases when anatomical slices are reordered while clinical evidence stays the same.
- Textual selection bias causes inconsistent diagnoses: label reordering triggers errors in up to 67.8% of cases despite identical visual inputs.
- Diagnostic overcommitment occurs: after removing expert‑annotated lesion slices, models generate categorical diagnoses in up to 76.1% of cases.

## Context
The paper contributes to the growing recognition that standard accuracy metrics are insufficient for safety‑critical AI systems where sequential or textual framing matters. By exposing hidden vulnerabilities, it aligns with efforts to develop more robust and interpretable multimodal models for medical imaging. The findings support a shift toward stability‑focused evaluation in clinical AI.

## Implications
For practitioners deploying VLM tools in hospitals, these results warn that reliance on aggregate accuracy may lead to unsafe deployments. The study calls for new metrics that capture sensitivity to presentation order and textual framing, guiding responsible model selection and validation protocols.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04885v1)
