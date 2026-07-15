---
title: "Summary: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md"
date: 2026-05-05
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-05-07 23:04
Source: 2026-05-05_17-59-18Z_AClosed_FormAdaptive_LandmarkKernelforCertifiedPoi.md
Model: None

---


## Summary  
This paper introduces PALACE, a closed‑form adaptive‑landmark kernel that delivers certified point‑cloud and graph classification with provable guarantees. The method adapts landmark placement and bandwidth to the data while guaranteeing structural distortion bounds without gradient training. It combines a cover‑theoretic core with Mahalanobis margins to produce per‑prediction certificates.  

## Key Contributions  
- [Finding 1] Structural lower distortion bound λ(τ;ν) on Dₙ under cross‑diagram non‑interference, achieving a (D/L)² budget reduction over uniform grids when diagrams concentrate.  
- [Finding 2] Equal weights wₖ = K⁻¹/₂ maximize λ and farthest‑point‑sampling positions approximate the optimal k‑center covering radius using only training labels.  
- [Finding 3] Kernel‑RKHS classification rate O((k−1)√K/(γ√m_min)) with binary necessity threshold m = Ω(√K/γ), delivering a per‑prediction certificate in non‑asymptotic Pinelis and asymptotic Gaussian forms.  

## Methodology  
The authors adopt a cover‑theoretic framework where landmarks are placed via farthest‑point sampling, the kernel is defined adaptively on a bandwidth γ, and classification decisions rely on Mahalanobis margins derived from a reproducing‑kernel Hilbert space (RKHS). The cross‑diagram non‑interference condition ensures structural distortion bounds without requiring gradient descent.  

## Results  
Empirically PALACE matches Persformer (91.3 ± 1.0 % on Orbit5k) while outperforming all diagram‑based methods on COX2 and MUTAG, and is within 1 pp of ECP on DHFR. At 8× domain inflation the adaptive placement retains 94 % accuracy versus a uniform grid dropping to chance (≈25 %). The theoretical rate O((k−1)√K/(γ√m_min)) aligns with Le Cam lower bound.  

## Significance  
By delivering certified, non‑asymptotic guarantees and maintaining performance under heavy domain shift, PALACE advances robust, explainable classification for point clouds and graphs without reliance on expensive gradient‑based optimization.  

## Related Concepts  
- Landmark cover theory  
- RKHS (Reproducing Kernel Hilbert Space)  
- Mahalanobis margin  
- Cover‑theoretic distortion bounds  
- Farthest‑point sampling

[[A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification]]