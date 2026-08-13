---
title: CT-$Δ$Bench: A Benchmark for Longitudinal 3D Medical Imaging Difference Reporting with Vision-Language Models
url: http://arxiv.org/abs/2608.11534v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_00-55-31Z_CT__Δ_Bench_ABenchmarkforLongitudinal3DMedicalImag.md
generated_at: 2026-08-12 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CT‑ΔBench, a benchmark for longitudinal 3D medical imaging difference reporting that requires models to compare two scans from the same patient and generate clinically meaningful reports. The authors develop change‑aware metrics and physician validation to assess temporal reasoning beyond simple text similarity. They also present DeltaMed, a baseline model trained on the new dataset.

## Key Takeaways
- CT‑ΔBench creates a patient‑level split of serial CT scans to prevent information leakage during evaluation.
- Change‑aware metrics are introduced to capture clinically relevant longitudinal changes rather than surface textual overlap.
- The study compares direct paired‑CT reasoning with an indirect two‑stage pipeline and validates the synthetic references using independent physicians.

## Context
Medical foundation models currently excel at single‑study image understanding but lack capability for temporal cross‑examination, which is essential for longitudinal disease monitoring. This work addresses that gap by focusing on the specific task of reporting interval changes between scans, a critical component in clinical decision making.

## Implications
The benchmark and evaluation framework provide a standardized way to measure how well models understand temporal medical data, guiding future research toward truly longitudinal foundation models. Practitioners can rely on these tools to assess model reliability for real‑world patient monitoring and treatment planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11534v1)
