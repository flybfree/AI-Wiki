---
title: Wiener Representation Filtering for VLM Hallucination Suppression
url: http://arxiv.org/abs/2608.08167v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_14-51-17Z_WienerRepresentationFilteringforVLMHallucinationSu.md
generated_at: 2026-08-10 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a training-free post‑hoc representation filtering technique that reduces hallucinations in vision‑language models by editing the language backbone’s hidden states. It estimates covariance between truthful and hallucinated representations offline using only forward passes, then applies a Wiener‑type correction to selected feed‑forward layers at inference time without changing model speed.

## Key Takeaways
- The method uses a single offline calibration on paired data to compute covariance structures that define the Wiener estimator for each hidden state.  
- It performs an eigendecomposition to produce mode‑wise attenuation, ensuring continuous response to estimation noise while preserving stability.  
- Corrections are applied once to feed‑forward output projections of deeper layers, leaving inference unchanged and fast.

## Context
Vision‑language models generate useful captions but frequently hallucinate details not present in the image, a problem that limits trustworthiness and downstream applications. Current solutions often require fine‑tuning or extra compute, which is costly for deployment.

## Implications
This approach offers a lightweight, scalable fix that can be integrated into existing VLM pipelines without retraining, making it attractive for industry use where model updates are expensive. It demonstrates broad applicability across diverse models and tasks, suggesting a new paradigm of representation‑level hallucination suppression.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08167v1)
