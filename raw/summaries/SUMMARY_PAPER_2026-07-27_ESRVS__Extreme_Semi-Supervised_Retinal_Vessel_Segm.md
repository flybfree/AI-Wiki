---
title: ESRVS: Extreme Semi-Supervised Retinal Vessel Segmentation with a Single Annotated Image
url: http://arxiv.org/abs/2607.24453v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_13-57-07Z_ESRVS_ExtremeSemi_SupervisedRetinalVesselSegmentat.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ESRVS, a method for retinal vessel segmentation that learns from only one manually annotated image and a large pool of unlabeled images. By leveraging target‑domain‑adapted DINOv3 features, constructing multi‑granular vessel prototypes, and applying physics‑inspired priors, ESRVS generates pseudo‑labels that are refined through weighted training and adversarial refinement. The approach outperforms existing semi‑supervised methods on eight public datasets, achieving the best Dice and clDice scores among them while using only a tiny fraction of labeled data.

## Key Takeaways
- ESRVS selects a single representative reference image for manual annotation and transfers vessel cues to unlabeled images using target‑domain‑adapted DINOv3 features.  
- The method builds a multi‑granular vessel prototype, combines prototype similarity maps with a physics‑inspired prior, and refines pseudo‑labels via weighted training and adversarial refinement.  
- Across eight datasets ESRVS reaches the highest Dice and clDice scores among semi‑supervised methods that use only 10–20% labeled data, while Mask2Former retains high performance comparable to fully supervised baselines.

## Context
This work addresses a critical bottleneck in medical imaging: the high cost of obtaining dense expert annotations. By demonstrating that foundation‑model label propagation can achieve state‑of‑the‑art results with minimal supervision, ESRVS aligns with broader trends toward leveraging large pre‑trained models for efficient downstream tasks.

## Implications
For clinicians and researchers, ESRVS offers a practical pathway to deploy high‑quality vessel segmentation tools in resource‑constrained settings where labeling is expensive. Practitioners can adopt this approach to reduce annotation overhead while maintaining diagnostic accuracy, potentially accelerating the integration of AI‑driven retinal analysis into clinical workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24453v1)
