---
title: Self-supervision drives representational convergence in medical foundation models more than clinical supervision
url: http://arxiv.org/abs/2607.20274v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_15-25-05Z_Self_supervisiondrivesrepresentationalconvergencei.md
generated_at: 2026-07-23 22:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether medical foundation models from different groups converge on shared representations and how that convergence is driven. It finds modest but above‑random alignment among self‑supervised encoders, not due to clinical supervision or model size, and demonstrates limited utility for radiologist judgments.

## Key Takeaways
- Matched self‑supervised encoders achieve 40.4% similarity on chest radiographs, higher than label‑supervised (21.1%) or image‑text (3.3%).  
- The convergence is modest, does not increase with model size (Spearman ρ=0.302, p=0.223), and remains below radiologist‑based judgments.  
- A linear classifier retains ~85% of within‑encoder performance across five hospitals, showing limited interoperability despite shared geometry.

## Context
Medical image encoders are often assumed interchangeable because large datasets and clinical supervision concentrate their outputs onto a common structure. However, prior work rarely isolates the objective that drives such alignment or assesses its clinical relevance beyond simple similarity metrics.

## Implications
Designing medical foundation models should prioritize the self‑supervised objectives that produce measurable cross‑encoder performance rather than relying on scale or clinical labels. Practitioners must validate shared representations against patient subgroups and radiologist assessments to ensure genuine interoperability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20274v1)
