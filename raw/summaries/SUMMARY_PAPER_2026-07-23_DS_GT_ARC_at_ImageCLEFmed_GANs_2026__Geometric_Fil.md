---
title: DS@GT ARC at ImageCLEFmed GANs 2026: Geometric Filtering for Privacy-Preserving CT Slice Generation
url: http://arxiv.org/abs/2607.20692v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_19-46-21Z_DS_GTARCatImageCLEFmedGANs2026_GeometricFilteringf.md
generated_at: 2026-07-23 22:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a privacy‑preserving framework for generating synthetic lung CT slices that meets the ImageCLEFmed GANs 2026 challenge. By integrating Optimal Transport Conditional Flow Matching with geometric filtering, it achieves a Privacy Preservation Score of 0.549 and visual fidelity measured by an FID of 0.3290.

## Key Takeaways
- The framework combines Optimal Transport Conditional Flow Matching with privacy‑oriented training to produce synthetic slices while limiting nearest‑neighbor memorization.  
- A post‑generation “Supervisor” pipeline that uses autoencoder embeddings, Determinantal Point Processes, and Stein Kernel Thinning cuts membership‑inference leakage further.  
- Despite these measures, patient re‑identification scores remain high, indicating that deeper anatomical identity can still be inferred.

## Context
Medical image generation must balance clinical realism with strict privacy protection, a challenge amplified by the rise of GANs in medical imaging challenges. This work contributes to that dialogue by providing quantitative metrics for both visual quality and privacy leakage.

## Implications
For healthcare AI developers, the study shows that effective privacy safeguards require more than simple copy‑prevention; they must address latent patient‑specific patterns. The findings influence industry practice toward stronger privacy architectures in synthetic medical data generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20692v1)
