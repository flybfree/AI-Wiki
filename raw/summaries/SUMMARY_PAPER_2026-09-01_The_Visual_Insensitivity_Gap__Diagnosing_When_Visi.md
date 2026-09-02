---
title: The Visual Insensitivity Gap: Diagnosing When Vision-Language Models Fail to Use Visual Evidence
url: http://arxiv.org/abs/2609.00868v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_08-01-57Z_TheVisualInsensitivityGap_DiagnosingWhenVision_Lan.md
generated_at: 2026-09-01 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why vision-language models sometimes ignore visual evidence and instead rely on language cues alone. It introduces the Visual Insensitivity Gap, showing that 40% to 97% of multimodal samples are insensitive to visual perturbations. The authors quantify this with a per‑sample Visual Sensitivity Index (VSI) that ranks samples as visually or linguistically dependent.

## Key Takeaways
- A linear probe on each model's vision tower can distinguish perturbed from clean images at 0.72–0.79 accuracy, yet the model’s argmax token changes only 2% to 11% of those same samples.
- The VSI gap is a property of individual samples rather than of models, with Spearman rank correlation across models of +0.40 and p < 10⁻³.
- Mapping VSI reveals two regimes: multi‑choice reasoning on capable VLMs yields AUROC 0.85–0.87, while factuality tasks are weak because softmax confidence already indicates correct answers.

## Context
Vision-language models are widely used for multimodal tasks and are typically judged by aggregate accuracy that assumes visual input is utilized. Recent work has highlighted that many models may not actually attend to the image when answering questions. The Visual Insensitivity Gap provides a finer‑grained diagnostic that separates sample‑level failures from model‑level limitations.

## Implications
Recognizing samples where vision is ignored can improve ensemble strategies by conditioning on VSI rather than defaulting to abstention. Practitioners should treat VSI as a sample‑intrinsic signal, not a universal best abstention cue, to avoid over‑relying on visual evidence in multimodal applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00868v1)
