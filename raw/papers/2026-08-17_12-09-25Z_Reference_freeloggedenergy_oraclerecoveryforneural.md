---
title: Reference-free logged energy-oracle recovery for neural approximations of symmetric coercive variational problems: conforming Riesz reconstruction and archive-level selection
published: 2026-08-17T12:09:25Z
authors: Karim Bounja, Lahcen Laayouni, Boujemaa Achchab, Abdeljalil Sakat
url: http://arxiv.org/abs/2608.16473v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reference-free logged energy-oracle recovery for neural approximations of symmetric coercive variational problems: conforming Riesz reconstruction and archive-level selection

## Abstract
Neural PDE training yields a finite checkpoint archive, yet its logged energy errors are inaccessible without the exact solution, while loss-based selection does not necessarily recover the logged energy oracle. For admissible neural approximations of symmetric coercive variational problems, we introduce a reference-free selection rule based on minimizing a computable conforming Riesz monitor. The exact residual-energy identity and conforming projection make the monitor an unconditional lower bound converging monotonically to each logged energy error under nested conforming refinement; under saturation, hierarchical enrichment yields a computable upper estimate and hence a lower-upper bracket. A key finding is that archive selection is order-sensitive: unresolved checkpoint-dependent components can reverse the oracle-non-oracle ranking at finite resolution, so checkpointwise recovery alone is insufficient. For finite archives, we prove uniform recovery, yielding convergence to the logged-oracle error and, without saturation, logged-oracle selection at sufficiently fine auxiliary resolution. Under saturation, the bracket gives a computable near-oracle bound and certifies unique logged-oracle selection upon interval separation. We also bound logging-resolution loss and certify oracle inclusion over prescribed comparison trajectories. The resulting criterion replaces inaccessible exact-error minimization by computable, training-independent post-training selection on the intrinsic energy-error scale, requiring only the computed candidates and the variational problem. Experiments on diffusion and elasticity, including a non-manufactured perforated plate, demonstrate energy-scale calibration, oracle-level selection, and modest post-processing cost.

## Metadata
- **Published**: 2026-08-17T12:09:25Z
- **Authors**: Karim Bounja, Lahcen Laayouni, Boujemaa Achchab, Abdeljalil Sakat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16473v1)