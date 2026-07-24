---
title: U-CFR: Uncertainty-Guided Cascade Forward Refinement for Interactive Segmentation
published: 2026-07-22T20:23:00Z
authors: Elijah Danquah Darko, Min Xian, Terence Soule, Tiankai Yao, Matthew William Anderson
url: http://arxiv.org/abs/2607.20705v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# U-CFR: Uncertainty-Guided Cascade Forward Refinement for Interactive Segmentation

## Abstract
Interactive image segmentation is critical for efficient image annotation; however, existing methods often require many corrective clicks or rely on passive refinement schemes that converge slowly. We propose Uncertainty-Guided Cascade Forward Refinement (U-CFR), a novel inference-time framework that enables models to autonomously self-correct after each user interaction. U-CFR introduces a boundary-aware uncertainty score that fuses segmentation uncertainty, contour gradients, and explicit edge predictions to guide the placement of internal pseudo-clicks. These self-generated clicks target the most ambiguous boundary regions, providing strong corrective signals without additional manual input. To support this process, we design a dual-head network with a shared encoder-decoder backbone: a segmentation head ensures region consistency, while an edge head sharpens boundary alignment. In inference, U-CFR launches a cascade of refinement steps, where each stage leverages the uncertainty-driven pseudo-clicks to refine the mask progressively. Experiments on standard benchmark datasets demonstrate that the proposed U-CFR improves click efficiency, initial mask quality, and boundary accuracy. It reduces the required clicks by over 10% on challenging datasets like Berkeley and offers a more intelligent and efficient interactive annotation.

## Metadata
- **Published**: 2026-07-22T20:23:00Z
- **Authors**: Elijah Danquah Darko, Min Xian, Terence Soule, Tiankai Yao, Matthew William Anderson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20705v1)