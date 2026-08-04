---
title: Beyond Static Anchors: Bounded Prototype Conditioning for Language-Free Medical Anomaly Detection
url: http://arxiv.org/abs/2608.00442v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_04-46-55Z_BeyondStaticAnchors_BoundedPrototypeConditioningfo.md
generated_at: 2026-08-03 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReCAP, a language‑free framework for medical anomaly detection that replaces static CLIP anchors with input‑conditioned visual prototypes. It achieves state‑of‑the‑art performance on zero‑shot and few‑shot benchmarks while cutting inference latency by over 70%.

## Key Takeaways
- ReCAP uses bounded gated modulation to re‑center normal and abnormal prototypes per image, providing query‑adaptive scoring without text prompts.
- A non‑parametric memory stores instance‑level target‑domain variation for few‑shot settings, complementing the conditional prototype branch.
- The method attains the best image‑level AUROC across six medical benchmarks in zero‑shot and 23 of 24 few‑shot scenarios.

## Context
Medical anomaly detection struggles with limited supervision and cross‑domain generalization. Traditional CLIP approaches rely on static text or visual tokens that do not adapt to new organs, limiting applicability. This work moves toward dynamic, image‑driven representations that can handle unseen targets.

## Implications
Clinicians benefit from faster, more accurate anomaly scores without needing additional annotations. The framework’s low latency and robustness make it suitable for real‑time deployment in hospitals, advancing AI‑assisted diagnostics across diverse imaging modalities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00442v1)
