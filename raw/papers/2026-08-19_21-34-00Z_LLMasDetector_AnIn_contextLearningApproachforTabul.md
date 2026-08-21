---
title: LLM as Detector: An In-context Learning Approach for Tabular Anomaly Detection
published: 2026-08-19T21:34:00Z
authors: Tu Anh Hoang Nguyen, Dang Nguyen, Thuc Duy Le, Trung Le, Sunil Gupta
url: http://arxiv.org/abs/2608.19463v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM as Detector: An In-context Learning Approach for Tabular Anomaly Detection

## Abstract
Anomaly detection in tabular data is challenging because abnormal samples often arise as violations of cross-feature dependencies rather than simple marginal deviations. Existing detectors rely on geometric or reconstruction signals, while prior LLM-based approaches mainly fine-tune LLMs with normal samples or generate synthetic anomalies. We propose LLM-Detector, a framework that utilizes the in-context learning capacity of LLMs for structured, prompt-conditioned scoring synthesis, enabling LLMs to derive anomaly detection logic from structured normal-state knowledge. Specifically, normal training data are converted into statistical summaries, causal dependencies, and distilled prototypes that are organized into a prompt for code generation. The resulting scoring engine evaluates statistical deviation, structural inconsistency, and density-based abnormality then computes an anomaly score for each test sample. We evaluate LLM-Detector on 24 tabular datasets, comparing against 15 SOTA baselines. Results show consistent improvements across both mixed-type and continuous-only settings. Moreover, this design eliminates the need for LLM fine-tuning or neural network training, reducing computational cost and enabling practical anomaly detection in real-world tabular systems.

## Metadata
- **Published**: 2026-08-19T21:34:00Z
- **Authors**: Tu Anh Hoang Nguyen, Dang Nguyen, Thuc Duy Le, Trung Le, Sunil Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19463v1)