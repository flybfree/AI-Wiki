---
title: Mask-Based Priors Are More Persistent than Query-Key Initializations
published: 2026-08-01T03:39:57Z
authors: Mingze Ma, Hemanth Saratchandran, Cameron Gordon, Simon Lucey
url: http://arxiv.org/abs/2608.00418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mask-Based Priors Are More Persistent than Query-Key Initializations

## Abstract
Transformers do not merely lack data on some Boolean extrapolation tasks; they generalize in a systematically wrong way. Recent work on generalization on the unseen has shown that, despite fitting the observed domain, Transformers often extrapolate according to a simpler minimum-degree interpolator rather than the true target function. These Boolean tasks are not practical applications, but controlled stress tests for understanding Transformer inductive bias. We ask whether this failure mode can be corrected by injecting explicit structural priors into attention. Existing structured-initialization methods alter Transformer inductive bias indirectly, by choosing query and key projections whose similarity scores approximate a desired attention pattern. However, we find that when applied to Boolean extrapolation, these QK-based priors can be rapidly overwritten during training and fail to change the learned extrapolation rule. We propose a simpler alternative: initialize the additive attention mask directly. Unlike standard hard masks used for causality or locality attention, our mask is a finite, learnable attention-logit bias initialized from task-level interaction structure. This separates the structural prior from content-dependent attention scores, allowing it to persist throughout optimization. On Boolean reasoning tasks, mask-based initialization achieves near-perfect extrapolation where vanilla and QK-initialized Transformers remain trapped by the default inductive bias. The same mechanism also improves low-data arithmetic performance and remains competitive on vision and language benchmarks. These results show that attention masks can serve not only as architectural constraints, but as a simple substrate for encoding persistent inductive bias in Transformers.

## Metadata
- **Published**: 2026-08-01T03:39:57Z
- **Authors**: Mingze Ma, Hemanth Saratchandran, Cameron Gordon, Simon Lucey
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00418v1)