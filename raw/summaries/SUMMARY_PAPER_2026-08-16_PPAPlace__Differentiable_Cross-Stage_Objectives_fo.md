---
title: PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization
url: http://arxiv.org/abs/2608.13790v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_21-50-07Z_PPAPlace_DifferentiableCross_StageObjectivesforChi.md
generated_at: 2026-08-16 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
PPAPlace introduces a timing‑driven differentiable surrogate that predicts post‑route performance from macro and standard‑cell placements, addressing the poor correlation between half‑perimeter wirelength and final timing metrics. The method is trained on post‑global‑routing labels and achieves significant gains in worst negative slack (WNS) and total negative slack (TNS) without retraining test circuits.

## Key Takeaways
- HPWL and pre‑route timing poorly reflect final post‑route timing rankings, as revealed by a label fidelity study of ten circuits at four design flow stages.  
- PPAPlace uses post‑global‑routing labels to train a dual‑stream predictor that combines graph attention over the netlist with spatial convolution over the placement grid.  
- The surrogate’s gradients flow end‑to‑end back to cell coordinates, enabling both co‑objective injection into an analytical placer and refinement via projected gradient descent.

## Context
Placement optimization has long relied on half‑perimeter wirelength as a primary objective, yet this metric often fails to predict real‑world performance. Recent AI placers that optimize only macro placement degrade post‑route PPA, highlighting the need for models that incorporate accurate timing labels and can propagate gradients through the design flow.

## Implications
This work demonstrates that end‑to‑end differentiable training can improve chip performance without costly retraining of test circuits, offering a practical path to higher WNS and TNS. Practitioners can integrate PPAPlace into existing flows, reducing development time and enhancing overall chip efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13790v1)
