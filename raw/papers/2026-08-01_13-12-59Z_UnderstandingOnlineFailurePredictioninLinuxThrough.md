---
title: Understanding Online Failure Prediction in Linux Through Complementary Multi-View Explainability
published: 2026-08-01T13:12:59Z
authors: Diogo Dória, João R. Campos
url: http://arxiv.org/abs/2608.00651v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Online Failure Prediction in Linux Through Complementary Multi-View Explainability

## Abstract
Accurate Online Failure Prediction (OFP) has been shown to be feasible in Operating Systems (OSs) settings, but prediction alone is not sufficient for practical adoption. Without diagnostic insight, operators have limited basis to trust alerts or decide how to respond. Moreover, even when predictive accuracy is high, it is often unclear whether models are capturing meaningful failure processes or merely exploiting workload-specific noise and incidental correlations in telemetry. This paper reports a practical experience building and evaluating an explainable OFP pipeline for Linux OSs. We combine consensus-based feature selection for detection with temporal onset analysis, subsystemlevel causal analysis, and complementary diagnostic mechanisms to support failure interpretation. Evaluated under strict crossworkload conditions with frozen training artifacts, it achieved 91-94% detection on unseen workloads without retraining, while maintaining false alarm rates below 1%. However, failure mode diagnosis proved substantially more sensitive to workload shift, and several diagnostics mechanisms showed limited effectiveness for specific failure types. Our experience highlights three main lessons: i) detection generalizes more robustly than diagnosis across workload changes; ii) early-warning capability depends strongly on the failure mode, ranging from 38 to 215 seconds in our study; and iii) unseen failure modes are not reliably diagnosable from related training modes alone, providing 0% accuracy under Leave-One-Mode-Out (LOMO) evaluation. Taken together, these results show the value of complementary explainability mechanisms for interpreting accurate failure predictions, revealing when predictive signals reflect transferable failure structure and when diagnostic generalization breaks down under workload variation.

## Metadata
- **Published**: 2026-08-01T13:12:59Z
- **Authors**: Diogo Dória, João R. Campos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00651v1)