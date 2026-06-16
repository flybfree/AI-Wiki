---
title: SACE: Concept Erasure at the Semantic Singularity in Visual Autoregressive Models
published: 2026-06-14T13:39:00Z
authors: Siya Yang, Nanxiang Jiang, Zhaoxin Fan, Yunfeng Diao
url: http://arxiv.org/abs/2606.15819v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SACE: Concept Erasure at the Semantic Singularity in Visual Autoregressive Models

## Abstract
The rapid progress of visual autoregressive (VAR) models has unlocked a transformative frontier for high-fidelity text-to-image synthesis, while heightening concerns over the safety alignment of generated content. Naive application of existing erasure techniques to VAR models causes catastrophic semantic collapse and visual artifacts, since they are predominantly designed for the homogeneous denoising steps of diffusion models. To address this foundational challenge, we first propose the Semantic Singularity Axiom, which posits that any target semantic concept embedded within a prompt is definitively locked at Scale-0. Then rigorously validate this axiom through our proposed Incremental Semantic Saliency Analysis (ISSA),which also enable the community to transparently inspect the coarse-to-fine semantic injection process. Guided by this insight, we introduce the first scale-aware concept erasure framework (SACE) for VAR models. By strictly confining interventions to the first scale, our approach couples an Entropy-Regularized Erasure Objective to prevent high-entropy sampling degeneration, alongside a restorative preservation loss to safely anchor the integrity of entangled benign priors. Extensive experiments demonstrate that our method achieves surgical concept erasure performance across various domains with minimal training overhead, timely and elegently resolute the critical safety vulnerabilities inherent in emerging VAR architectures. Code is available at: https://github.com/limerenceysy/SACE}{https://github.com/limerenceysy/SACE.

## Metadata
- **Published**: 2026-06-14T13:39:00Z
- **Authors**: Siya Yang, Nanxiang Jiang, Zhaoxin Fan, Yunfeng Diao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.15819v1)