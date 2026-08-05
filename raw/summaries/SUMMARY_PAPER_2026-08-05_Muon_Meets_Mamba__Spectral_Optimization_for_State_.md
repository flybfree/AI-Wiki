---
title: Muon Meets Mamba: Spectral Optimization for State Space Models
url: http://arxiv.org/abs/2608.03941v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-10-47Z_MuonMeetsMamba_SpectralOptimizationforStateSpaceMo.md
generated_at: 2026-08-05 01:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a controlled comparison between Muon and AdamW optimizers on the Mamba‑2 130M model, focusing only on which weight groups receive Muon’s Newton‑Schulz updates. The results show that applying Muon to the output projection alone yields significant token efficiency gains without affecting other components.

## Key Takeaways
- Muon improves performance when it is applied solely to the output projection, outperforming AdamW and even beating Muon on input or both projections combined.  
- The benefit is primarily a reduction in token usage rather than a change in model accuracy, persisting across two corpora and token budgets beyond compute‑optimal points.  
- Lowering the condition number of the targeted projection drives the improvement, but conditioning alone does not explain the observed gain.

## Context
State‑space models like Mamba have gained attention for their efficiency, yet most optimization research concentrates on Transformers. This study fills a gap by evaluating Muon—a method known from Transformer training—within this less explored architecture.

## Implications
Practitioners can selectively apply Muon to specific weight groups to achieve faster inference without retraining the entire model. The insight highlights that optimizer choice may be as impactful as architectural design in optimizing state‑space models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03941v1)
