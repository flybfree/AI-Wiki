---
title: C$^2$A: Coupling Spatial Evidence with Clinical Priors via Co-occurrence Aware Class Attention for Multi-Label Chest X-Ray Classification
url: http://arxiv.org/abs/2608.09774v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_16-02-05Z_C__2_A_CouplingSpatialEvidencewithClinicalPriorsvi.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces C$^2$A, a classification head that couples spatial evidence with clinical priors for multi‑label chest X‑ray diagnosis. By treating pooling as an expectation over learned per‑class attention maps and linking descriptors through a graph warm‑started from label co‑occurrence, the method improves performance on CheXpert to 0.895 macro‑mean AUROC. The gains are especially evident for highly co‑occurrent diseases such as Atelectasis.

## Key Takeaways
- C$^2$A replaces global pooling with per‑class spatial attention maps that preserve location information, allowing the model to focus on relevant regions of each disease.
- The learned graph warm‑started from empirical label co‑occurrence introduces a structured interaction between related findings without altering the original logits, acting as a bounded perturbation.
- A single residual message‑passing step enables evidence sharing among classes, resulting in a negligible overhead limited to one linear projection and a C×C edge matrix.

## Context
Multi‑label medical imaging classification remains challenging because lesions often co‑occur and global descriptors ignore their spatial relationships. Recent work has explored context gating or attention mechanisms, but most treat each class independently, missing the benefit of shared priors. This paper advances the field by integrating clinical knowledge directly into the model’s architecture.

## Implications
Clinicians can rely on a system that better understands where lesions appear and how they relate to one another, potentially reducing false negatives for co‑occurring conditions. For developers, C$^2$A offers a scalable way to incorporate prior knowledge with minimal computational cost, supporting deployment in real‑time clinical workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09774v1)
