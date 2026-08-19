---
title: Structured Driving-State Narratives for Small Language Model-Based GNSS Spoofing Detection
url: http://arxiv.org/abs/2608.17092v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_19-59-20Z_StructuredDriving_StateNarrativesforSmallLanguageM.md
generated_at: 2026-08-18 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a small language model based framework that detects and classifies GNSS spoofing attacks by converting independent driving states into structured narratives. It compares this approach with large language models on the same data and evaluates performance across five attack classes. The results show high accuracy, precision, recall and F1 scores while demonstrating lower computational demands.

## Key Takeaways
- The SLM framework achieves an average accuracy of 96.99% which is comparable to LLMs fine‑tuned on identical data.
- Computational efficiency is highlighted: the model requires less GPU memory and inference latency than LLMs during both training and deployment.
- Field testing in a geographically distinct location confirms that the approach works reliably outside the original test set.

## Context
Autonomous vehicles rely heavily on GNSS for navigation, making spoofing detection critical. Recent advances in language models have been applied to sensor data fusion tasks, but their resource intensity limits real‑time use in vehicles. This work bridges that gap by showing a lightweight model can match performance while fitting into constrained hardware.

## Implications
For the industry, this framework enables real‑time spoof detection on edge devices without sacrificing accuracy. Practitioners can integrate it into vehicle computing platforms to improve safety and trust in autonomous navigation systems. The approach also offers a template for applying small language models to other sensor anomaly detection problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17092v1)
