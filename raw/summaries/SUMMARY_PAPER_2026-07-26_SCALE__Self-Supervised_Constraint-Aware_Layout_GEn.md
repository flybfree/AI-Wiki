---
title: SCALE: Self-Supervised Constraint-Aware Layout GEneration for Local P&R DRV Fixing at Advanced Nodes
url: http://arxiv.org/abs/2607.21850v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_22-38-04Z_SCALE_Self_SupervisedConstraint_AwareLayoutGEnerat.md
generated_at: 2026-07-26 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SCALE a self‑supervised framework that generates local place‑and‑route design rule violation pairs from advanced node layouts without explicit labels. By masking polygons in multi‑layer images and reconstructing them with a fine‑tuned language model guided by natural‑language constraints the system produces DRC‑annotated repair variants. On 100 real sub‑2nm cases it improves solve rates by up to 25 percent reaching near perfect performance.

## Key Takeaways
- SCALE uses self‑supervised layout generation to create violation pairs from BEOL context alone, eliminating the need for labeled DRC data.
- The language model reconstructs masked polygons using high‑temperature sampling and natural‑language rule constraints to explore diverse repair options.
- On real sub‑2nm layouts the approach raises solve rates by 12–25 percent up to 97 percent.

## Context
The rapid push toward sub‑2nm semiconductor nodes creates a surge in complex DRC violations that traditional tools struggle to resolve. General‑purpose vision models lack fine geometric reasoning and foundry‑specific rule knowledge, limiting their utility for local repair tasks. This work bridges the gap by applying language modeling to visual layout understanding.

## Implications
Practitioners can integrate SCALE into automated signoff pipelines to reduce manual DRC fixing effort. The framework’s modular design allows adaptation to new node technologies and foundry rules, offering a scalable solution for next‑generation chiplet and 3D stacking designs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21850v1)
