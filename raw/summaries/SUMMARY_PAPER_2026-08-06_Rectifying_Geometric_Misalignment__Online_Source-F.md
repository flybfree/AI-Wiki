---
title: Rectifying Geometric Misalignment: Online Source-Free Adaptation for Class-Imbalanced EEG
url: http://arxiv.org/abs/2608.05315v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_18-17-59Z_RectifyingGeometricMisalignment_OnlineSource_FreeA.md
generated_at: 2026-08-06 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OSPDIM, an online source‑free unsupervised domain adaptation method for class‑imbalanced EEG data on a Riemannian manifold. It corrects geometric misalignment caused by label shifts by embedding a bias parameter into the tangent space mapping and optimizing it through information maximization. Simulations and experiments show that OSPDIM outperforms standard Riemannian alignment techniques, especially when data streams have severe class imbalance.

## Key Takeaways
- OSPDIM adds a manifold‑constrained bias term to the tangent space mapping to counteract geometric skew introduced by imbalanced label distributions.
- The bias is estimated online via information maximization rather than relying on offline batch statistics.
- Experiments demonstrate that OSPDIM significantly improves adaptation performance compared with baseline Riemannian methods such as RCT.

## Context
Unsupervised domain adaptation remains a key challenge for brain‑computer interfaces because EEG signals vary across subjects and sessions. Traditional alignment techniques assume balanced class priors, which breaks down when label shifts occur in real time. This paper addresses that limitation by designing an online framework that continuously adapts to dynamic data distributions.

## Implications
For BCI developers, OSPDIM provides a plug‑and‑play solution that maintains high accuracy despite label imbalance without requiring extensive offline calibration. The method’s robustness could lower deployment costs and enable seamless integration across multiple users and clinical settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05315v1)
