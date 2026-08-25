---
title: Loss Landscape Features That Make Adam Stall: Definitions, Estimators, and the Preconditioned Hessian View
published: 2026-08-23T00:21:33Z
authors: Rodion Podorozhny
url: http://arxiv.org/abs/2608.22145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loss Landscape Features That Make Adam Stall: Definitions, Estimators, and the Preconditioned Hessian View

## Abstract
Across implicit-neural-representation (INR) architectures and analytic benchmarks we observe that a thoroughly tuned Adam (especially its learning rate (lr), e.g. in a hyperparameter sweep from $lr = 0.05$ to $10^{-8}$) can potentially reach a very low loss even on ill-conditioned loss landscape or converge at a plateau far above the loss attained by second-order methods. This report defines the measured metrics that help determine if Adam can mitigate the ill-conditioning on a given loss landscape. We provide the indicators by which each outcome is determined, that are: the condition number of the Hessian and of the Adam-preconditioned Hessian $D^{-1/2}HD^{-1/2}$ (with the derivation from Adam's update rule), the diagonal mass $ρ$ that distinguishes axis-aligned from cross-coupled ill-conditioning, the negative spectral mass estimated by stochastic Lanczos quadrature, and the gradient energy fractions over curvature bands, including the flat fraction that indicates the Adam stall. A worked out $2\times 2$ example and an illustration show the reasons why a diagonal preconditioning by Adam can remove axis-aligned ill-conditioning by rescaling and why it cannot do the same if the ill-conditioning is cross coupled. In addition, we present a case study of FINER image fitting architecture that goes over the whole loss landscape analysis framework: the fitting architecture description, reasons due to which its landscape stalls Adam at saddles, the measured PSNR values through our tuned baselines to the $120$--$134$\,dB results of the blockwise second order methods, the error maps behind those numbers, and description of the benefits such image fitting accuracy gives in practice.

## Metadata
- **Published**: 2026-08-23T00:21:33Z
- **Authors**: Rodion Podorozhny
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22145v1)