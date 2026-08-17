---
title: PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization
published: 2026-08-13T21:50:07Z
authors: Ruogu Chen, Jie Han
url: http://arxiv.org/abs/2608.13790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization

## Abstract
Macro placement significantly affects a chip's post-route performance, power, and area (PPA). Most placement methods optimize half-perimeter wirelength (HPWL) as the primary objective. However, recent benchmarking shows a near-zero correlation between HPWL and post-route timing metrics such as the worst negative slack (WNS) and total negative slack (TNS). As a result, all six evaluated artificial intelligence (AI) placers degraded PPA relative to the hierarchical baseline. Recent efforts have tried to train cross-stage predictors to close this gap. However, existing methods focus on macro-only representations and use pre-route metrics as training labels. A label fidelity study of ten circuits at four design flow stages reveals that HPWL and pre-route timing poorly reflect final post-route timing rankings. In contrast, post-global-routing achieves the best balance between final timing fidelity and label generation cost-effectiveness. Based on this finding, PPAPlace is a timing-driven differentiable surrogate predicting post-route PPA from macro and standard-cell placements. The surrogate is a dual-stream predictor that combines graph attention over the chip netlist with spatial convolution over the placement grid. It is trained on post-global-routing labels. The predicted WNS and TNS gradients flow end-to-end back to cell coordinates. PPAPlace exploits these gradients in two ways: as a co-objective injected into an analytical placer's optimization loop (PPAPlace-CoOpt), and as a post-placement refinement step that adjusts macro positions via projected gradient descent (PPAPlace-Refine). On five ChiPBench test circuits excluded from training, PPAPlace improves average WNS and TNS by 22\% and 51\% over the hierarchical baseline while preserving power and routability, using the same predictor without test-circuit retraining. Code is available at https://github.com/ValleyC/PPAPlace.

## Metadata
- **Published**: 2026-08-13T21:50:07Z
- **Authors**: Ruogu Chen, Jie Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13790v1)