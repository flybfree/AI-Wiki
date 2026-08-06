---
title: Canonical Joint Energy-Based Model on CIFAR-10: failure modes and practical indistinguishability of Predictor-Corrector and SGLD samplers
url: http://arxiv.org/abs/2608.05025v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_16-28-57Z_CanonicalJointEnergy_BasedModelonCIFAR_10_failurem.md
generated_at: 2026-08-05 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper reproduces the canonical joint energy‑based model on CIFAR‑10 and compares two stochastic samplers, predictor‑corrector (PC) and stochastic gradient Langevin dynamics (SGLD), across training, generation, and out‑of‑distribution detection. It finds that both samplers achieve similar reconstruction accuracy and OOD performance with no systematic advantage of PC over SGLD.

## Key Takeaways
- The canonical JEM reaches 92.88% test accuracy on WideResNet‑28‑10 but its buffer‑FID is higher than the baseline, indicating a trade‑off between classification and generation quality.
- Both PC and SGLD suffer from catastrophic late‑training divergence caused by the outlier‑buffer mechanism, producing run‑dependent SVHN OOD discrimination that cannot be distinguished by method alone.
- The absolute AUROC difference between samplers stays below 0.007 across ten checkpoint‑OOD pairs, suggesting practical indistinguishability and no clear theoretical benefit of PC.

## Context
Joint energy‑based models aim to fuse classification and generative modeling in a single network, offering a route to robust out‑of‑distribution detection without separate detectors. The canonical formulation has been widely used but its practical implementation remains unexplored beyond SGLD.

## Implications
For practitioners, the study reassures that alternative samplers like PC do not guarantee superior OOD performance and may be unnecessary complexity. It also highlights the importance of monitoring run‑dependent artifacts in energy‑based training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05025v1)
