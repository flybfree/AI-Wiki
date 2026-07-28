---
title: Hidden Boundary Motion in Transformer Optimization: Function-Space Orthogonalization of Affine Weight and Bias Updates
published: 2026-07-24T21:51:43Z
authors: Zhang Gongyue, Sheng Yixuan, Liu donghan, Wang Zhiyong, Ren Weihong, Liu honghai
url: http://arxiv.org/abs/2607.22927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hidden Boundary Motion in Transformer Optimization: Function-Space Orthogonalization of Affine Weight and Bias Updates

## Abstract
Weights and biases are normally optimized as separate parameter tensors, yet they do not represent separate functions when the input to an affine layer has nonzero mean. For an affine map $z=Wx+b$ with input mean $μ$, a weight update contains a sample-independent displacement $ΔWμ$ that is functionally indistinguishable from a bias update. We call this hidden contribution \emph{boundary motion} and decompose each update into a centered, sample-varying \emph{shape} component and a shared \emph{boundary} component. On a four-layer Transformer trained from scratch on IMDb, the bias-like term $g_bμ^\top$ has a median norm equal to 0.664 of the raw weight-gradient norm across affine layers and training checkpoints. More strikingly, the median ratio $\norm{ΔWμ}/\norm{Δb}$ is 134.7, while $\norm{ΔWμ}/\norm{Δb+ΔWμ}$ is 0.994. Thus, under AdamW, the observed boundary motion is almost entirely realized through the weight matrix rather than the explicit bias.   We implement a diagnostic optimizer, Shape--Boundary Orthogonal AdamW (SBO-AdamW), that optimizes $g_W-g_bμ^\top$ and $g_b$ with independent Adam states and compensates the weight-induced boundary displacement. In a single-seed experiment, SBO-AdamW raises validation accuracy from 81.68\% to 85.81\% and validation-selected test accuracy from 78.73\% to 82.73\%, with the best validation checkpoint occurring at step 800 instead of step 3000. However, the moving-batch-center compensation produces severe bias-coordinate drift and strongly reduces boundary energy. The present evidence therefore supports hidden boundary motion as an important optimization mechanism, but it does not yet establish a final general-purpose optimizer. A stable centered-affine parameterization is identified as the required next step.

## Metadata
- **Published**: 2026-07-24T21:51:43Z
- **Authors**: Zhang Gongyue, Sheng Yixuan, Liu donghan, Wang Zhiyong, Ren Weihong, Liu honghai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22927v1)