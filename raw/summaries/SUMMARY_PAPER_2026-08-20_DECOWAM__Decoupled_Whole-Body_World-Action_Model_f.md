---
title: DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation
url: http://arxiv.org/abs/2608.20114v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_14-44-11Z_DECOWAM_DecoupledWhole_BodyWorld_ActionModelforLeg.md
generated_at: 2026-08-20 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DECOWAM, a whole‑body world‑action model that separates camera ego‑motion from base and arm actions for mobile manipulation. On the ARMDOG dataset it outperforms FastWAM by reducing action prediction MSE by 21.7% while adding only 25.95 million trainable parameters.

## Key Takeaways
- DECOWAM uses a conditional interface to freeze a FastWAM backbone and train residual adapters, enabling precise separation of base‑velocity conditioning from arm‑latent adaptation.  
- The model achieves a 21.7% lower action MSE compared with the baseline, demonstrating efficient parameter‑efficient improvement through adversarial separation.  
- Across 79 closed‑loop trials DECOWAM shows higher whole‑body coordination and greater robustness to base displacement while maintaining comparable task completion rates.

## Context
Mobile manipulation demands models that account for how locomotion and arm motion jointly affect future observations, a challenge not fully addressed by fixed‑base world‑action frameworks. This work advances embodied AI by integrating real‑robot data and language labels into a factorized prediction pipeline.

## Implications
The findings suggest that embodiment‑aware factorization can be applied to other moving platforms, reducing the need for large adaptation sets in robotics research. Practitioners may adopt DECOWAM’s lightweight adapters to build more responsive mobile manipulators with improved visual and control coordination.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20114v1)
