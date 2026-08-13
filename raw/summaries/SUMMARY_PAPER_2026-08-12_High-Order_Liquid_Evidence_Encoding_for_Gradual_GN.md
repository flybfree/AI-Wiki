---
title: High-Order Liquid Evidence Encoding for Gradual GNSS Spoofing Detection in Autonomous Driving
url: http://arxiv.org/abs/2608.11790v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_08-30-17Z_High_OrderLiquidEvidenceEncodingforGradualGNSSSpoo.md
generated_at: 2026-08-12 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a causal high‑order liquid evidence framework to detect gradual GNSS spoofing attacks in autonomous driving by modeling the evolution of GNSS‑motion inconsistency residuals. Experiments on three AV‑GPS subsets show the method achieves F1 scores of 0.9535 and 0.9777, outperforming other temporal models, especially on Dataset 3 where it identifies normal‑to‑attack transitions within four steps.

## Key Takeaways
- The framework constructs a physics‑guided residual that compares GNSS‑implied displacement with onboard motion‑derived displacement to capture spoofing cues.  
- It creates three evidence streams—residual level, first‑order variation, and second‑order variation—each processed by an adaptive liquid encoder tailored to the stream’s order.  
- The method predicts spoofing at window endpoints using only current and past observations without relying on static vehicle features.

## Context
This work advances AI detection of subtle sensor manipulation in safety‑critical systems like autonomous vehicles, where traditional anomaly detectors often miss gradual changes. By leveraging hierarchical evidence encoding, the approach aligns with broader efforts to integrate physics‑informed signals into machine learning pipelines for real‑time monitoring.

## Implications
For industry practitioners, the method offers a robust, low‑latency detection tool that can be embedded directly into vehicle perception stacks. Its high F1 scores suggest it could reduce false alarms while maintaining strong attack detection, supporting safer deployment of GNSS‑based autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11790v1)
