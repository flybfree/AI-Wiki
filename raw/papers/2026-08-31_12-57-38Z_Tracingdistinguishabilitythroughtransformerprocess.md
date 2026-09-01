---
title: Tracing distinguishability through transformer processing with stochastic LayerNorm
published: 2026-08-31T12:57:38Z
authors: Kieran Murphy
url: http://arxiv.org/abs/2608.30720v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing distinguishability through transformer processing with stochastic LayerNorm

## Abstract
Representational similarity is foundational to analyses of deep networks, yet distances between point-valued representations are not intrinsically tied to downstream function: nearby states may produce different behaviors, while distant states may behave similarly. We instead give representations volume, turning similarity into statistical distinguishability. Overlapping stochastic representations necessarily induce overlapping downstream distributions, grounding latent comparison in model function and bringing it under information-theoretic tools such as the data-processing inequality. We realize this idea in pretrained transformers through a light-touch modification to LayerNorm: at each residual-stream read, we normalize the state, add isotropic Gaussian noise, and renormalize. During distillation fine-tuning, one learned allocation parameter per residual-stream read distributes a fixed global rate budget across the processing stack. The resulting model can be viewed as transformer blocks reading the residual stream with learned finite precision under a shared global rate budget. Using the Bhattacharyya coefficient, we trace which counterfactual distinctions are preserved through MLP blocks or selectively exposed to the query, key, and value computations of individual attention heads. Experiments on ViT-S and GPT-2 small reveal the depthwise propagation of continuous visual perturbations and head-specific sensitivity to token distinctions aligned with known attention motifs. These results establish distinguishability as a functionally grounded lens on transformer computation that complements existing interpretability approaches.

## Metadata
- **Published**: 2026-08-31T12:57:38Z
- **Authors**: Kieran Murphy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30720v1)