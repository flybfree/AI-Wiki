---
title: Grounding latent algorithm routing in transformer reasoning
published: 2026-07-27T14:07:12Z
authors: Xiangbo Zhang, Xiaoxu Ma
url: http://arxiv.org/abs/2607.24471v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Grounding latent algorithm routing in transformer reasoning

## Abstract
A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families. We study this question in a controlled setting through latent algorithm routing: route-like behavior in which the solver-family preference changes with the latent data-generating regime while prompt form is held fixed, remains stable under nuisance perturbations, and is selectively influenced by targeted activation interventions without large losses in answer quality. We introduce ROUTEBENCH, a diagnostic benchmark whose regimes differentially favor global shrinkage, sparsity, robustness, and locality, operationalized by ridge-like, lasso-like, Huber-like, and kNN-like family representatives. Across dense decoder-only transformers trained from scratch at 44M-612M parameters, a 306M model closes 80.9 percent of the oracle-routing gap and achieves route F1 of 84.1. The effect remains substantial under natural-language renderings, shuffled supports, lexical paraphrases, and a unified four-way routing setting. Stronger adaptive alternatives, including an input-conditioned soft mixture and an unsupervised Gumbel router, narrow the gap but remain below the 306M and 612M models on route F1 and OOD performance. Probe controls and matched activation-patching controls further show that route-relevant internal directions are decodable and functionally involved in solver-family-consistent output behavior. These results provide controlled evidence that dense transformers trained on ROUTEBENCH can develop route-like internal variables, but they do not establish universal routing in pretrained language models or unrestricted natural-language reasoning.

## Metadata
- **Published**: 2026-07-27T14:07:12Z
- **Authors**: Xiangbo Zhang, Xiaoxu Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24471v1)