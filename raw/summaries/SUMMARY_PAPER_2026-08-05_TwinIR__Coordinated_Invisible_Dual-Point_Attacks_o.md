---
title: TwinIR: Coordinated Invisible Dual-Point Attacks on Online HD Map Construction
url: http://arxiv.org/abs/2608.04453v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_05-08-28Z_TwinIR_CoordinatedInvisibleDual_PointAttacksonOnli.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TwinIR, a coordinated invisible dual-point attack that reduces the accuracy of online HD map construction by exploiting compensating geometric cues. Experiments on nuScenes show significant drops in mAP and increases in unsafe trajectories while keeping attacks visually hidden. The method achieves up to 8.96% mAP reduction under RSA.

## Key Takeaways
- TwinIR jointly optimizes attack effectiveness and point sparsity, selecting the minimum number of points needed to suppress compensating geometric cues from surrounding boundaries.
- It models camera responses to near-infrared illumination and maps optimized attack points to feasible physical placements, producing interference with minimal visible-spectrum changes.
- The attacks are validated on a real-world testbed AV, inducing road straightening and early-turn deformations while remaining inconspicuous in full-color views.

## Context
Online HD map construction is essential for autonomous driving safety and efficiency. Current attack methods often require many points or cause large visual artifacts, limiting practical deployment. TwinIR addresses these limitations by integrating physics‑aware optimization into the attack pipeline.

## Implications
This work demonstrates that subtle, invisible perturbations can degrade perception models without obvious signs, raising concerns about trust in AI systems. Practitioners must consider such attacks when evaluating robustness and may need to incorporate multi‑spectral defenses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04453v1)
