---
title: Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models
published: 2026-08-10T07:49:10Z
authors: Puneet Mathur, Manan Suri, Dinesh Manocha
url: http://arxiv.org/abs/2608.09227v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models

## Abstract
Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive. While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal cross-modal anchors necessary for coherent reasoning. We introduce Omni2LoRA, a two-stage framework for efficient parametric memory compression via coherence-preserving context distillation that bypasses the token bottleneck entirely. First, a Perceiver hypernetwork processes intermediate representations from a frozen OLM to encode the multimodal context into a full-rank Low-Rank Adaptation (LoRA) adapter in a single forward pass. To prevent the resulting parameter footprint from scaling linearly with recording length, we optimize a discrete rank allocation policy via Group Relative Policy Optimization (GRPO) that uses a modality-ablated counterfactual reward to explicitly penalize the loss of audio-visual coherence, forcing the model to allocate its fixed sub-linear rank budget to synergistic cross-modal anchors rather than isolated visual features. Across three omnimodal backbones, Omni2LoRA operating at a 30% rank budget outperforms direct full-context inference and strong token-compression baselines (OmniZip, OMAC, O-MARC) on four audio-visual question answering benchmarks, improving average accuracy by 8-12% over the strongest baseline and remaining stable under compression ratios as tight as 75%, where token-pruning methods degrade sharply. By converting multimodal memory into a fixed-budget, reusable parameter state, our method drives answer-time multimodal-token load to zero, cutting per-query Time to First Token (TTFT) by up to 12x relative to full-context inference and amortizing to under 0.5s after a handful of queries.

## Metadata
- **Published**: 2026-08-10T07:49:10Z
- **Authors**: Puneet Mathur, Manan Suri, Dinesh Manocha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09227v1)