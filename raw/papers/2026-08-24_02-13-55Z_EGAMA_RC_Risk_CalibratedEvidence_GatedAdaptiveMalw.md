---
title: EGAMA-RC: Risk-Calibrated Evidence-Gated Adaptive Malware Analysis for Robust and Interpretable Memory-Forensic Triage
published: 2026-08-24T02:13:55Z
authors: Isaac Kofi Nti
url: http://arxiv.org/abs/2608.22721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EGAMA-RC: Risk-Calibrated Evidence-Gated Adaptive Malware Analysis for Robust and Interpretable Memory-Forensic Triage

## Abstract
Machine-learning malware detectors often achieve high clean-data accuracy, but operational triage also requires evidence about uncertainty, novelty, robustness, interpretability, latency, and review cost. This paper presents EGAMA-RC, a risk-calibrated evidence-gated framework for memory-forensic malware triage. Building on SHAP-guided feature refinement, EGAMA-RC combines dataset-specific refinement, model-pool evaluation, adversarial and open-family testing, novelty scoring, explanation-conditioned evidence, and runtime-aware routing. Low-risk samples are accepted automatically, while uncertain, high-risk, or potentially novel cases are routed to review, escalation, or novelty-aware handling. Across three malware datasets and a frozen multi-seed protocol, the selected hybrid gate accepts 93.12% of pooled samples with 99.86% accepted accuracy and a 0.136% false-accept rate. Novelty calibration reduces over-restrictive review behavior while preserving a low unsafe-accept profile. XGBoost provides lightweight fast-path inference with p50/p95 latency of 0.0054/0.0059 ms per sample. The results show that dependable malware analysis requires risk-calibrated routing, novelty awareness, and controlled analyst review, not classification accuracy alone.

## Metadata
- **Published**: 2026-08-24T02:13:55Z
- **Authors**: Isaac Kofi Nti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22721v1)