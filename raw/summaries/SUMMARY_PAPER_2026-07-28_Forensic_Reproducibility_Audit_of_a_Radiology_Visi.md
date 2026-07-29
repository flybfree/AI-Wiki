---
title: Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact
url: http://arxiv.org/abs/2607.25589v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_11-19-38Z_ForensicReproducibilityAuditofaRadiologyVision_Lan.md
generated_at: 2026-07-28 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper conducts a forensic reproducibility audit of a chest‑radiograph vision‑language model benchmark, tracing how the intended protocol diverged from the released artifact. It finds that only 297 of 300 planned model‑prompt calls produced nonempty reports and that several critical artifacts—such as missing polarity inversion, truncated annotations, and mismatched dataset splits—skew statistical results.

## Key Takeaways
- 297 out of 300 model‑prompt calls yielded nonempty reports, indicating high call success but still leaving a small gap in data completeness.  
- Sixty Claude A/B calls were executed with the same C prompt across 30 studies representing only 28 patients, showing that dataset splits and patient representation are not preserved.  
- Four MONOCHROME1 images were rendered without required polarity inversion and five reports were truncated to 4000 characters, causing a change in Cochran's Q from 154.73 to 182.29.

## Context
Medical‑imaging AI benchmarks rely on the assumption that all artifacts remain consistent across runs, yet this paper demonstrates that many components—prompt bindings, DICOM rendering, label extraction, and release propagation—can vary without detection. This highlights a gap between documented protocols and actual reproducible outputs in clinical AI research.

## Implications
For researchers, industry stakeholders, and clinicians, the findings stress the need for machine‑verifiable controls over cohort definition, image rendering, prompt identity, call status, annotation provenance, and derived artifacts to ensure trustworthy performance claims. Without such safeguards, reported rankings and clinical claims remain unverified and potentially misleading.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25589v1)
