---
title: GAUGE: Granularity-Adaptive Counterfactual Gating of Evidence for Incomplete Multimodal Classification
url: http://arxiv.org/abs/2608.05608v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_05-07-14Z_GAUGE_Granularity_AdaptiveCounterfactualGatingofEv.md
generated_at: 2026-08-06 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
GAUGE introduces a lightweight counterfactual gating framework for incomplete multimodal classification that outperforms strong baselines on six benchmarks. The method is lightweight and requires only a single additional forward-backward pass to compute its predictions.  

## Key Takeaways
- GAUGE imputes missing modalities with a frozen imputer and encodes both observed and recovered inputs as fine-grained evidence units.  
- The framework scores the counterfactual effect via prediction‑aware Taylor evidence scores computed in one forward‑backward pass, mapping them to continuous gates that modulate attention logits.  
- A theoretical analysis of the Taylor remainder shows how the first‑order approximation error relates to the exact counterfactual effect.  

## Context
Incomplete multimodal inputs are common in real‑world scenarios, yet existing methods operate at a coarse modality level, leading to unreliable predictions. GAUGE addresses this limitation by operating at a fine‑grained evidence level without modifying the backbone architecture.  

## Implications
This work enables more robust classification systems that can handle data gaps without architectural changes, offering scalable solutions for industry applications where input completeness is uncertain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05608v1)
