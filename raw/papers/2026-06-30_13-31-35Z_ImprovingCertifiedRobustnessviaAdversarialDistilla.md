---
title: Improving Certified Robustness via Adversarial Distillation
published: 2026-06-30T13:31:35Z
authors: Matteo Melis, Jesus Martinez Del Rincon, Vishal Sharma
url: http://arxiv.org/abs/2606.31653v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Certified Robustness via Adversarial Distillation

## Abstract
Certified training aims to produce models whose predictions can be formally verified against adversarial perturbations, typically by optimising upper bounds on the worst-case loss over an allowed perturbation set. For neural networks, certified training methods based purely on tight relaxation bounds produce networks that are amenable to certification, but sacrifice standard accuracy. Conversely, adversarial training often yields stronger empirical robustness and standard accuracy, but the resulting models are generally difficult to certify with neural network verifiers. Recently, the literature has shown that better standard-certified accuracy trade-offs can be achieved by combining adversarial training objectives with loose over-approximations based on Interval Bound Propagation (IBP), effectively interpolating between lower and upper bounds of the worst-case loss. Building on this, we introduce AD-CERT, a certified training objective that combines adversarial distillation with an IBP upper bound. We show that distilling adversarial information over the logit space from an empirically robust teacher provides an effective lower bound surrogate for certified training, with AD-CERT achieving state-of-the-art certified performance on several robustness benchmarks. Furthermore, in a unified setup, distilling adversarial information at the logit-level is shown to improve certified accuracy over a robust feature-space distillation objective by up to 5.40 percentage points.

## Metadata
- **Published**: 2026-06-30T13:31:35Z
- **Authors**: Matteo Melis, Jesus Martinez Del Rincon, Vishal Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.31653v1)