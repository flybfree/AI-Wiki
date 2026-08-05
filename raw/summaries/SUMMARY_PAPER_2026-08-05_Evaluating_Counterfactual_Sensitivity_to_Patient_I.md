---
title: Evaluating Counterfactual Sensitivity to Patient Information in Medication-Safety Reasoning
url: http://arxiv.org/abs/2608.03028v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_02-17-16Z_EvaluatingCounterfactualSensitivitytoPatientInform.md
generated_at: 2026-08-05 01:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MedPIC‑Bench to evaluate how well medication‑safety models use patient information when applying rules under counterfactual conditions. Across 28 models, accuracy on these questions falls from 63.6 % to 45.1 %, indicating a systematic weakness in conditional reasoning.

## Key Takeaways
- Model accuracy drops from 63.6 % to 45.1 % when patient information is altered, showing reduced counterfactual performance.  
- Models excel only when a patient attribute directly signals a known contraindication but falter when the information narrows or withdraws a safety warning.  
- Model rationales often mention the changed patient data yet still produce the original safety judgment.

## Context
Current medical AI benchmarks focus on static, rule‑following tasks and ignore whether models adapt to altered patient contexts. This gap limits trust in systems that must dynamically apply safety rules based on individual health profiles.

## Implications
Measuring conditional rule application is essential for reliable clinical decision support. The findings warn that relying solely on overall accuracy can mask failures in patient‑specific scenarios, urging developers to prioritize counterfactual robustness in medical AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03028v1)
