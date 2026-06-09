---
title: Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate
published: 2026-05-20T17:59:40Z
authors: Dayal Singh Kalra, Maissam Barkeshli
url: http://arxiv.org/abs/2605.21486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

## Abstract
Hyperparameter transfer allows extrapolating optimal optimization hyperparameters from small to large scales, making it critical for training large language models (LLMs). This is done either by fitting a scaling law to the hyperparameters or by a judicious choice of parameterization, such as Maximal Update ($μ$P), that renders optimal hyperparameters approximately scale invariant. In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. Next, we investigate through a comprehensive series of ablations why $μ$P appears to offer high-quality learning rate transfer relative to standard parameterization (SP), as existing theory is inadequate. We find that the overwhelming benefit of $μ$P relative to SP when training with AdamW arises simply from maximizing the learning rate of the embedding layer. In SP, the embedding layer learning rate acts as a bottleneck that induces training instabilities; increasing it by a factor of width to match $μ$P dramatically smooths out training while improving hyperparameter transfer. We also find that weight decay improves the scaling law fits, while, in the fixed token-per-parameter setting, it hurts the robustness of the extrapolation.

## Metadata
- **Published**: 2026-05-20T17:59:40Z
- **Authors**: Dayal Singh Kalra, Maissam Barkeshli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.21486v1)