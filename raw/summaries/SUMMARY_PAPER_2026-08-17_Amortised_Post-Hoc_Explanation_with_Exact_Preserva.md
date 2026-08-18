---
title: Amortised Post-Hoc Explanation with Exact Preservation for Dynamic Graph Anomaly Detectors
url: http://arxiv.org/abs/2608.15559v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_06-10-40Z_AmortisedPost_HocExplanationwithExactPreservationf.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces X-StrGNN, a post‑hoc explanation module that adds dual attributions to the StrGNN anomaly detector. It provides structural and temporal attribution vectors while preserving detection performance exactly as measured by zero delta AUC, AP, or P@100. The method is lightweight at 0.66 ms per edge.

## Key Takeaways
- X‑StrGNN emits two multiplicative masks—structural and temporal—that together explain each flagged edge without altering the underlying model output.
- The dual attribution system achieves exact pass‑through: ΔAUC = 0.0000, ΔAP = 0.0000, ΔP@100 = 0.0000, confirming no loss in detection accuracy.
- Explanation cost is only 0.66 ms per edge, enabling full alarm list explanation within feasible time budgets.

## Context
Explainability for deep graph models remains a bottleneck because most detectors output only scores, limiting human trust and regulatory compliance. This work addresses that gap by delivering interpretable masks while preserving model fidelity, aligning with the need for auditable AI in high‑stakes domains.

## Implications
Practitioners can now generate transparent justifications for fraud or intrusion alerts without sacrificing performance, supporting responsible deployment of dynamic graph detectors. The low per‑edge cost makes real‑time explanation scalable across large alert lists, encouraging broader adoption of explainable anomaly detection systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15559v1)
