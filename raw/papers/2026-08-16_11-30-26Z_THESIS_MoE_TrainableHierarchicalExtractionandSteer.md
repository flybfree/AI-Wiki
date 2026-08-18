---
title: THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts
published: 2026-08-16T11:30:26Z
authors: Kareem Hassani, Chaymaa Abbas, Lama Mawlawi, Mariette Awad
url: http://arxiv.org/abs/2608.15687v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts

## Abstract
Sycophancy, the tendency of a language model to change its answer to match a user's stated belief, is a common alignment failure. Existing activation steering methods typically apply a single contrastive direction uniformly throughout the model, which is an unconditional intervention that alters activations even when no sycophantic behavior is present, trading knowledge retention for behavioral correction. In Mixture-of-Experts (MoE) models, prior work further suggests that behavior is encoded within expert computations rather than routing decisions alone, making precise behavioral steering particularly challenging. In this work, we introduce a shared contrastive signal, built from matched prompts with and without a stated belief, that identifies where sycophancy lives across the MoE hierarchy and drives interventions that act only where the behavior is present. We formulate localization as a causal search over a granularity ladder of MoE blocks, experts, attention blocks, and heads, and compare unconditional subtraction against two conditional alternatives: an analytic projection-based subtraction and a learned per-token gate that steers the model away from sycophancy while keeping its weights frozen. We evaluate on three MoE models measuring sycophancy alongside general knowledge and reasoning benchmarks. Our conditional interventions removed up to 90\% of the belief-induced sycophancy. Our results demonstrate that sycophancy resides in identifiable computational subcircuits and can be selectively steered while maintaining a favorable removal-retention trade-off.

## Metadata
- **Published**: 2026-08-16T11:30:26Z
- **Authors**: Kareem Hassani, Chaymaa Abbas, Lama Mawlawi, Mariette Awad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15687v1)