---
title: Distribution-free false-alarm calibration and chance-corrected spatial evaluation for industrial anomaly detection
url: http://arxiv.org/abs/2608.15090v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_07-21-05Z_Distribution_freefalse_alarmcalibrationandchance_c.md
generated_at: 2026-08-17 21:39
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method for industrial visual inspection that focuses on false‑alarm calibration without relying on the AUROC or raw mask overlap. By using a distribution‑free upper tolerance threshold and a paired‑minus‑crossed spatial test, the authors quantify spatial evidence lift relative to chance. The study shows significant lifts only for one detector modality, supporting calibrated performance metrics alongside traditional evaluation.

## Key Takeaways
- The paired‑minus‑crossed test yields spatial evidence lift values of 0.259 (95 % CI 0.159–0.347) for DINOv2‑ASM, indicating a statistically significant improvement over chance overlap.
- Calibration confidence is limited: a 95 % distribution‑free claim holds only at false‑positive rates ≥ 1.98 %, requiring 299 normals for a 1 % target rate.
- Crossed masks restricted to the same defect class still produce lifts of 0.185 (WRN50) and 0.210 (ViT‑B/16), confirming consistent spatial evidence.

## Context
The work addresses a longstanding gap in industrial anomaly detection where performance is measured without correcting for false alarms or chance overlap, leading to misleading AUROC scores. By integrating distribution‑free thresholds with spatial tests, the approach aligns evaluation with real‑world inspection constraints and improves interpretability of detector behavior across modalities.

## Implications
Practitioners can now report calibrated operating‑point metrics that reflect both sensitivity and specificity, reducing overestimation caused by recurrent defects or mask geometry. This framework supports more reliable model selection and deployment in high‑stakes manufacturing environments where false alarms are costly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15090v1)
