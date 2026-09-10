---
title: How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE
published: 2026-09-09T06:48:08Z
authors: Yi Shi, Tanyu Chen, Kai Shen
url: http://arxiv.org/abs/2609.09793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE

## Abstract
Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream. It needs no gradient-based training and no optimization, only a few hundred contrastive prompts, which makes it the canonical white-box attack on open-weight alignment. However, it has been established only on dense models up to roughly 70B parameters. We study whether it survives the shift to frontier mixture-of-experts (MoE) models whose residual streams are no longer a single tensor and whose weights ship quantized. We apply it to GLM-5.3-Flash (320B parameters, 288 routed experts, a four-wide hyper-connection residual, block-FP8). The attack survives the architecture, but what it reaches is no longer where a reader of the original recipe would look for it. Editing the attention, dense and routed-expert writers on their own removes 0.039, 0.016 and 0.148 of refusal respectively; editing all three together removes 0.776. As a result, 74% of the effect exists only under the joint intervention. The part the conventional recipe reaches by module-name matching accounts for 0.066 of that 0.776, which is why it fails silently on an MoE. The effect does not follow from removing just any direction: ablating a random direction orthogonal to it leaves refusal unchanged. A category-concentrated residue survives every edit we tried: subspaces fitted on violence, sexual content and hate leave measurable refusal at every rank from 1 to 12. We report the method, the 41-89 percentage-point reductions it achieves across seven harmful benchmarks with no detected change in capability, and the boundary where it stops.

## Metadata
- **Published**: 2026-09-09T06:48:08Z
- **Authors**: Yi Shi, Tanyu Chen, Kai Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09793v1)